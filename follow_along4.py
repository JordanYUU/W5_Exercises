# Types of iterables:
str_1 = 'string'
list = [1,2,3,4]
tuple = ('allspice', 'bay', 'cinnamon', 'dandelion')
range_5 = range(1,7,1)
# range consistst of opporator(start, end, step)
dict1 = {'1':'allspice', '2':'bay', '3':'cinnamon', '4':'dandelion'}

balance = 150
print(f'Starting balance is ${balance}.')

while balance > 50:
    print('Treat yoself!')
    balance -= 25
    print('$'+str(balance))
    if balance == 75:
        break
# Break only ends the loop if the exact conditions are met
# if balance > 70 and balance < 75:

print(f'Your final balance is ${balance}.')


# counter = 0
# spices = []

# while loop
# while counter == 0:
#     for i in  tuple:
#         if i == 'bay' or i == 'dandelion':
#             print('That\'s  a leaf')
#         else:
#             counter += 1
#             spices.append(i)
#             print(f'{i.capitalize()} is a spice')

# print(f'Item {counter} is the first spice in the cabinet')



# for loop
# for i in tuple:
#     counter+= 1
#     if i == 'bay' or i == 'dandelion':
#         print('Bay is a leaf')
#     else:
#         spices.append(i)
#         print(f'{i.capitalize()} is a spice')

# print(f'We have {counter} items in our spice cabinet')
# print(f'{spices} are spices')