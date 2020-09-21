'''11. Define the exception called 'OopsException'. Generate it to see what happens.
Then write a code to catch this exception and print the string 'Caught an oops'.'''
class OopsExeption(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise OopsExeption("Caught an oops")
        