'''9. Define the generator function 'get_odds' returning even numbers in range(10).
Use For loop to find and print the third returned value. Опять ODDS и опять четные.'''
def get_odds(r):
    count = 0
    
    for z in range(r):
        if z % 2 != 0:
            continue
        else:
            count += 1
           
        yield z

x = get_odds(10)        
evens = []
for y in x:
    evens.append(y)
    print(y)
print(f"\n{evens[2]}")
