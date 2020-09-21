'''6. Use Set comprehension to create the 'odd' set containing even numbers in range(10).
Так и написано ODD, в котором ЧЕТНЫЕ числа. Опечатка возможно.'''
odd = {even for even in range(10) if even % 2 == 0}
print(odd)
