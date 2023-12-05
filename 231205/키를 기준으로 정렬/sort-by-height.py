class User:
    def __init__(self, name, height, weight):
        self.name = name 
        self.height = height 
        self.weight = weight 

n = int(input())
users = []
for _ in range(n):
    name, height, weight = input().split()
    users.append(User(name, height, weight))
users.sort(key = lambda x: x.height)
for user in users:
    print(user.name, user.height, user.weight)