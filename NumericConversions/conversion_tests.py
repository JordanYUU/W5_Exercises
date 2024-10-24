# Description: A script for testing 
#              numeric conversion tech
# Author: Jordan AC

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# print(a, type(a)
# SyntaxError: '(' was never closed

a_int = int(float(a))
b_float = float(b)

print(a_int, type(a_int))

print(b_float, type(b_float))

a_stripped = a.strip
print(a.strip())

d_stripped = d.strip()
d_sliced = d_stripped[7:]
print(d_sliced) 

# You can't from the output that the space at the end
# was removed. Just trust that it was though.

# I was kinda confused on what this question
# asked of me but I tried w