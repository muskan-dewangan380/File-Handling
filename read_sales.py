with open("sales_data.txt","r") as file:
    contents = file.read()
print("Using read():")
print(contents)

with open("sales_data.txt","r")as file :
    first_line = file.readline().strip()
print("Using readline():")
print(first_line)
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
sales= [int(line.strip()) for line in lines]
print("Using readlines():")
print(sales)