with open("product.txt", "w") as file:
    for i in range(3):
        product_name = input(f"Enter product{i + 1} name: ")
        price = input(f"Enter price of {product_name}: ")
        file.write(product_name +" | " + price+ "\n")
        
with open("product.txt","r") as file:
    print("Product Information:")
    for line in file:
        print(line.strip())