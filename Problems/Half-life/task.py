initial = abs(int(input().strip()))
final = abs(int(input().strip()))
half = 0
while initial >= final:
    half += 1
    initial /= 2
print(half * 12)
