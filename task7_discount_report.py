
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percentage = float(input("Enter discount percentage: "))


with open("discount_report.txt", "w") as file:

    file.write("Product | Original Price | Discounted Price\n")
    file.write("--------------------------------------------\n")

    total_discounted_price = 0

    for product, original_price in prices.items():

        discount_amount = original_price * discount_percentage / 100
        discounted_price = original_price - discount_amount

        total_discounted_price += discounted_price

        file.write(
            f"{product} | {original_price:.2f} | {discounted_price:.2f}\n"
        )

   
    total_items = len(prices)
    average_discounted_price = total_discounted_price / total_items

    file.write("\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(
        f"Average Discounted Price: {average_discounted_price:.2f}\n"
    )



with open("discount_report.txt", "r") as file:
    report = file.read()

print("\nDiscount Report:")
print(report)