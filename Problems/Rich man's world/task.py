initial = abs(int(input().strip()))
top = 700000
rate = 0.071
years = 0
while initial < top:
    initial *= 1 + rate
    years += 1
print(years)
