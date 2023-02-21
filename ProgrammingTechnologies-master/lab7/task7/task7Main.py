import datetime

from StudentGroup import StudentGroup
from Student import Student

student1: Student = Student("Pupkin Vasiliy G", datetime.date(2021, 9, 1))
student2: Student = Student("Barbolin Semyon P", datetime.date(2021, 9, 2))
student3: Student = Student("Nikto Nikto N", datetime.date(2021, 8, 2))

group: StudentGroup = StudentGroup(1, 3)

print(group.add_student(student1))
print(group.add_student(student2))
print(group.add_student(student3))

print()
group.print_students_()

print()
print(group.remove_student("Barbolin Semyon P"))
group.print_students_()
