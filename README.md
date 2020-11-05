# PyMenu
A module for building menus in python.
## Syntax
### Menu Item
```
Item = {
  "name" : "Item name",
  "function" : function
}
```
### Menu
```
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
```
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
  ]
}
```
---
## Example

### Define Functions for Menu Item
```
def hello():
    print("Hello World")
    
def hello2():
    print("Hello2")
    
def subHello():
    print("Sub Hello World")
```
### Define Main Menu
```
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
### Bind to Menu Handler
```
from menu import Menu, MenuHandler
menu = Menu(main_menu)
handler = MenuHandler()
handler.setMenu(menu)
handler.printMenu()
handler.handle()
```
