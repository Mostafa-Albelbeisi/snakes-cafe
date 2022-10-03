
if __name__ == "__main__" :
    
    our_menu = ("Wings", "Cookies", "Spring Rools",
                "Salmon", "Steak", "Meat Tornado", "A literal Garden",
                "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears")

print('''
         **************************************
         **    welcome to the snack cafe!    **
         **    Please see our menu below.    **
         **
         **   To quit any time, type "quit"  **
         **************************************
''')

MENU = '''
        Menu:

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
         Unicron Tears

         ***********************************
         ** What would you like to order? **
         ***********************************
         '''

user_order = {}
print(MENU)
while True : 
        order = input("> ").capitalize()
        if order in our_menu:
            user_order[order] = user_order.get(order, 0) + 1
                    
            print("** " , end = "")
            for meal in user_order:
                
                if user_order[meal] == 1:
                    print(f"1 order of {meal} ", end="")
                elif user_order[meal] > 1:  
                    print(f"{user_order[meal]} orders of {meal} ", end="")  
                    print("Has been added to your meal **")
        
        elif order == "Quit":
            if len(user_order) == 0:
                print("Have a nice Day! ")
            else :
                    print("You ordered: ")
            for meal in user_order:
                print(user_order[meal] , meal)
            break       

        else :
            print(f'''
            ************************************************
            Could not find {order}

            Please choice the correct ordering from our menu
            ************************************************
            ''')
            # print(MENU)
               
