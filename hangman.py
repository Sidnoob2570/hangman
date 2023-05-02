import random
from art import logo, stages
from word_pool import words

print(logo)
print("You have 6 chances to save yourself")
chosen_word = random.choice(words)
display = []
for _ in range(len(chosen_word)):
    display += '_'
print(display)
lives = 6
flag = 0
while (flag == 0):
    guess = input('Enter the letter ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter    
    if guess not in chosen_word:
        lives -=1
        print(f"Lives left = {lives}")
        if lives == 0:
            print("You Lose")
            break
    print(display)

    if "_" not in display:
        flag == 1
        print("Clutch game")
        break
    
    print(stages[lives])
