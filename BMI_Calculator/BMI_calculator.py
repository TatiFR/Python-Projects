height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

f_height = float(height)
f_weight = float(weight)
bmi = f_weight / (f_height * f_height)
i_bmi = int(bmi)
print(i_bmi)
