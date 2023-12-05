class User:
    def __init__(self, name, code, location):
        self.name = name 
        self.code = code 
        self.location = location 

n = int(input())
users = []
for _ in range(n):
    name, code, location = input().split()
    users.append(User(name, code, location))

max_idx = 0
for i in range(n):
    if users[max_idx].name < users[i].name:
        max_idx = i 
print(f"""name {users[max_idx].name}
addr {users[max_idx].code}
city {users[max_idx].location}""")