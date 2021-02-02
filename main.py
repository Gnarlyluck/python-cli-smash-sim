import smash 
import random
import json
import time
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def play_game():
    for index, element in enumerate(characters):
        print(index, element['name'])
    character_select = input('Choose your combatants. Please select by number: \n')
    if character_select.isnumeric() == False:
        user_choice = smash.Character(random.choice(characters))
        print(f"Invalid input we have chosen your character for you! \n ")
        time.sleep(4)
    elif 0 <= int(character_select) <= len(characters):
        user_choice = smash.Character(characters[int(character_select)])
    else:
        print(f"Invalid input we have chosen your character for you!\n ")
        user_choice = smash.Character(random.choice(characters))
        time.sleep(4)
    a_i_choice = smash.Character(random.choice(characters))
    
    print(f'"You have selected " {user_choice.name}\n')
    print(f'"AI has selected " {a_i_choice.name}\n')
    time.sleep(3)

    smash.Battle(user_choice, a_i_choice)
    play_again = input('Would you like to play again? Y/N? \n')
    if play_again == str('y' or 'Y'):
       play_game() 
    else:
        print('See you next time')
play_game()