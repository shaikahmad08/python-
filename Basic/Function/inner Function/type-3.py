def outer():
    print("hello")
    def inner():
        return "hii"
    return inner()
x=outer()
print(x)
    
