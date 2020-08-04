# put your python code here
total = 0
square = 0
while True:  # total != 0:
    n = int(input())
    square += n ** 2
    total += n
    if total == 0:
        break
print(square)
