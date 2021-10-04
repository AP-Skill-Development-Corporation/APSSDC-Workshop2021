class Student:
    name,age = 'rajesh',26
    def marks():
        print("It is a method")
    def profile():
        return "This is Rajesh"


##print(Student.name)
##print(Student.age)
##print(Student.marks)
##print(dir(Student))
##print(type(Student.name))
##print(Student.name.__class__)
##print(Student.__dict__)
##Student.profile()
##f = Student
##print(f.name,f.age,f.profile())
##print(dir(f))
k = Student()
print(k.name)
print(k.profile())
