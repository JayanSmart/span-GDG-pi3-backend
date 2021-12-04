# PI3 backend for scanning social media profile similarities

import os
from flask import Flask, request, jsonify

import lib.db
import lib.scanner.twitter.twitter as twit
import lib.scanner.twitter.bsoup as bsoup

# Initialize Flask app
app = Flask(__name__)

# Init firestore connection:
db_conn = lib.db.create_connection()
user_ref = lib.db.get_collection(db_conn, 'users')


@app.route("/hello")
def hello():
    return "hello! Welcome to PIII!"


@app.route("/soup/test")
def soup_test():
    return bsoup.search_by_displayname("Robyn Thomas")


@app.route("/scan/twitter/displayname/<username>")
def scan_twitter(username):
    print("Searching for: " + username)
    accounts = twit.search_by_username(username)
    flaged = check_duplicates(user_id, accounts)

    return users.json()


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
