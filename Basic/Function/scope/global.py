#converting global to local 

x='shaik'
def myfun():
    global x
    y="Ahmad"
    print(x+y)
myfun()