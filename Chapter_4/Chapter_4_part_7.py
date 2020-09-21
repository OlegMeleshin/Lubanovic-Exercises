'''7. Use generator comprehension to return 'Got' string + quantity of numbers
in range(10). Iterate over it using For loop.'''
generator1 = (number for number in range(10))
count = 0
for number in generator1:
    count += 1
print(f"Got {count}")