'''10. Define 'test' decorator which prints 'start' when the function is called
and 'end' when the function completes its work.'''
def test(func):
    
    def wrapper():
        print("Start")
        func() 
        print("End")
    
    return wrapper



def stand_alone_function():
    print("main func")

stand_alone_function_decorated = test(stand_alone_function)
stand_alone_function_decorated()