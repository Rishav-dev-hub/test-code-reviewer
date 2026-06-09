import os
import requests

password = "supersecret123"
api_key = "sk-live-xK9pQr"

def get_user(username):
    query = "SELECT * FROM users WHERE name='" + username + "'"
    return query

result = eval(input("Enter: "))
