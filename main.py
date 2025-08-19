def calculate_discount(price, discount_percent):
    """Apply discount only if it is 20% or higher."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

try:
    original_price = float(input("👉 Enter the original price of the item: "))
    discount = float(input("👉 Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"✅ Discount applied! Final price is: {final_price:.2f}")
    else:
        print(f"❌ No discount applied. Price remains: {final_price:.2f}")

except ValueError:
    print("⚠️ Invalid input. Please enter numbers only.")
