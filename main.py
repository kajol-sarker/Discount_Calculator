bill_amount = int(input("Enter customer bill amount: "))

DISCOUNT_RATE_10_PERCENT = 0.10
DISCOUNT_RATE_20_PERCENT = 0.20

if bill_amount > 1000:
    discount_amount = bill_amount * DISCOUNT_RATE_20_PERCENT
    final_price = bill_amount - discount_amount
    print(f"Discount Amount: {discount_amount:.2f} taka")
    print(f"Final Bill: {final_price:.2f} taka")
elif bill_amount > 500: 
    discount_amount = bill_amount * DISCOUNT_RATE_10_PERCENT
    final_price = bill_amount - discount_amount
    print(f"Discount Amount: {discount_amount:.2f} taka")
    print(f"Final Bill: {final_price:.2f} taka")
else:
    print("No discount applicable.")
    print(f"Final Bill: {bill_amount:.2f} taka")