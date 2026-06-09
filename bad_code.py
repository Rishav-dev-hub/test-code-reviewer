import os
import json
import requests

password = "supersecret123"
api_key = "sk-live-abc123"

def get_user(username):
    query = "SELECT * FROM users WHERE name='" + username + "'"
    db.execute(query)

def login(user, pwd):
    if pwd == password:
        return True

result = eval(input("Enter command: "))
