count_arr = [0] * 4
for _ in range(3):
    arr = input().split()
    symptom = arr[0]
    temperature = int(arr[1])
    if symptom == 'Y' and temperature >= 37:
        count_arr[0] += 1
    elif symptom == 'N' and temperature >= 37:
        count_arr[1] += 1
    elif symptom == 'Y' and temperature < 37:
        count_arr[2] += 1
    else:
        count_arr[3] += 1
for i in range(4):
    print(count_arr[i], end = ' ')
if count_arr[0] >= 2:
    print('E')