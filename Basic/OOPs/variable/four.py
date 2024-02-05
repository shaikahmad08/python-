class Employee:
    def __init__(self):
        self.emp_id_list = []
        self.emp_name_list = []
        self.emp_sal_list = []
        self.avg_sal = 75000

    def old_emp(self, emp_id, emp_name, emp_sal):
        self.emp_id_list.append(emp_id)
        self.emp_name_list.append(emp_name)
        self.emp_sal_list.append(emp_sal)

    def hike(self, salary):
        self.avg_sal = sum(self.emp_sal_list) / len(self.emp_sal_list)
        for i in range(len(self.emp_sal_list)):
            self.emp_sal_list[i] += salary

e1 = Employee()
print(e1.__dict__)

e1.old_emp(101, 'sk', 25000)
e1.old_emp(102, 'john', 35000)
e1.old_emp(103, 'alice', 45000)
e1.old_emp(104, 'bob', 55000)
print(e1.__dict__)

e1.hike(2000)
print(e1.__dict__)
