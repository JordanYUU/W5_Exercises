tourists = 38
days_touring = 3
van_cost = 250
van_limit = 15

vans_needed = round(tourists / van_limit + .5) 
rent_cost = van_cost * days_touring
charge_per_person = round(rent_cost / tourists + .005, 2)

print(vans_needed, rent_cost, charge_per_person)