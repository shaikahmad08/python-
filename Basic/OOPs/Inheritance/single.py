#type of inheritance 
#1--single inheritance

class parents:
    def p1(self):
        print("This is the parent class")

class child(parents):
    def child1(self):
        print("This is the child class")

obj=child()
obj.p1()
obj.child1()