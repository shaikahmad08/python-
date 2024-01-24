def outer():
    print("hello")
    
    def inner():
        print( "hii")
    return inner
x=outer()
x()