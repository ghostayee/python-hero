my_list = [
    "Phase 1",
    ". Python Foundations",
    "Master:",
    "• Variables and data types",
    "• Functions",
    "• Loops and conditions",
    "• Lists, dictionaries, tuples, sets",
]


file1 = open("my-data", "a")
for list in my_list:
    file1.write(my_list)

file2 = open("my-data", "r")
content = file2.read()
print(f"these are the contents:{content}")


file = open("honor", "w")
file.write("Honor dad and mum ")

file = open("honor", "a")
file.write("pleasure to be your dad and mum ")
