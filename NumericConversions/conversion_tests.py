# Description: A script for testing 
#              numeric conversion tech
# Author: Jordan AC

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# print(int(float(a)), type(a))

a2 = int(float(a))
b2 = float(b)

print(a2, type(a2))

print(b2, type(b2))

a_stripped = a.strip
print(a.strip())

d_stripped = d.strip()
d_sliced = d_stripped[7:]
print(d_sliced) 

# You can't from the output that the space at the end
# was removed. Just trust that it was though.

# I was kinda confused on what this question
# asked of me but I tried