# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

# The function should return the final price after applying the discount if applicable.


def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(price, discount_percent)

        if final_price == price:
            print(f"No discount applied. The original price is: ${price:.2f}")
        else:
            print(f"The final price after applying the discount is: ${final_price:.2f}")

    except ValueError:
        print(
            "Invalid input. Please enter numeric values for price and discount percentage."
        )


def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        return price
    else:
        return price - (price * discount_percent / 100)
