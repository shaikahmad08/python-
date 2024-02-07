#  2--multiple inheritance
class Father:
    def father(self):
        print("This is father class")

class Mother:
    def mother(self):
        print("This is mother class")

class Child(Father,Mother):
    def child(self):
        print("This is child class")

obj=Child()
obj.father()
obj.mother()



