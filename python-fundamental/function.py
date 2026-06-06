def greetings (name):
    greetings = "hello"
    print(f"{greetings} {name}")
    
    return greetings
    


greetings("john")


def describe_pet (*args, **kwargs):
    print(args)
    print(kwargs)
    
describe_pet()

def order_pizza (size, *toppings, **details):
    print(f"ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        print("\nDetails of our order are:")
        for key, value in details.items():
            print(f"- {key}: {value}")
    
order_pizza("large", "peperoni", "chicken peri peri", delivery=True, tip=5)