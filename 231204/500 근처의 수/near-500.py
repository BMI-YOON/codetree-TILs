arr = list(map(int, input().split()))
small = 0
large = 1001
for elem in arr:
    if elem > small and elem < 500:
        small = elem 
    if elem < large and elem > 500:
        large = elem
print(small, large)