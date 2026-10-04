# THE SMART CART OPTIMIZER 
#You are writing a crash register system for a small grocery checkout.This system must handle data more 
#efficiently and gracefully recover if a user inputs the wrong type of data.
# CORE REQUIREMENT : THE MENU DICTIONARY :Before starting any loops , create a single python dictionary 
# called 'menu' that holds these items and prices .
#"apple" :$1.50,"bread":$2.50,"milk":$3.00
#THE MAIN LOOP AND EXIT :create a continuous loop .
#.promt the user for an item .If they enters "checkout" the loop breaks and prints the final shift totals.
#THE CRASH-PROOF QUANTITY(CRASH VALIDATION):Promt the user for the quantity as an integer .
#THE TWIST :You must wrap this input in a try - except valueerror block.If the user acidentally types a 
#word like ("two")intead of a number 2 the program must not crash .instead it should print "please enter a 
# valid whole number" and ask for the quantity again .
#MATHS & UPDATE :Look up the price directly from the dictionary (menu[item]).Calculate the cost , update your 
# accumulators , and print the current receipt line .

menu = {"apple": 1.50,
        "bread":2.50,
        "milk":3.00
}

total_items_bought = 0
total_cart_value = 0 

while True:
    price = 0
    item = str(input("enter the name of the item you wanna buy(or 'checkout' to end the shift) :")).lower().strip()
    if item == "checkout":
        break 
    if item in menu :
        price = menu[item]  

        while True:
                try:
                     quantity = int(input("enter quantity :"))
                     break
                except ValueError:
                     print("please enter a valid whole number.")
    
        total = price * quantity
        print("your total is :$",total)  
        total_items_bought +=quantity
        total_cart_value +=total  
    else:
                print("we dont carry that item ,try again")          

print("your total items sold today are:",total_items_bought) 
print("your today's cart value is:",total_cart_value)   