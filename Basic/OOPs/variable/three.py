class Employee:
    def __init__(self):
        avg_salary=50000

    def new_emp(self,id,name,sal):
        self.emp_id=id
        self.emp_name=name
        self.emp_sal=sal
        
    def emp_hike(self,e_hike):
        self.emp_sal=self.emp_sal+e_hike
        

e=Employee()
print(e.__dict__)

e.new_emp(101, 'sk', 25000)
print(e.__dict__)

e.emp_hike(2000)
print(e.__dict__)