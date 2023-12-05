class Student:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

students = []
for _ in range(5):
    n, h, w = input().split()
    students.append(Student(n, int(h), float(w)))

print("name")
students.sort(key = lambda x: x.n)
for student in students:
    print(student.n, student.h, student.w)
print()
print("height")
students.sort(key = lambda x: -x.h)
for student in students:
    print(student.n, student.h, student.w)