class Forecast:
    def __init__(self, date, day, weather):
        self.date = date 
        self.day = day
        self.weather = weather 

n = int(input())
arr = []
for _ in range(n):
    date, day, weather = input().split()
    if weather == 'Rain':
        arr.append(Forecast(date, day, weather))

min_idx = 0
for i in range(len(arr)):
    if arr[min_idx].date > arr[i].date:
        min_idx = i 
print(arr[min_idx].date, arr[min_idx].day, arr[min_idx].weather)