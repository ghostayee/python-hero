The roadmap to mastery in flask
1. variables and data types in python
==> text="string"
==> num = 5 == integer
==> boolean true or false statement like is_student = true all false.
==> Float 10.05
==> complex real and imaginary part (1 + 2j)

others include:
=> list
=> tuple
=> dict
=> range.
=> set - mutable
=>frozen set = immutable type of set.

Variables
>-- multiple assign of variables =>> 
> x, y, z =1, 2, 3



>-- FUNCTIONS 
python functions are reusable blocks of code accept inputs and parameters 

>-- modularity 
>-- avoid repeat

>--- when * i used then its unpacking 
in this manner any function for example:

def order-pizza(size, *toppings, **details):
    print(f"you ordered {size} pizza with the following toppings:")
    for topping in toppings
    print(f"-{topping}")


Decorator function:
>-- add something to base function without changing it 
we use a wrapper function 
def wrapper():
    print("add some chicken peri")
    return


loops and condition
>-- for i in fruits:
>--print(i)


short hand if else statement 
>-- print("you can't vote") if age < 18 else print("you can vote done") 
print("done")

>-- list
they are mutable
can be accessed by index


list1.extend(list2)
fruits.append("mango")
insert >--- list.insert(0, "python)

>-- dictionaries are ordered mutable and unique
>-- dict = {
"usa":"washington"
}
update can add or change 
capital.popitem()

for values() and keys()


>-- sets 
no duplicates in sets 
they are unordered


.remove can help you type the value and remove


>-- Files handling in python 

r = read
a = append
w = write
x = create