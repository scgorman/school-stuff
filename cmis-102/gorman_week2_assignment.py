# This program calculates and prints the total salary of a newspaper carrier along with the total salary's components.

# Prompt user for the necessary amounts of papers, days, and tips
amt_papers = eval(input("How many papers are delivered on the route?"))
amt_days_delivered = eval(input("How many days per week is is the paper delivered?"))
amt_tips = eval(input("What was the amount of tips received for the week?"))

# print(str(amt_papers) + str(amt_days_delivered) + str(amt_tips))

# Define the cost per paper and percentage rate for the carrier's commission
# I set the cost per paper at $1 and the percentage for the carrier at 10%
cost_paper = 1.00
carrier_commission_percentage = 0.10

# calcuate total number of papers for the week
weekly_amt_papers = amt_papers * amt_days_delivered
# calculate the total cost of the papers for the week
weekly_cost = weekly_amt_papers * cost_paper
# calculate the salary of the carrier
weekly_salary = weekly_cost * carrier_commission_percentage
# caculate the total pay of the carrier for the week
weekly_pay = weekly_salary + amt_tips

# formats the outputs into floats with 2 digits after the point, like a dollar (15.00, 5.23, 1.25, etc)
format(amt_tips, '.2f')
format(weekly_salary, '.2f')
format(weekly_pay, '.2f')

# output the total number of papers delivered, weekly salary, tips for the week, and the total pay for the week
print(
    "Weekly papers delivered: " + str(weekly_amt_papers)
     + "\nWeekly salary: $" + str(weekly_salary) 
     + '\nWeekly tips: $' + str(amt_tips) 
     + '\nWeekly pay: $' + str(weekly_pay)
    )
