print("*------------Pizza Delivery JOB -------------*")

size = input("Enter your size do you want ? S, M, L :")


add_pepperoni = input("You want to add pepperoni ? Y ,N :")
extra_cheese = input("You want to extra cheese ? Y ,N :")

# pizza costright 
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# pepperoni pizza cost
small_pizza_a = 15+3
medium_pizza_a = 20+5
large_pizza_a = 25+5

# pepperoni and cheese pizza cost
small_pizza_pc = 15+3+1
medium_pizza_pc = 20+5+1
large_pizza_pc = 25+5+1

# cheese pizza cost
small_pizza_c = 15+1
medium_pizza_c = 20+1
large_pizza_c = 25+1


if size == "S":
    if (add_pepperoni == "Y") and (extra_cheese == "Y"):
        print(f"your pepperoni and extra cheese Small pizza ${small_pizza_pc}")
    elif add_pepperoni == "Y":
        print(f"your pepperoni Small pizza ${small_pizza_a}")
    elif extra_cheese == "Y":
        print(f"you cheese Small pizza ${small_pizza_c}")
    else:
        print(f"your selected Small size pizza ${small_pizza} ")


if size == "M":
    if (add_pepperoni == "Y" ) and (extra_cheese == "Y"):
        print(f"your pepperoni and extra cheese Medium pizza ${medium_pizza_pc}")
    elif add_pepperoni == "Y":
        print(f"your pepperoni Medium pizza ${medium_pizza_a}")
    elif extra_cheese == "Y":
        print(f"you cheese Medium pizza ${medium_pizza_c}")
    else:
        print(f"your selected Medium size pizza ${medium_pizza} ")

if size == "L":
    if (add_pepperoni == "Y") and (extra_cheese == "Y"):
        print(f"your pepperoni and extra cheese Large pizza ${large_pizza_pc}")
    elif add_pepperoni == "Y":
        print(f"your pepperoni Large pizza ${large_pizza_a}")
    elif extra_cheese == "Y":
        print(f"you cheese Large pizza ${large_pizza_c}")
    else:
        print(f"your selected Large size pizza ${large_pizza} ")
