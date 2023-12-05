class Student:
    def __init__(self, n, a, b, c):
        self.n = n
        self.a = a
        self.b = b
        self.c = c 

n = int(input())
students = []
for _ in range(n):
    n, a, b, c = input().split()
    students.append(Student(n, int(a), int(b), int(c)))
students.sort(key = lambda x: x.a + x.b + x.c)
for student in students:
    print(student.n, student.a, student.b, student.c)