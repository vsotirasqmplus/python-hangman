low = input()
output = ''
for letter in low:
    if letter == letter.upper():
        output += '_' + letter.lower()
    else:
        output += letter
print(output)
