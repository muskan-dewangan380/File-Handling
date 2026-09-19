with open("sales_data.txt", 'r') as file:
    lines = file.readlines()
sales = [int(line.strip()) for line in lines]
total_sale = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sale/ len(sales)
print("sales summary report")
print("Total Sale:", total_sale)
print("Highest sale:", highest_sale)
print("Average sale : " , average_sale)
print("Lowest sale: ", lowest_sale)