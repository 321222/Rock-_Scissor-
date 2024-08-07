print("Welcome to bakery system:")
order=str(input("Enter the order:"))
print(order)
total_order=input(("total number of order:"))
print(total_order)
food_charge=int(input("Enter the food charge:"))
print(food_charge)
gst=int(input("Enter the GST charge :"))
print(gst)
Total_charge=food_charge + gst/100
print(total_order)
if Total_charge >=1000:
    print("Have a cupon")
elif Total_charge >=800:
    print("we have discount in order:")
else:
    print("Sorry we have not offer")

cupon_code=int(input("Enter the cupon code:"))
print(cupon_code)
cupon_charge=int(input("Enter the cupon given to user :"))
if cupon_charge >=1000:
    cupon=Total_charge-28/100
print(cupon)
discount_a=int(input("Enter the discount available:"))
print(discount_a)
discount=total_order-discount_a/100
print(discount)

