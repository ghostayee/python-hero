my_list = "Lists, dictionaries, tuples, sets\n"

file1 = open("my-data-center", "w")
file1.write(f"{my_list}")

file1 = open("my-data-center", "a")
file1.write("hello world the first step \nThe most interactive part")

file1 = open("my-data-center", "r")
for data in file1:
    file1.write(data)
