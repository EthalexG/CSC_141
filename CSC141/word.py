word = 'python'

scrambled = ["_" for letter in word]
print('',join(scrambled))

while true:
    print('guess a letter.')
    guess = input ()
    guess = guess.upper()
    if guess in word:
        letter_index = word.index(guess)
        scrambled[letter_index] = guess
    else:
        print('not in word try again')
    print('',join(scrambled)) == word
        break
print(
    'game over'
)