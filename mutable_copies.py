# a = [3, 5, 2, 21]

# b =  a

# b[1]= 666

# print(a)

a = [3, 5, 2, 21]

b =  a.copy()

b[1]= 666

print(a)
# after creating a copy of a and assigning
# it to b, we can change b without affecting a.