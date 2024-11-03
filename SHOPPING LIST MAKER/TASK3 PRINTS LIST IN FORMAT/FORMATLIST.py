#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#Task 3: Add a function that prints out the entire list in a formatted way.


def viewList():
    for i in shoppingList:
        print("Your list contains: " + str(shoppingList), end="")
              
def addItem():
    item = input("add item: ")
    shoppingList.append(item)
    print((item + " has been added"))

def removeItem():
    item = input("item: ")
    shoppingList.remove(item)
    print(item + " has been removed")

shoppingList = ['apples', 'bananas']  

print("what would you like to do?" 
    "1. View List, 2. Add item, 3. Remove item, ")

selection  = input("")
                   
if selection == "1":
    viewList()
elif selection == "2":
    addItem()
elif selection == "3":
    removeItem()
else:
    print("Invalid selection")