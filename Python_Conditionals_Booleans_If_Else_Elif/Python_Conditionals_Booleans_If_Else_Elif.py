# Notes from Corey Schafer's Python Course
# https://www.youtube.com/c/Coreyms

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

from itertools import filterfalse


if True:
    print("Conditional was True")

# Output
# Conditional was True

if False:
    print("Conditional was False")

# Output was blank

language = 'Python'

if language == 'Python':
    print("Set to True")

# Output
#Set to True

language = 'Python'

if language == 'Python':
    print("Set to Python")
else:
    print('no match')

# Output
# Set to Python

language = 'Java'

if language == 'Python':
    print("Set to Python")
else:
    print('no match')

# Output
# no match

language = 'Ruby'

if language == 'Python':
    print("Set to Python")
elif language == 'Java':
    print("Set to Java")
else:
    print("no match")

#Python Test Output
# Set to Python

# Java Test Output
# Set to Java

# Ruby Test Output
# no match

# Bools
# and
# or 
# not

user = "Admin"
logged_in = True

if user == "Admin" and logged_in == True:
    print("Admin Page")
else:
    print("Bad Creds")

#Output
# Admin Page


user = "Admin"
logged_in = False

if user == "Admin" or logged_in == True:
    print("Admin Page")
else:
    print("Bad Creds")

#Output (uses 'or' vs 'and')
# Admin Page


# 'Not' is used to reverse bool, Not false or not true...if not false. 
user = "Admin"
logged_in = False 

if not logged_in:
    print ("Not logged in")
else:
    print ("Logged in")

# Output
# Not logged in

# Object id
# checks to see if two objects are in the same location in memeory.  

a = [1, 2, 3]
b = [1, 2, 3]

print (id (a))
print (id (b))
print(a is b)
# output
# 1406400154496
# 1406376311616
# False...two diffrent locations. Checking IDs

a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)
# Output
# 1458897342208
# 1458897342208
# True

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


condition = False 

if condition:
    print('Eval to True')
else:
    print('Eval to False')

# output
# Eval to False

condition = None 

if condition:
    print('Eval to True')
else:
    print('Eval to False')

# output
# Eval to False

# if set to zero will eval to false, any other setting will eval to true.
condition = 0 

if condition:
    print('Eval to True')
else:
    print('Eval to False')

# output
# Eval to False

# empty list, string, tuple...will eval to false, any other setting will eval to true.
condition = []

if condition:
    print('Eval to True')
else:
    print('Eval to False')

# output
# Eval to False

# empty mapping (dictionary)...will eval to false, any other setting will eval to true.
condition = {}

if condition:
    print('Eval to True')
else:
    print('Eval to False')

# output
# Eval to False

# Non Empty string...will eval to true.
condition = "Test"

if condition:
    print('Eval to True')
else:
    print('Eval to False')

# output
# Eval to True