n, m = tuple(map(int, input().split()))
arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr_3 = [
    [1 if arr_1[i][j] != arr_2[i][j] else 0 for j in range(m)]
    for i in range(n)
]
for row in arr_3:
	for elem in row:
		print(elem, end=" ")
	print()