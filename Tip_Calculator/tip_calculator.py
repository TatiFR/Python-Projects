#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = float(input("What was the total costs of the bill? $"))
decimals = round(bill, 2)

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
percentage = tip / 100
f_tip = float(percentage)
add_bill = bill * f_tip
total_bill = bill + add_bill

i_total = int(decimals)

people = int(input("How many people would you like to split the bill? "))
individual = i_total / people
s_indiv = str(individual)

print("Each person should pay: $" + s_indiv)
