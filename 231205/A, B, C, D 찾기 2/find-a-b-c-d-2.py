arr = list(map(int, input().split()))

def f(arr1, arr2):
    if sorted(arr1) == sorted(arr2):
        return True
    else:
        return False

for i in range(1, 41):
    for j in range(i, 41):
        for k in range(j, 41):
            for l in range(k, 41):
                new_arr = [i, j, k, l, i+j, i+k, i+l, j+k, j+l, k+l, i+j+k, i+j+l, i+k+l, j+k+l, i+j+k+l]
                if f(arr, new_arr):
                    print(i, j, k, l)