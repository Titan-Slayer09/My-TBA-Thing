import time

def typing_print(text, delay=0.03, end=''):
    for letter in text:
        print(letter, end=end, flush=True)
        time.sleep(delay)

def game_intro():
    typing_print("MESSAGE FROM CREATOR: PLEASE ONLY TYPE THINGS WHEN YOU ARE ASKED TO, OR WHEN THE CURSOR AUTO-MOVES TO THE TYPE POSITION, OR THE STORY WILL MESS UP.\n")

def get_player_info():
    name = input("system: what is your name? ")
    age = input("system: how old are you? ")
    gender = input("system: are you a, boy, or girl, or other? ")
    if gender == "boy":
        Pronoun = "he"
    elif gender == "girl":
        Pronoun = "she"
    elif gender == "other":
        Pronoun = "they/them"
    else:
        typing_print("pick an option please")
        exit()
    return name, age, gender, Pronoun

def game_start(name, gender, Pronoun):
    typing_print("MESSAGE FROM CREATOR: ocassionally words double space, due to you placing a space before the word when you type it, please ignore. also eventually in the story, glitches may happen. please tell creator to fix.")
    typing_print(" ")
    typing_print(" ")

    Continue= input("\n system: Begin story? y/n ")
    typing_print(" ")

    if Continue == "y" or "yes":
        typing_print("Story Starting... ")
        time.sleep(3)
        hello = input(f"\n computer: Hello {name} ")
        typing_print(" ")
    elif Continue == "n" or "no":
        typing_print("Ending 1: don't want to play.")
        exit()
    else:
        typing_print("system: You're lucky you messed up so early, your options here are to input y or n no capital letters, or spaces this is your warning, this story is very unforgining to people who misspell their options or answers so if you need to copy and paste the option.")

def game_play(name, Pronoun):
    typing_print("You look around you for the first time, and notice you are floating, in blackness, all you can see is black. occasionally words appear in front of you. you are in a console, one of many, in which your world is controlled by your actions.")
    typing_print(" ")
    typing_print(" ")

    GAME = input(f"\n computer: now {name}, do you want to play a game? y/n ")
    if GAME == "n":
        computer_opinion1 = -1
        #opinion system?
        typing_print(" ")
        typing_print("computer: ...")
        time.sleep(1)
        typing_print(" ")
    if GAME == "y":
        typing_print(f"computer: HA don't care, entertain yourself, plus we have more important things to do. ")
        typing_print(" ")
    else:
        typing_print(" ")
        typing_print("please select a given option.")
        typing_print("Ending 0, the failure, answer a question properly.")
        time.sleep(5)
        game_over()
        
def game_over():
    exit()

def meaning_of_life(name):
    time.sleep(5)
    typing_print(" ")
    typing_print(f"\n computer: so {name} what is the meaning of life?")
    time.sleep(2)
    life = input(f" system: {name} what do you think? #this should be a verb# ")
    time.sleep(2)
    typing_print(" ")
    typing_print(f"computer: ahh you think it is {life}")
    time.sleep(2)
    typing_print(" ")
    typing_print(f"computer: your opinion is valid {name}.")
    time.sleep(2)
    typing_print(" ")
    typing_print(f"computer: updating databanks to add the definition {life} as the meaning of life.")

def main():
    game_intro()
    name, age, gender, Pronoun = get_player_info()
    game_start(name, gender, Pronoun)
    game_play(name, Pronoun)
    meaning_of_life(name)

main()