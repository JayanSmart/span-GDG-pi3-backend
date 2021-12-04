# app.py

# Required imports
import os
from flask import Flask, request, jsonify
import db

# Initialize Flask app
app = Flask(__name__)

#Init firestore connection:
db_conn = db.create_connection()
user_ref = db.get_collection(db_conn, 'users')

@app.route("/hello")
def hello():
    return "hello! Welcome to PIII!"



port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
