print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
services=["wings","cookies","spring rolls",
    "salmon","steak","meat tornado","a literal garden",
    "coffee","tea","unicorn tears"]
    
list_order=[]

order= input()
order=order.lower()
while order != "quit":
         
    if order in services:

        list_order.append(order) 
        coun=list_order.count(order)   
        print(f"** {coun} order of {order.capitalize()} have been added to your meal **")

    elif order=='quit':
        break       
    else:
        print("this order not fund in the list")    
    order=input('** What would you like to order? **')
for i in list_order:
    print(i)

  