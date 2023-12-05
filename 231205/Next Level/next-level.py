class Account:
    def __init__(self, id = 'codetree', level = '10'):
        self.i = id 
        self.l = level 

account1 = Account()
id, level = input().split()
account2 = Account(id, level)

print(f"user {account1.i} lv {account1.l}")
print(f"user {account2.i} lv {account2.l}")