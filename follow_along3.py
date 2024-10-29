# Pet store calculator

# Difine the unknown
num_cats = int(input('How many cats need feeding?'))
cat_food = {'fromm': int(input('How much fromm do we have?')), 
            'purina': int(input('How much purina do we have?')), 
            'kirkland': int(input('How much kirkland do we have?'))
            }
cat_serving = 0.10
cats_fed = num_cats * cat_serving

print(f'Number of cats: {num_cats}')
print(f'Cat food in stock: {cat_food}')

# Calculate the unknown

if cat_food['kirkland'] > 0:
    cat_food['kirkland'] = cat_food['kirkland'] - (num_cats * cat_serving)
elif cat_food['fromm'] > 0:
    cat_food['fromm'] = cat_food['fromm'] - (num_cats * cat_serving)
elif cat_food['purina'] > 0:
    cat_food['purina'] = cat_food['purina'] - (num_cats * cat_serving)
print(f'After feeding the cats: {cat_food})')