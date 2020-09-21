'''2. Assign value 7 to the variable 'guess_me', and value 1 to variable 
'start'. Make a 'while' statement which compares variables 'start' and 'guess_me'.
Print 'too low' if 'start' is lesser than 'guess_me'. If they`re equal print 
'found it!'and quit the loop.If 'start' is bigger than 'guess_me' print 'oops' 
and quit the loop. Increase the value of the 'start' at the end of the loop.'''
start = 1
guess_me = 7
while start:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it!")
        break
    elif start > guess_me:
        print("oops")
        break
    start += 1  