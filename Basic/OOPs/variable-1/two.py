class Marks:
    pass_marks=40
    extra_marks=10

    def __init__(self,roll_no,name,mark,subject):
        self.stu_roll_no=roll_no
        self.stu_name=name
        self.stu_mark=mark
        self.sub=subject
        
    def marks(self):
        if self.stu_mark<=40:
            print('student must pass exam')
        else:
            print('student had pass with 70%')        
        
    def total_marks(self):
        self.total_mark=self.stu_mark+Marks.extra_marks
        print(f'Total marks after adding extra marks: {self.total_mark}')

    @classmethod
    def student1(cls):
        pass

    @staticmethod
    def student2(cls):
        pass


m1=Marks(1,'baasha',72,'maths')
m2=Marks(11,'sk',39,'phy')
m3=Marks(21,'vasmi',35,'chem')

print(m1.__dict__)
m1.marks()

print(m2.__dict__)
m2.marks()

print(m3.__dict__)
m3.marks()

m1.total_marks()
print(m1.__dict__)