## Magic behind print() function in Python.

# Python’s print() function comes with a parameter called ‘end’. And I didn't know about it till now.
# By default, the value of this parameter is ‘\n’, i.e. the new line character.
# You can end a print statement with any character/string using this parameter.

# Let's test it.
print('Avengers ')
print('Endgame')  

# Output: Avengers
#         Endgame

# Now, using end parameter.
print('Avengers',end=" ")
print('Endgame',end="")

# Output: Avengers Endgame

#------------------------------------------------------------------------------------------------

## A must-know fact about Tuples.

# When ever you want you create a tuple with just 1 element/item, you need to do the following.

tuple1 = (12,) # This is the right way to do it.

tuple2 = (12) # Not like this

# You may ask why not. Well! Let's see why.

print(type(tuple1),type(tuple2))

# Output: <class 'tuple'> <class 'int'>
# In tuple1 we used a comma to explicitly define it as a tuple, but in the tuple2 Python Intrepreter considered it to be a 'int' datatype value.

