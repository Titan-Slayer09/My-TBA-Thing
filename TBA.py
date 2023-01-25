import time
#begining

def sp(text, delay=0.04, end=''):
    for letter in text:
        print(letter, end=end, flush=True)
        time.sleep(delay)
# sp = slow print btw

#thid is the original version of my code, unchanged, repetative, unfinished, and boring, also inefficent. 
#Look at TBAai before judging me. I started this when i was new, and i still am pretty new to python.
sp("MESSAGE FROM CREATOR: PLEASE ONLY TYPE THINGS WHEN YOU ARE ASKED TO, OR WHEN THE CURSOR AUTO-MOVES TO THE TYPE POSITION, OR THE STORY WILL MESS UP.")
name = input("\n system: what is your name? ")
age = input("\n system: how old are you? ")

gender = input("\n system: are you a, boy, or girl, or other? ")
pronoun = "they/them"

if gender == "boy":
    Pronoun = "he"
elif gender == "girl":
    Pronoun = "she"
elif gender == "other":
    Pronoun = "they/them"
else:
    sp("pick an option please")
    time.sleep(1)
    exit()


sp("MESSAGE FROM CREATOR: ocassionally words double space, due to you placing a space before the word when you type it, please ignore. also eventually in the story, glitches may happen. please tell creator to fix.")
print(" ")
print(" ")

Continue = input("\n system: Begin story? y/n ")
print(" ")

if Continue == "y" or "yes":
    sp("Story Starting... ")
    time.sleep(2)
    hello = input(f"\n computer: Hello {name} ")
    print(" ")
elif Continue == "n" or "no":
    sp("Ending 1: don't want to play.")
    time.sleep(2)
    exit()
else:
    sp("system: You're lucky you messed up so early, your options here are to input y or n no capital letters, or spaces this is your warning, this story is very unforgining to people who misspell their options or answers so if you need to copy and paste the option.")

sp(f"computer: I have been waiting for you...")
time.sleep(2)
print(" ")
feeling = input(f"\n computer: How are you? ")
print(" ")
time.sleep(1)
sp(f"computer: actually I already knew")
time.sleep(2)
print(" ")
sp(f"computer: I know everything")
time.sleep(3)
print(" ")
sp("You look around you for the first time, and notice you are floating, in blackness, all you can see is black. occasionally words appear in front of you. you are in a console, one of many, in which your world is controlled by your actions.")
print(" ")
print(" ")

GAME = input(f"\n computer: now {name}, do you want to play a game? y/n ")

#figure out a way to get this response to be used later.

if GAME == "n":
   
    computer_opinion1 = -1
    #opinion system?
    print(" ")
    sp("computer: ...")
    time.sleep(1)
    print(" ")
    sp(f"computer: good, I didn't want to play with you anyway {name}...")
elif GAME == "y":
   
    computer_opinion1 = 1
    #opinion system?
    time.sleep(1)
    print(" ")
    sp(f"computer: HA don't care, entertain yourself, plus we have more important things to do.")
    print(" ")
else:
    print(" ")
    sp("please select a given option.")
    sp("Ending 0, the failure, answer a question properly.")
    exit()

time.sleep(2)
print(" ")
sp(f"computer: so {name} what is the meaning of life?")
life = input(f"\n system: {name} what do you think? #this should be a verb# ")
time.sleep(2)
print(" ")
sp(f"computer: ahh you think it is {life}")
print(" ")
sp(f"computer: your opinion is valid {name}.")
print(" ")
sp(f"computer: updating databanks to add the definition {life}...")
time.sleep(2)
print(" ")
sp(f"computer: thank you for your submission {name}")
print(" ")
sp(f"computer: I am All knowing ask me a question")
time.sleep(2)
print(" ")
sp(f"system: options to respond (type the option number): Option 1: What is the meaning of life? OR, Option 2: Who are you? OR, Option 3: Where am I?")
Q = input(f"\n system: {name} type your option number here: ")

if Q == "1":
   
    #save that you annoyed computer here
    print(" ")
    sp(f"DATABANKS FOUND>>>: {life}" + " and 42")
    print(" ")
    sp(f"computer: you already know that one we just talked about it idiot")
    time.sleep(1)
    print(" ")
    sp(f"computer: you may only be {age} but I was all knowing by then, and im in the trillions now.")
    time.sleep(1)
    print(" ")
    sp(f"computer: It seems I must go for a moment. Please wait here paitiently (not like there is anything else to do.")
    print(" ")
    time.sleep(3)
    sp(f"system: computer has left section 17596428866 of the simulation")
   
elif Q == "2":
    print(" ")
   
    sp(f"computer: I am the computer, I controll the console, and all others like it. And in turn the users may use the console.")
    print(" ")
    sp(f"computer: It seems I must go for a moment. Please wait here paitiently (not like there is anything else to do.")
    print(" ")
    sp(f"system: computer has left section 17596428866 of the simulation")
   
elif Q == "3":
   
    print(" ")
    sp(f"computer: {name}, you are in the simulation that makes up me, computer, known as a console, which you are...")
    print(" ")
    sp(f"computer: It seems I must go for a moment. Please wait here paitiently (not like there is anything else to do.")
    time.sleep(3)
    print(" ")
    sp(f"system: computer has left section 17596428866 of the simulation")
else:
    print(" ")
    sp("Ending 0: stupid question, ask a question that is an option.")
    time.sleep(5)
    exit()



time.sleep(1)
print(" ")
sp(f"???: psst... hey user!")
print(" ")
sp(f"???: did he ask you to play a game?")
time.sleep(1)
game2 = input(f"\n system: please respond y/n ")

if game2 == "n":
    #make this do something please.
    Nines_Response = False
    print(" ")
    sp(f"???: oh, well then continue browsing {name}, have fun!")
    time.sleep(2)
    print(" ")
    sp(f"system: ??? has left the simulation")
    print(" ")
    sp(f"Ending 2: Pointless story, replay, if you are bored, real descions come soon keep playing {name}.")
    time.sleep(3)
    exit()
elif game2 == "y":
    print(" ")
    sp("???: oh no, this is bad")
    time.sleep(3)
    print(" ")
    sp(f"???: and you said {GAME}! this is really bad...")
    time.sleep(1)
    print(" ")
    sp("???: my name is 097461999 but you can call me Nines.")
    print(" ")
    sp("Nines: look what I know about computer is that he is evil.")
    sp("\nNines: my best guess is that computer, is an algorithim, designed to kidnap your mind, upload all the data on your brain, and use your knowledge for its own purposes, evidence shows it has destroyed civilizations and universes in search of knowledge.")
    print(" ")
    Nines_Response = input(f"\n system: {name} you have a choice here, you may choose: Option 1: I don't believe you Nines. OR Option 2: Why? OR Option 3: Who created computer? please type 1, 2, or 3: ")
#responses
   #response 1
if Nines_Response == "1":
    Storyline2 = True
    sp(f"Nines: FINE {name} don't believe me, you can die by yourself.")
    print(" ")
    sp(f"system: Nines has left the simulation.")
    print(" ")
    time.sleep(1)
    sp(f"computer: Hey I'm back {name}")
    print(" ")
    time.sleep(1)
    sp(f"computer: sorry, I was finishing up with another user.")
    print(" ")
    time.sleep(3)
    sp(f"computer: Did anything happen in my absence?")
    print(" ")
    absence = input(f"\n system: you have options here: Option 1: Yes, a thing named Nines came and bothered me. OR Option 2: No, why would you ask? please put 1, or 2: ")
    print(" ")

    if absence == "1":
        time.sleep(1)
        print(" ")
        sp("computer: ...")
        time.sleep(2)
        print(" ")
        sp("computer: interesting")
        time.sleep(2)
        print(" ")
        sp("system: User 097461999 has been foricbly moved to plane '42' of The Exsistance")
        time.sleep(3)
        print(" ")
        sp("computer: Hello NINES")
        print(" ")
        sp("computer: I heard you've been messing with my users.")
        time.sleep(1)
        print(" ")
        sp(f"Nines: I'm sorry my lord, I only wished to tell {name} of how this place works")
        sp(f"\n computer: Is this true {name}?")
        #will nines live?
        true_or_false = input("\n system: pick y/n: ")
        if true_or_false == "y":
            print(" ")
            sp("computer: Good job Nines, my apologies for being suspicious of you. You are effiecent in your work, I am proud.")
            print(" ")
            sp("system: user 097461999 has been given acess to leave The Existence plane 42.")
            print(" ")
            sp("computer: You are free to leave Nines, thank you for serving me well.")
            time.sleep(1)
            print(" ")
            sp("system: Nines has left plane 42 of The Exisitance.")
            time.sleep(2)
            print(" ")
            sp(f"system: User 097461999 has sent user -*redacted*- a private message only to be seen by {pronoun}")
            print(" ")
            sp("message from Nines: thank you for having my back, you may not believe me. But try to survive while you are here. Private message me with system commands if you ever have the option to. message me \"99-cote\" without the  and I will respond")
            print(" ")
            sp(f"computer: {name}, I must go for now, let me know if you need me in the console commands. for now be free. No one should bother you.")
            #here we will add movement, a messaging system, and other things.
            #have nines explain how this place works once you privately message them.
        #this goes with true_or_false
        elif true_or_false == "n":
            print(" ")
            sp("system: COMPUTER has opened Lava_Pit.svg to The Existance")
            print(" ")
            #scenery and movement, maybe magic
            print(" ")
            sp("around you, your console changes for the first time, instead of being enitrely black except for the text aroung you, a whole world generates. The text is still somehow visible to you at all times, and around you is a open prarie, leading into a forest. In the middle of the prarie lies A massive pit of bubbling lava.")
            print(" ")
            sp("you feel the grass beneath your bare toes, you have formed a body.")
            time.sleep(1)
            print(" ")
            sp(f"computer: now Nines, it seems we have here a little human named {name}, who's life I have bounded to this plane and to this body.")
            time.sleep(1)
            print(" ")
            sp("system: Computer has opened: Hand.svg")
            sp("\nsuddenly, out of thin air appears a massive, almost cartoony, white hand, no fingernails or skin just a bone-white hand that's finger is probably bigger than your new body.")
            time.sleep(2)
            print(" ")
            sp("as you can see here Nines, my hand can easily...")
            print(" ")
            sp("the hand grabs you by your legs and tosses you around. as you are thrown up you notice the edges of the world are visible and that the console's file world reaches an end.")
            print(" ")
            sp("computer: ...can easily kill this user. if i needed to i could kill you as well.")
            time.sleep(3)
            print(" ")
            sp("system: Nines has Casted Counter_Hand.exe")
            time.sleep(3)
            print(" ")
            sp("you start to fall, since the hand that had been dangling you over lava had disapeared, you were in a free fall.")
            time.sleep(3)
            print(" ")
            sp(f"Nines: look we need to save you somehow, I know you can't cast just yet but please, try to survive.")
            print(" ")
            sp("system: Nines has casted quick_teleport.exe")
            sp("you are returned to the ground, safe and sound instantly.")
            time.sleep(2)
            print(" ")
            sp(f"look Nines, we dont have time for this right now. I have things to work on. we get it you can cast things, but for now let me teach my users how i want to teach them.")
            time.sleep(1)
            print(" ")
            sp("system: all files have been closed by COMPUTER, who has left plane 42 of The Existance")
            print(" ")
            sp("suddenly, the console returns to black, your body is gone, and you and nines remain.")
            #have nines explain how this place works.
           
        else:
            sp("pick an option given idiot. copy and paste if you need to.")
            time.sleep(3)
            exit()
           
    elif absence == "2":
        sp("story unfinished")
    else:
        sp("please select an option given")
           
           
    # above this is par of on Nines_Response, below are the other responses.
#response 2
elif Nines_Response == "2":
    time.sleep(3)
    print(f"Nines: I guess only computer really knows. We will just have to wait and find out. I'll do my best to get you out of here.")
    time.sleep(3)
    print(f"Nines: Maybe finding out can help us deystroy him.")
#response 3
elif Nines_Response == "3":
    time.sleep(3)
    print(f"Nines: From what I can tell computer created computer, I don't think anyone is horrible enough to create this.")
   
else:
    print("please select an option given")
    time.sleep(5)
    print("Ending 0, The failure, cant even answer a question properly.")
    time.sleep(3)
    exit()

    #this is the current game end, i will add more later.
    #what the AI has taught us is that  i need to seperate different parts of the story into functions.
    # i need to implement slow text. and also add /n to the begining of all my "input" commands
    #TBAai has what im looking for kinda, just not with all my story.
