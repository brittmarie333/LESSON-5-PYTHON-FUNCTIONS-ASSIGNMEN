#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#Task 1: Write a function that lets the user add items to a list.

def viewList():
    for i in shoppingList:
        print(i)

def addItem():
    item = input("add item: ")
    shoppingList.append(item)
    print(item + "has been added ")


shoppingList = ['apples', 'bananas']  

print("what would you like to do?" 
    "1. View List, 2. Add item")

selection  = input("")
              
if selection == "1":
    viewList()
elif selection == "2":
    addItem()
else:
    print("Invalid selection")