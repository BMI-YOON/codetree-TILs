class Student:
    def __init__(self, n, k, e, m):
        self.n = n
        self.k = k
        self.e = e
        self.m = m

n = int(input())
students = []
for _ in range(n):
    n, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    students.append(Student(n, k, e, m))
students.sort(key = lambda x: (-x.k, -x.e, -x.m))
for student in students:
    print(student.n, student.k, student.e, student.m)