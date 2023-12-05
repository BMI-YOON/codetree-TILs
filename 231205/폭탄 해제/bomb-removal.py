class Bomb:
    def __init__(self, code, color, second):
        self.code = code 
        self.color = color 
        self.second = second 

code, color, second = input().split()
bomb = Bomb(code, color, second)
print(f"""code : {bomb.code}
color : {bomb.color}
second : {bomb.second}""")