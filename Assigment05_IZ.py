# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Irina Zubova,2-14-2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
lstRow = []   # A list of data in the row

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for strData in objFile:
   lstRow = strData.split(",")
   dicRow = {"Task":lstRow[0], "Priority":lstRow[1].strip()}
   lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Task"] + ", " + dicRow["Priority"].strip())
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter the task: ")
        strPrior = input("Enter Priority(Low, Medium, High): " ).title()
        tplPRIOR = ('Low', 'Medium', 'High')
        while strPrior not in tplPRIOR:
            print("Please choose Low, Medium or High")
            strPrior = input("Enter Priority(Low, Medium, High): " ).title()
        
        dicRow = {"Task":strTask.title(), "Priority":strPrior.title()}
        
        if dicRow in lstTable:
            print('Already exist.')
        else:
            lstTable.append(dicRow)
            print("\n Item added.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("Please enter the task you want to delete: ").title()
        for dicRow in lstTable:    
            if strTask == dicRow['Task']:
                lstTable.remove(dicRow)
                print("\n Item removed.")
                break
        else:
            print(strTask, "is not in the Task list.")
        continue
    
    #Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] + '\n')
        print("Data saved to file")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strYorN = input("Are you sure you want to exit? [Y or N] ").upper()
        if strYorN == "Y":
            break # and Exit the program

    else:
        print(strChoice, "is not in the Menu of Options.")
         
         

