cash = 523.23
personal_property = 897.51
real_estate = 0
investments = 0

assets = (cash + personal_property + investments + real_estate)

mortgages = 0
car_lones = 0
student_loans = 0
credit_card_debt = 0
other_debt = 0

liabilities = (mortgages + car_lones + student_loans + credit_card_debt + other_debt)

networth = (assets - liabilities)

print("Your networth is $" + str(networth))