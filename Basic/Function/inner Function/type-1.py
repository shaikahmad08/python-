def outer():
    print("hello")
    
    def inner():
        print("hii")
    inner()
outer()