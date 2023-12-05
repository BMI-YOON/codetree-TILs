class Student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n

N = int(input())
students = []
for i in range(1, N + 1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, i))
students.sort(key = lambda x: (x.h, -x.w))
for student in students:
    print(student.h, student.w, student.n)