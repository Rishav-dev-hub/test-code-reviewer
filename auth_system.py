import os
import json
import requests
import hashlib
import pickle
skbcbhedcbhjd
# Hardcoded credentials - very bad practice
SECRET_KEY = "mysupersecretkey123"
DB_PASSWORD = "admin1234"
API_TOKEN = "sk-live-xK9pQr2mX"

DEBUG = True
wkjefe
Debug=false
# User database (stored as plain text passwords)
users = {
    "admin": "password123",
    "john": "john1234",
    "alice": "alice5678"
}

def get_user_from_db(username):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE username='" + username + "'"
    result = db.execute(query)
    return result

def hash_password(password):
    # MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username, password):
    if username in users:
        # Comparing plain text passwords
        if users[username] == password:
            return True
    return False

def load_user_session(session_data):
    # pickle.loads is dangerous with untrusted data
    user = pickle.loads(session_data)
    return user

def run_admin_command(cmd):
    # eval is extremely dangerous
    result = eval(cmd)
    return result

def get_all_users():
    # Fetching without authentication check
    query = "SELECT * FROM users"
    all_users = db.execute(query)
    # printing sensitive data to console
    print("All users password:", users)
    return all_users

def process_input(user_input):
    # exec is dangerous
    exec(user_input)

# unused variable
temp_data = [1,2,3,4,5]
unused_config = {"key": "value"}

def calculate(x,y):
    result=x+y
    temp=x*y
    return result
