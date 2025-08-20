def calculate_discount(price, discount_percent):
    if discount_percent > 0.2:
        calculated_price = price * discount_percent
        print(calculated_price)
    else:
        calculated_price = price
        print(calculated_price)


price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent (like 0.2 for 20%): "))


calculate_discount(price, discount_percent)
