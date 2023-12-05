class Code:
    def __init__(self, codename, score):
        self.c = codename 
        self.s = score 

codes = []
for _ in range(5):
    codename, score = input().split()
    codes.append(Code(codename, int(score)))

min_idx = 0
for i in range(5):
    if codes[i].s < codes[min_idx].s:
        min_idx = i 
print(codes[min_idx].c, codes[min_idx].s)