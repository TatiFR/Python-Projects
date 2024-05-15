age = input("What is your current age? ")

i_age = int(age)
years = 90 - i_age
days = years * 365
s_days = str(days) + " days, "
weeks = years * 52
s_weeks = str(weeks) + " weeks, and "
months = years * 12
s_months = str(months) + " months left."
print("You have " + s_days + s_weeks + s_months)
