import mysql.connector
from flask import Flask
import random

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer"
)

mycursor = mydb.cursor()


@app.route("/")
 
def getDatabase():
    query = "select * from customers"
    mycursor.execute(query)
    myresults = mycursor.fetchone()
    showDatabase = "<h1>" + myresults + "<h1>"
    return showDatabase

if __name__ == "__main__":
    app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    