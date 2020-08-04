punct = list(',.!?')
text = list(input().lower())
for p in punct:
    while p in text:
        text.remove(p)
print(''.join(text))
