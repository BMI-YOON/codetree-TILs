import sys

question = list(input())
n = len(question)
max_ans = -sys.maxsize

def calculate():
    global question, n

    ans = question[0]
    for i in range(1, n, 2):
        if question[i] == '+':
            ans += question[i+1]
        elif question[i] == '-':
            ans -= question[i+1]
        else:
            ans *= question[i+1]
    return ans 

def simulate(cur_idx):
    global question, n, max_ans 

    if cur_idx == n+1:
        max_ans = max(max_ans, calculate())
        return
    
    for num in range(1, 5):
        question[cur_idx] = num 
        simulate(cur_idx+2)

simulate(0)
print(max_ans)