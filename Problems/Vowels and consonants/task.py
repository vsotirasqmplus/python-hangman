import string
text = input()
vowels = 'aeiou'
for letter in text:
    if letter.lower() in vowels:
        print("vowel")
    elif letter.lower() in string.ascii_lowercase:
        print("consonant")
    else:
        break
