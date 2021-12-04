# PI3 backend for scanning social media profile similarities

import os
from flask import Flask, request, jsonify, Response

import lib.db
import lib.scanner.twitter.twitter as twit
import lib.scanner.twitter.comparitor as comparator

# Initialize Flask app
app = Flask(__name__)

# Init firestore connection:
db_conn = lib.db.create_connection()
user_ref = lib.db.get_collection(db_conn, 'users')


@app.route("/hello")
def hello():
    return "hello! Welcome to PIII!"


@app.route("/scan/twitter/<app_user>/<twitter_user>")
def scan_twitter(app_user, twitter_user):
    user_account = twit.get_user_profile_data(twitter_user)
    similar_accounts = twit.search_by_username(twitter_user)
    cases = comparator.check_duplicates(
        user_account.json(), similar_accounts.json())

    for case in cases:
        # Add cases to firestore
        lib.db.add_cases(db_conn, app_user,
                         "https://twitter.com/" + case['username'])
    return Response("{}", status=200, mimetype='application/json')


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
