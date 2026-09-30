import sqlite3
import os # Used for keeping environment variable secret
from flask import Flask, render_template, request, session, redirect

import database


### Setup Vars###
app = Flask(__name__) #This is for Flask to know the app
app.secret_key = os.getenv('FLASK_SECRET_KEY')

def db_init():
    con = sqlite3.connect("testDatabase.db") #get connection
    with open("schema.sql","r") as file: # opens the template for the database table
        con.executescript(file.read()) # creates the table
    con.close()



### Routes ###
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        #check if username and password are in the database 
        #if yes add user id to session
        #if no add them to the database and create id 
        #maybe redirect to dashbord
        #make dashboard.html
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        return #error / not in session


#Execute following code if this file is main
if __name__ == '__main__':
     db_init()
     app.run(debug=True)
