import pyttsx3
import random

engine = pyttsx3.init()  # object creation

options = ['rock', 'paper', 'scissors']

# RATE
rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 125)  # setting up new voice rate

# VOLUME
volume = engine.getProperty("volume")  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty("voice", voices[0].id)  # changing index, changes voices. 1 for female


while True:

    user_option = input('Rock, Paper , Scissors Which one Will you chose?: ').strip().lower()

    if user_option in ['leave', 'q']:
        engine.say('See you next time!')
        engine.runAndWait()
        break

    if user_option not in options:
        engine.say('Unusuable option')
        engine.runAndWait()
        break


    computer_option = random.choice(options)

    print(f'Your Choice: {user_option}')
    print(f'Computer Choice: {computer_option}')

    engine.say('Computer choice' + computer_option)
    engine.runAndWait()


    if user_option == computer_option:
        winner = engine.say('Draw')

    elif (
        (user_option == "rock" and computer_option == "scissors") or
        (user_option == "paper" and computer_option == "rock") or
        (user_option == "scissors" and computer_option == "paper")
    ):
        winner = 'Player Has won'
    else:
        winner = 'Computer Has won'

    print(f"Winner: {winner}\n")

    engine.say(winner)
    engine.runAndWait()

engine.stop()