class Student:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

n = int(input())
students = []
for _ in range(n):
    n, h, w = input().split()
    students.append(Student(n, int(h), int(w)))
students.sort(key = lambda x: (x.h, -x.w))
for student in students:
    print(student.n, student.h, student.w)