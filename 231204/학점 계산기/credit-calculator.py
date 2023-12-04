n = int(input())
arr = list(map(float, input().split()))
print(f"{sum(arr)/len(arr):.1f}")
if sum(arr)/len(arr) >= 4.0:
    print("Perfect")
elif sum(arr)/len(arr) >= 3.0:
    print("Good")
else:
    print("Poor")