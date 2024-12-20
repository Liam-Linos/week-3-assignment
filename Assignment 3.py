def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    
    Parameters:
    price (float): Original price of the item.
    discount_percent (float): Discount percentage to be applied.
    
    Returns:
    float: Final price after applying the discount, or original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
if __name__ == "__main__":
    # Prompt user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Print the final price or original price
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
