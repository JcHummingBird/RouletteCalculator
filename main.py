a = 2
b = 3.8
print(a*b)
print(type(b))
print(type(a))


yourBill = float(input("How much is your total bill?"))
print(yourBill)
serviceCharge = 4 / 100 * yourBill
tips = int(input("How much tip would you give?"))
totalBill = yourBill + serviceCharge + tips
print(f"Your total bill:   ${totalBill:.2f}")




