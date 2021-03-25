from student import Student

from teacher import Teacher

t1 = Teacher()
t1.name = "Farah"
t1.set_email()
print(t1.get_email())

s1 = Student()
s1.name = "farrah"
s1.set_email()
print(s1.get_email())