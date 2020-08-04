cafe = ''
max_c = 0
choice = ' '
while choice != 'MEOW':
    cafe = input().split()
    if cafe[0] == 'MEOW':
        break
    if int(cafe[1]) > max_c:
        choice = cafe[0]
        max_c = int(cafe[1])
print(choice)
