class Number:
    def __init__(self, num, idx):
        self.num = num  
        self.idx = idx

n = int(input())
arr = list(map(int, input().split()))
numbers = []
for i in range(n):
    numbers.append(Number(arr[i], i))
numbers.sort(key = lambda x: x.num)
ans = [0] * n 
for i, number in enumerate(numbers, start = 1):
    ans[number.idx] = i
for elem in ans:
    print(elem, end = ' ')