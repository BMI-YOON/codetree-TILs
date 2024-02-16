import sys

question = list(input())
alphabet = list()
new_question = list()
n = len(question)
max_ans = -sys.maxsize

def calculate():
    global new_question, n

    ans = new_question[0]
    for i in range(1, n, 2):
        if new_question[i] == '+':
            ans += new_question[i+1]
        elif new_question[i] == '-':
            ans -= new_question[i+1]
        else:
            ans *= new_question[i+1]
    return ans 

def simulate(cur_idx):
    global question, alphabet, new_question, n, max_ans 

    if cur_idx == 6:
        new_question = list()
        for i in range(n):
            if question[i] == '*' or question[i] == '+' or question[i] == '-':
                new_question.append(question[i])
            else:
                new_question.append(alphabet[ord(question[i]) - 97])
        max_ans = max(max_ans, calculate())
        return
    
    for num in range(1, 5):
        alphabet.append(num) 
        simulate(cur_idx+1)
        alphabet.pop()

simulate(0)
print(max_ans)