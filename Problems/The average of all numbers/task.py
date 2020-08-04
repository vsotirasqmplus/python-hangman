# put your python code here
small = int(input().strip())
big = int(input().strip())
total = 0
div = 0
for _ in range(small, big + 1):
    if _ % 3 == 0:
        total += _
        div += 1
print(total / div)
