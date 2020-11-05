import os
from abc import ABC, abstractmethod

class MenuItem:
    BACK = {"name" : "Back"}
    EXIT = {"name" : "Exit"}

    #data is dict type
    def __init__(self, data=dict()):
        self.data = data

    #it checks whether a Menu Item has function key or not
    def has_function(self):
        return "function" in self.data

    #it checks whether a Menu Item has menu key or not
    def has_menu(self):
        return "menu" in self.data

    #this sets the name in of Menu Item
    def setName(self, name):
        self.data['name'] = name

    #it returns the name of Menu Item
    def getName(self):
        if "name" in self.data:
            return self.data['name']
        else:
            return None
    
    #sets Menu Object to the data of MenuItem
    def setMenu(self, menu):
        self.data['menu'] = menu.data

    #return type is Menu Object
    def getMenu(self):
        if self.has_menu():
            return Menu(self.data['menu'])
 
    #sets the function to the data of MenuItem
    def setFunction(self, func):
        self.data['function'] = func

    #It returns the function from Menu Item data
    def getFunction(self):
        if self.has_function():
            return self.data['function']
        else:
            return None

    #it invokes function of Menu Item
    def call(self):
        if self.has_function():
            self.data['function']()


class Menu:
    
    #data is dict type
    def __init__(self, data=dict()):
        self.data = data
        self.items = list()

        if self.isMain():
            self.addMenuItem(MenuItem.EXIT)
        else:
            self.addMenuItem(MenuItem.BACK)

    #sets the name of menu
    def setName(self, name):
        self.data['name'] = name

    #returns the name of Menu
    def getName(self):
        if "name" in self.data:
            return self.data['name']

    #sets the type of Menu, for Main Menu must be used 'main_menu' type
    def setType(self, type):
        self.data['type'] = type

    #returns the type of Menu, 
    def getType(self):
        return self.data['type'] if 'type' in self.data else "sub_menu"

    #items is list of MenuItem Object
    def setItems(self, items):
        self.data['items'] = items

    #return is list of MenuItem Object
    def getItems(self):
        return self.data['items']

    #it checks whether a menu has key which is given by input
    def isKeyExists(self, key):
        #print('Internal key existance called')
        if(self.totalItem() > 0):
            return (key > 0 and key <= self.totalItem())
        else:
            return False

    #it returns the number of total Menu Items present in Menu
    def totalItem(self):
        return len(self.getItems())

    #it appends the Menu Item data to the Menu
    def addMenuItem(self, item):
        self.getItems().append(item)

    #it checks whether menu is main or not
    def isMain(self):
        return self.getType() == 'main_menu'

class MenuInterface(ABC):
    #this method is invoked on getting user input
    @abstractmethod
    def getUserInput(handler):
        pass
    
    #this method is invoked before start printing the menu items
    @abstractmethod
    def onStart(handler):
        pass
    
    #this method is invoked while printing each menu items
    @abstractmethod
    def onPrint(handler, key, name):
        pass
    
    #this method is invoked after completing the print menu items
    @abstractmethod
    def onStop(handler):
        pass
    
class MenuHistory:
    
    def __init__(self):
        self.menu_list = list()
    
    #it append menu object to the list of menu
    def add(self, menu):
        self.menu_list.append(menu)
    
    #it deletes particular menu from history
    def delete(self, menu):
        self.menu_list.remove(menu)
        
    #it deletes last one menu from history
    def deleteLast(self):
        return self.menu_list.pop()
    
    #it clears all history
    def clear(self):
        self.menu_list.clear()
        self.menu_list = list()
        
    
class MenuHandler:

    def __init__(self):
        self.history = MenuHistory()

    #menu is type of Menu Object not dict type
    def setMenu(self, menu):
        self.menu = menu
        self.getHistory().add(menu)

    #return is type of Menu Object not dict type
    def getMenu(self):
        return self.menu
    
    #it will set the history for handler
    def setHistory(self, history):
        self.history = history
        
    #it returns the list of Menu Object from history
    def getHistory(self):
        return self.history

    #this function is used for switching back to the parent menu if exists
    def back(self):
        #remove current menu from history
        self.getHistory().deleteLast()
        parentMenu = self.getHistory().deleteLast()
        self.setMenu(parentMenu)
        self.printMenu()

    #this is an interface for defining the User Prompt text
    def getInput(self):
        return input("Choose Option >> ")

    #it prints the menu in default style from handler
    def printMenu(self):
        os.system("clear")
        menuItems = self.getMenu().getItems()
        print('')
        for i in range(len(menuItems)):
            key = i + 1
            name = MenuItem(menuItems[i]).getName()
            print("   [ {} ] {}".format(key, name))
        print('')

    #this function is used for handle the user input and interacts with the menu and sub menu and menu item
    def handle(self):
        while(True):
            #Here we getting menu because object can be changed while user input.
            menu = self.getMenu()
            i = self.getInput()
            try:
                index = int(i)
                if menu.isKeyExists(index):
                    item = MenuItem(menu.getItems()[index-1])
                    if(item.getName() == 'Exit'):
                        break
                    elif(item.getName() == 'Back'):
                        self.back()
                    else:
                        if(item.has_function()):
                            item.call()
                        elif(item.has_menu()):
                            self.setMenu(item.getMenu())
                            self.printMenu()
                        else:
                            print("No any function or menu is defined for this Option.")
                else:
                    print("Invalid Input, option doesn't exists !!")
            except:
                print("Invalid user input data type.")
            
