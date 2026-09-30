import sqlite3

### Functions ###
def get_db_cursor():
    con = sqlite3.connect("testDatabase.db")
    return con.cursor()

def db_init():
    con = sqlite3.connect("testDatabase.db") #get connection
    with open("schema.sql","r") as file: # opens the template for the database table
        con.executescript(file.read()) # creates the table
    con.close()