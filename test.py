import menu, os
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
class MyInterface(MenuInterface):
    
    def onStart(self, handler):
        os.system("clear")
        print(handler.getMenu().getName())
        print('')
    
    def onPrint(self, handler, key, name):
        print('   [ {} ] {}'.format(key, name))
    
    def onStop(self, handler):
        print('')
    
    def getUserInput(self, handler):
        return input('Choose >> ')
    
menu = Menu(main_menu)
interface = MyInterface()
handler = MenuHandler(interface, menu)
handler.printMenu()
handler.handle()