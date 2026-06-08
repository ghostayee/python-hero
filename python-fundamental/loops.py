count = 0
while count < 5:
    print("I am sorry")
    count += 1

num = int(input("Enter a number and will determine whether is ODD or EVEN:"))
if num % 2 == 0:
    print(num, "EVEN number")
else:
    print(num, "ODD number")
    
    
    
for num in range(1, 100):
    if num % 2 == 0:
        print(num, "its a EVEN number")
    else:
        print(num, "ODD number")