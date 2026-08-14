# string 
name = "Ismail" # a string alwasys use double quotes or single quotes to define a string
print (name) # print the string

# lenth of string
print(len(name)) 

# String slicing : use to extract a portion of string.

print(name[0:3])
print(name[1:5:2])
print(name[2:])
print(name[:4])


# slicing a string with negative index
print(name[-3:])
print(name[-5:-2])


# commmon String Methods lower() and upper()


print(name.lower())
print(name.upper())


# Srip() : revove extra space 
text = " Hel lo  world "

print(len(text))
text = text.strip()

print(len(text))
print(text)

# replace() : replaces part of  a string with another string
print(text.replace("world", "python"))



# split():splits a string into a list based on a separator

friuts = "apple,banana,orange"
items = friuts.split(",")
print(friuts)
print(items)

# join(): joins elements of a list into a single string.

txt = "," .join(friuts)
print(txt)

# find(): Finds the position of a substring.

position = friuts.find("banana")
print(position)

# startswith() and endswith : checks whether a string sarts or ends with a fiven value.
email='imail@gmial.com'
print(email.startswith(email))
print(email.endswith(".com"))

# String concatenation : use for combined using the + operator

first = "hello"
second = "world"
print(first+" "+second)

# String formating: allows inserting values into string.

# using f string
age = 22 
message=f"My name is {name} and I am {age} years old"
print(message)

# checking string content : python provides methods to check stringg content.
data = "Python123"

print(data.isalpha())
print(data.isdigit())
print(data.isalnum())

# String are Immutable : Strings cannot be changed agter creation.
# data[0] = "j" it show a error




