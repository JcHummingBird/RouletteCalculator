#Roulette Calculation for Pit Supervisor or a Surveillance Officer

#Calculating Straight Up bets
multiplicand = int(input("How many pieces in Straight Up? : "))
product = multiplicand * 35
print("Straight Up: ", product)

#Calculating Split bets
multiplicand_1 = int(input("How many pieces in Split? : "))
product_1 = multiplicand_1 * 17
print("Split: ", product_1)


#Calculating Corner bets
multiplicand_2 = int(input("How many pieces in Corner? : "))
product_2 = multiplicand_2 * 8
print("Corner: ", product_2)


#Calculating Streets bets
multiplicand_3 = int(input("How many pieces in Streets? : "))
product_3 = multiplicand_3 * 11
print("Streets: ", product_3)


##Calculating Six Line bets
multiplicand_4 = int(input("How many pieces in Six Lines? : "))
product_4 = multiplicand_4 * 5
print("Six Lines: ", product_4)


#add the products of each type of bets
sum = product + product_1 + product_2 + product_3 + product_4
print("Total: ", sum)

#convert the sum to any cash chip value
cashChipValue = int(input("Enter a denomination: "))
print("You need to prepare: $ ", cashChipValue * sum)
