print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#0. Convert each name to lowercase
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

#1. Count number of letters from "True" occur in each name
t_letter = int(lower_case_name1.count("t") + lower_case_name2.count("t"))
r_letter = int(lower_case_name1.count("r") + lower_case_name2.count("r"))
u_letter = int(lower_case_name1.count("u") + lower_case_name2.count("u"))
e_letter = int(lower_case_name1.count("e") + lower_case_name2.count("e"))

#1.1 Store letter count
letter_count_true = str(t_letter + r_letter + u_letter + e_letter)

#2. Count number of letters from "Love" occur in each name
l_letter = int(lower_case_name1.count("l") + lower_case_name2.count("l"))
o_letter = int(lower_case_name1.count("o") + lower_case_name2.count("o"))
v_letter = int(lower_case_name1.count("v") + lower_case_name2.count("v"))
e_letter = int(lower_case_name1.count("e") + lower_case_name2.count("e"))
#2.1 Store letter count
letter_count_love = str(l_letter + o_letter + v_letter + e_letter)

#3. Combine numbers to a 2 digit number to determine score
score = letter_count_true + letter_count_love
int_score = int(score)

#4. Print the output and recommendation 
if int_score < 10 or  int_score > 90:

    print(f"Your score is {score}, you go together like coke and mentos.")
elif int_score  > 40 and  int_score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
