new_sales = [5000, 2500, 1700]
with open("sales_data.txt","a") as file:
    for sales in new_sales:
        file.write(str(sales)+"\n")
with open("sales_data.txt", "r") as file:
    updated_data =file.read()
print("Updated sales record:")
print(updated_data)
with open("sales_data.txt","r") as file:
    lines = file.readlines()
print("Total number of sales: ")
print(len(lines))