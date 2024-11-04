# Find length of list: len(“listname”)
# Add to list: listname.append(“new item”)
# Insert at an index: listname.insert(1, “new item”)
# Remove item at index: listname.pop(1)
# Remove item: listname.remove(“second item”)
# Sort the list: listname.sort()
# Reverse the items in a list: listname.reverse()
# Make a new list object of a list that’s sorted: sorted(listname)
# Get the max value from the list: max(listname)
# Get the min value from the list: min(listname)
# Get the sum of items in list: sum(listname)

movies = ['I Am Legend', 
        'After Death', 
        'Soul', 
        'The Purge', 
        'Skinamarink', 
        'The Babysitter', 
        'The Babysitter 2'
]
movies.append('Puss In Boots: The Last Wish')
length = len(movies)

# print(f'The "movies" list includes my top {length} movies')

print(sorted(movies))

print(f'The "movies" list includes my top {length} movies')
# movies.sort()
# print(movies)