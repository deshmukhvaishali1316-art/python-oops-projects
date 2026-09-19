class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

# 3 students
s1 = Student("Amit", 85)
s2 = Student("Rahul", 35)

print(s1.name, "-", s1.result())
print(s2.name, "-", s2.result())