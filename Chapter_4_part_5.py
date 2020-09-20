'''5. Use dictionary comprehension to create 'squares' dictionary.
Use range(10) call to get the keys and square them to get values.'''
squares = {key: key**2 for key in range(10)}
print(squares)