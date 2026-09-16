import sqlite3
from flask import Flask
#render_template, request, jsonify

#sqlite database connection. 
def db_init():
    con = sqlite3.connect("testDatabase.db") #get connection
    with open("schema.sql","r") as file: # opens the template for the database table
        con.executescript(file.read()) # creates the table
    con.close()
#This is for Flask to know the app
app = Flask(__name__)

#Routes to the home http file
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Execute following code if this file is main
if __name__ == '__main__':
    db_init