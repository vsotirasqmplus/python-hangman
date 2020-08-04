n = int(input().strip())
sq = list()
for _ in range(n):
    q = int(input().strip())
    q = q * q
    if q % 7 == 0:
        sq.append(q)
for q in sq:
    print(q)
