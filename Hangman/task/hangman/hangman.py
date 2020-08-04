# Write your code here
import random
import string

choice = ''
print('Type "play" to play the game, "exit" to quit:')
while choice not in ['play', 'quit']:
    choice = input()
    if choice == 'quit':
        quit()

random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
copy_word = chosen_word
found_letters = '-' * len(chosen_word)
in_letters = set()
print('H A N G M A N\n')
print()
mistakes = 0
# while mistakes < 8 and found_letters != chosen_word:
while found_letters != chosen_word:
    print()
    print(found_letters)
    prompt = "Input a letter: "
    in_letter = input(prompt)
    err = False
    if len(in_letter) > 1:
        print("You should input a single letter")
        err = True
    if in_letter not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        err = True
    if in_letter in in_letters:
        print("You already typed this letter")
        err = True
    else:
        in_letters.add(in_letter)

    if found_letters.count(in_letter) > 0:
        print("You already typed this letter")
        err = True

    if err:
        continue
    else:
        counter = chosen_word.count(in_letter)
        # print(f'{in_letter} was found {counter} times in {found_letters}')
        if counter > 0:
            for _ in range(counter):
                idx = copy_word.find(in_letter)

                if idx == 0:
                    copy_word = '-' + copy_word[idx + 1:len(copy_word)]
                    found_letters = in_letter + found_letters[1:len(found_letters)]

                elif idx == len(copy_word) - 1:
                    copy_word = copy_word[0:len(copy_word) - 1] + '-'
                    found_letters = found_letters[0:len(found_letters) - 1] + in_letter

                elif idx > 0:
                    copy_word = copy_word[0:idx] + '-' + copy_word[idx + 1: len(copy_word)]
                    found_letters = found_letters[0:idx] + in_letter + found_letters[idx + 1: len(found_letters)]

        else:
            print("No such letter in the word")
            mistakes += 1

    if mistakes == 8:
        break

if found_letters == chosen_word:
    print("You guessed the word!")
    print("You survived!")
else:            
    print("You are hanged!")
