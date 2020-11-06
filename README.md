# PyMenu
A module for building menus in python.

## Screenshot
![screenshot](/screenshot/snap1.png?raw=true "PyMenu Snap")

## Syntax
### Menu Item
```python
Item = {
  "name" : "Item name",
  "function" : function
}
```
### Menu
```python
menu = {
  "name" : "Menu Name",
  "type" : "main_menu",
  "items" : [
    {"name" : "Item 1", "function" : function1},
    {"name" : "Item 2", "function" : function2}
  ]
}
```
### Nested Menu
```python
menu = {
  "name" : "Menu Name",
  "type" : "main_menu",
  "items" : [
    {"name" : "Item 1", "function" : function1},
    {"name" : "Item 2", "function" : function2},
    {
      "name" : "More",
      "menu" : {
        "name" : "Sub Menu",
        "items" : [
          {"name" : "Item 1", "function" : function3},
          {"name" : "Item 2", "function" : function4}
        ]
      }
    }
  ]
}
```
---
## Example

### Define Functions for Menu Item
```python
def hello():
    print("Hello World")
    
def hello2():
    print("Hello2")
    
def subHello():
    print("Sub Hello World")
```
### Define Main Menu
```python
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
```

### Define Interface
```python
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
        return input('Choose Option >> ')
```
### Bind to Menu Handler
```python
from menu import Menu, MenuHandler
menu = Menu(main_menu)
interface = MyInterface()
handler = MenuHandler(interface, menu)
handler.printMenu()
handler.handle()
```
