class Employee:
    def __init__(self):
        emp_sal=45000
        
    def junior_emp(self,id,name,sal):
        self.emp_id=id
        self.emp_name=name
        self.emp_sal=sal

    def senior_emp(self):
        pass

e1=Employee()
print(e1.__dict__)
        

e1.junior_emp(101, 'sk', 25000)
print(e1.__dict__)