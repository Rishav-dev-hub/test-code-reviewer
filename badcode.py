import os
import sqlite3

password = "admin123"
API_KEY = "secret_api_key_12345"

conn = sqlite3.connect("users.db")

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = conn.execute(query)
    return result.fetchall()

def run_command(cmd):
    os.system(cmd)

def execute(user_input):
    return eval(user_input)

def divide(a,b):
 return a/b

def process(data):
    if data == None:
        print("No data")
    else:
     print(data)

def login(username,password):
    if username=="admin" and password=="admin":
        return True
    return False

for i in range(10):
 print(i)

unused_variable = 12345
