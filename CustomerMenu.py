import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="customer"
)

mycursor = mydb.cursor()

def createTable():
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    
createTable()

def queryEvy():
    query = "select * from customers"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

def addCustomer(name, address):
    sqlAdd = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    valAdd = (name, address)

    mycursor.execute(sqlAdd, valAdd)

    mydb.commit() #Must commit to save changes

    print("Entry Added.")

def deleteCustomer(row):
    sqlDel = "DELETE from customers where id = " + row
    
    mycursor.execute(sqlDel)
    
    mydb.commit()
    
    print("Entry Deleted")

def editCustomer(id, name, address):
    sqlEdit = "REPLACE INTO customers (id, name, address) VALUES (%s, %s, %s)"
    valEdit = (id, name, address)

    mycursor.execute(sqlEdit, valEdit)

    mydb.commit() #Must commit to save changes

    print("Entry Edited.")

def mainMenu():
    print("")
    print("Welcome to the database, please enter the number according to the action you want")
    print("If you are in an action and want to cancel, type 'end' (You may need to enter every field before it brings you to the menu)")
    print("===================================================")
    print("1. View Database")
    print("2. Add into Database")
    print("3. Delete from Database")
    print("4. Update Entry in Database")
    print("5. Exit the Program")
    print("===================================================")
    print("")

programRun = True
while programRun == True:
    mainMenu()
    menuChoice = input("Please enter a number: ")
    
    if menuChoice == "1":
        query = "select * from customers"

        mycursor.execute(query)

        myresult = mycursor.fetchall()

        print("ID, Customer Name, Address")
        for row in myresult:
            print(row)
        
        print("")
        backToMenu = input("Please Enter Anything to Continue: ")
    
    elif menuChoice == "2":
        nameAdd = input("Please enter your name: ")
        addressAdd = input("Please enter your address: ")
        if nameAdd == "end":
            print("Canceled")
        else:
            query = "select * from customers"
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            dupe = False
            for row in myresult:
                if row[1] == nameAdd:
                    if row[2] == addressAdd:
                        print("Same entry already in Database")
                        dupe = True
                    else:
                        print("")
                else:
                    print("")
            if dupe == False:
                addCustomer(nameAdd, addressAdd)
            else:
                print("")
      
        backToMenu = input("Please Enter Anything to Continue: ")
        
    elif menuChoice == "3":
        rowDel = input("Please enter the row id you want to delete: ")
        if rowDel == "end":
            print("Canceled")
        else:
            query = "select * from customers where id = '" + rowDel + "'"
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)
                
            confirmDel = input("Confirm Delete? Press 1 for yes, Press 2 for no: ")
            if confirmDel == "1":
                queryEvy()
                deleteCustomer(rowDel)
            elif confirmDel == "2":
                print("Canceled")
                
            else:
                print("Unknown Input, Action Canceled")
        
        print("")
        backToMenu = input("Please Enter Anything to Continue: ")
        
    elif menuChoice == "4":
        rowEdit = input("Please enter the row id you want to edit: ")
        if rowEdit == "end":
            print("Canceled")
        else:
            nameEdit = input("Enter new name: ")
            addressEdit = input("Enter new address: ")
            editCustomer(int(rowEdit), nameEdit, addressEdit)
            
        print("")
        backToMenu = input("Please Enter Anything to Continue: ")
        
    elif menuChoice == "5":
        print("Ending Program, Have a nice day")
        programRun = False
    
    elif menuChoice == "Pun":
        print("haha very funny, just for that I am ending this program")
        programRun = False
        
    else:
        print("Unknown Input Detected")

