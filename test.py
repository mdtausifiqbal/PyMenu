import menu
from menu import *

def hello():
    print("Hello World")
    
def hello2():
    print("Hello2")
    
def subHello():
    print("Sub Hello World")

main_menu = {
    "name" : "Main Menu",
    "type" : "main_menu",
    "items" : [
        {
            "name" : "Item 1",
            "function" : hello
        },
        {
            "name" : "Item 2",
            "function" : hello2
        },
        {
            "name" : "Sub Menu",
            "menu" : {
                "name" : "Sub Menu",
                "items" : [
                    {
                        "name" : "Sub Item 1",
                        "function" : subHello
                    }
                ]
            }
        }
    ]
}
menu = Menu(main_menu)
handler = MenuHandler()
handler.setMenu(menu)
handler.printMenu()
handler.handle()