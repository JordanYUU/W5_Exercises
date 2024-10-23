tourists = 38
days_touring = 3
van_cost = 250
van_limit = 15

import math

vans_needed = math.ceil(tourists / van_limit) 
rent_cost = van_cost * days_touring
charge_per_person = round(rent_cost / tourists + .005, 2)

print('3 vans are needed for ' + str(tourists) + ' people')
print('Rental cost is $' + str(rent_cost) + ' for 3 days')
print('Charge is $' + str(charge_per_person) + ' per person')