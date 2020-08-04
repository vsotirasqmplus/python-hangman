word = input()
pal = True
w_len = len(word)
idx = 0
while idx < w_len / 2:
    pal = pal and word[idx] == word[-idx - 1]
    idx += 1
print("Palindrome" if pal else "Not palindrome")
