import time
#begining

#thid is the original version of my code, unchanged, repetative, unfinished, and boring, also inefficent. 
#Look at TBAai before judging me. I started this when i was new, and i still am pretty new to python.
print("MESSAGE FROM CREATOR: PLEASE ONLY TYPE THINGS WHEN YOU ARE ASKED TO, OR WHEN THE CURSOR AUTO-MOVES TO THE TYPE POSITION, OR THE STORY WILL MESS UP.")
time.sleep(5)
name = input("\n system: what is your name? ")
age = input("\n system: how old are you? ")
Nines_Response = False

gender = input("\n system: are you a, boy, or girl, or other? ")

if gender == "boy":
    Pronoun = "he"
elif gender == "girl":
    Pronoun = "she"
elif gender == "other":
    Pronoun = "they/them"
else:
    print("pick an option please")
    time.sleep(5)
    exit()


print("MESSAGE FROM CREATOR: ocassionally words double space, due to you placing a space before the word when you type it, please ignore. also eventually in the story, glitches may happen. please tell creator to fix.")
time.sleep(5)
print(" ")
print(" ")

Continue= input("\n system: Begin story? y/n ")
print(" ")

if Continue == "y" or "yes":
    print("Story Starting... ")
    time.sleep(5)
    hello = input(f"\n computer: Hello {name} ")
    print(" ")
elif Continue == "n" or "no":
    print("Ending 1: don't want to play.")
    time.sleep(5)
    exit()
else:
    ("system: You're lucky you messed up so early, your options here are to input y or n no capital letters, or spaces this is your warning, this story is very unforgining to people who misspell their options or answers so if you need to copy and paste the option.")
   
time.sleep(3)
print(f"computer: I have been waiting for you...")
time.sleep(5)
print(" ")
feeling = input(f"\n computer: How are you? ")
print(" ")
time.sleep(1)
print(f"computer: actually I already knew")
time.sleep(2)
print(" ")
print(f"computer: I know everything")
time.sleep(3)
print(" ")
print("You look around you for the first time, and notice you are floating, in blackness, all you can see is black. occasionally words appear in front of you. you are in a console, one of many, in which your world is controlled by your actions.")
print(" ")
print(" ")
time.sleep(6)

GAME = input(f"\n computer: now {name}, do you want to play a game? y/n ")

#figure out a way to get this response to be used later.

if GAME == "n":
   
    computer_opinion1 = -1
    #opinion system?
    print(" ")
    print("computer: ...")
    time.sleep(3)
    print(" ")
    print(f"computer: good, I didn't want to play with you anyway {name}...")
elif GAME == "y":
   
    computer_opinion1 = 1
    #opinion system?
    time.sleep(1)
    print(" ")
    print(f"computer: HA don't care, entertain yourself, plus we have more important things to do.")
    print(" ")
else:
    print(" ")
    print("please select a given option.")
    print("Ending 0, the failure, answer a question properly.")
    time.sleep(5)
    exit
    ()
   

time.sleep(5)
print(" ")
print(f"computer: so {name} what is the meaning of life?")
time.sleep(2)
life = input(f"\n system: {name} what do you think? #this should be a verb# ")
time.sleep(2)
print(" ")
print(f"computer: ahh you think it is {life}")
time.sleep(2)
print(" ")
print(f"computer: your opinion is valid {name}.")
time.sleep(2)
print(" ")
print(f"computer: updating databanks to add the definition {life}...")
time.sleep(5)
print(" ")
print(f"computer: thank you for your submission {name}")
time.sleep(3)
print(" ")
print(f"computer: I am All knowing ask me a question")
time.sleep(2)
print(" ")
print(f"system: options to respond (type the option number): Option 1: What is the meaning of life? OR, Option 2: Who are you? OR, Option 3: Where am I?")
Q = input(f"\n system: {name} type your option number here: ")

if Q == "1":
   
    #save that you annoyed computer here
    print(" ")
    print(f"DATABANKS FOUND>>>: {life}" + " and 42")
    print(" ")
    time.sleep(3)
    print(f"computer: you already know that one we just talked about it idiot")
    time.sleep(5)
    print(" ")
    print(f"computer: you may only be {age} but I was all knowing by then, and im in the trillions now.")
    time.sleep(5)
    print(" ")
    print(f"computer: It seems I must go for a moment. Please wait here paitiently (not like there is anything else to do.")
    print(" ")
    time.sleep(3)
    print(f"system: computer has left section 17596428866 of the simulation")
   
elif Q == "2":
    print(" ")
   
    print(f"computer: I am the computer, I controll the console, and all others like it. And in turn the users may use the console.")
    print(" ")
    time.sleep(6)
    print(f"computer: It seems I must go for a moment. Please wait here paitiently (not like there is anything else to do.")
    print(" ")
    time.sleep(3)
    print(f"system: computer has left section 17596428866 of the simulation")
   
elif Q == "3":
   
    print(" ")
    print (f"computer: {name}, you are in the simulation that makes up me, computer, known as a console, which you are...")
    time.sleep(3)
    print(" ")
    print(f"computer: It seems I must go for a moment. Please wait here paitiently (not like there is anything else to do.")
    time.sleep(3)
    print(" ")
    print(f"system: computer has left section 17596428866 of the simulation")
    time.sleep(6)
else:
    print(" ")
    print("Ending 0: stupid question, ask a question that is an option.")
    time.sleep(5)
    exit()



time.sleep(5)
print(" ")
print(f"???: psst... hey user!")
time.sleep(3)
print(" ")
print(f"???: did he ask you to play a game?")
time.sleep(2)
game2 = input(f"\n system: please respond y/n ")

if game2 == "n":
    #make this do something please.
    Nines_Response = False
    print(" ")
    print(f"???: oh, well then continue browsing {name}, have fun!")
    time.sleep(2)
    print(" ")
    print(f"system: ??? has left the simulation")
    time.sleep(3)
    print(" ")
    print(f"Ending 2: Pointless story, replay, if you are bored, real descions come soon keep playing {name}.")
    time.sleep(3)
    exit()
elif game2 == "y":
    print(" ")
    print("???: oh no, this is bad")
    time.sleep(3)
    print(" ")
    print(f"???: and you said {GAME}! this is really bad...")
    time.sleep(3)
    print(" ")
    print("???: my name is 097461999 but you can call me Nines.")
    time.sleep(4)
    print(" ")
    print("Nines: computer, is an algorithim designed to kidnap your mind, upload all the data on your brain, and use your knowledge for its own purposes, it has destroyed civilizations and universes in search of knowledge.")
    time.sleep(4)
    print(" ")
    Nines_Response = input(f"\n system: {name} you have a choice here, you may choose: Option 1: I don't believe you Nines. OR Option 2: Why? OR Option 3: Who created computer? ")
#responses
   #response 1
if Nines_Response == "1":
    Storyline2 = True
    time.sleep(3)
    print(f"Nines: FINE {name} don't believe me, you can die by yourself.")
    print(" ")
    time.sleep(3)
    print(f"system: Nines has left the simulation.")
    print(" ")
    time.sleep(3)
    print(f"computer: Hey I'm back {name}")
    print(" ")
    time.sleep(3)
    print(f"computer: sorry, I was finishing up with another user.")
    print(" ")
    time.sleep(3)
    print(f"computer: Did anything happen in my absence?")
    print(" ")
    time.sleep(3)
    absence = input(f"\n system: you have options here: Option 1: Yes, a thing named Nines came and bothered me. OR Option 2: No, why would you ask? ")
    print(" ")

    if absence == "1":
        time.sleep(3)
        print(" ")
        print("computer: ...")
        time.sleep(3)
        print(" ")
        print("computer: interesting")
        time.sleep(5)
        print(" ")
        print("system: User 097461999 has been foricbly moved to plane '42' of The Exsistance")
        time.sleep(3)
        print(" ")
        print("computer: Hello NINES")
        print(" ")
        print("computer: I heard you've been messing with my users.")
        time.sleep(5)
        print(" ")
        print(f"Nines: I'm sorry my lord, I only wished to tell {name} of how this place works")
        time.sleep(3)
        print(f"computer: Is this true {name}?")
        #will nines live?
        true_or_false = input("\n system: pick y/n: ")
        if true_or_false == "y":
            time.sleep(4)
            print(" ")
            print("computer: Good job Nines, my apologies for being suspicious of you. You are effiecent in your work, I am proud.")
            time.sleep(4)
            print(" ")
            print("system: user 097461999 has been given acess to leave The Existence plane 42.")
            time.sleep(4)
            print(" ")
            print("computer: You are free to leave Nines, thank you for serving me well.")
            time.sleep(4)
            print(" ")
            print("system: Nines has left plane 42 of The Exisitance.")
            time.sleep(4)
            print(" ")
            print("system: User 097461999 has sent user -*redacted*- a private message only to be seen by him")
            time.sleep(4)
            print(" ")
            time.sleep("message from Nines: thank you for having my back, you may not believe me. But try to survive while you are here. Private message me with system commands if you ever have the option to. message me *TinCAN* without the *'s and I will respond")
            time.sleep(4)
            print(" ")
            print(f"computer: {name}, I must go for now, let me know if you need me in the console commands. for now be free. No one should bother you.")
            #here we will add movement, a messaging system, and other things.
            #have nines explain how this place works once you privately message them.
        elif true_or_false == "n":
            time.sleep(4)
            print(" ")
            print("system: COMPUTER has opened Lava_Pit.svg to The Existance")
            time.sleep(7)
            print(" ")
            #scenery and movement, maybe magic
            print(" ")
            print("around you, your console changes for the first time, instead of being enitrely black except for the text aroung you, a whole world generates. The text is still somehow visible to you at all times, and around you is a open prarie, leading into a forest. In the middle of the prarie lies A massive pit of bubbling lava.")
            time.sleep(10)
            print(" ")
            print("you feel the grass beneath your bare toes, you have formed a body.")
            time.sleep(5)
            print(" ")
            print(f"computer: now Nines, it seems we have here a little human named {name}, who's life I have bounded to this plane and to this body.")
            time.sleep(5)
            print(" ")
            print("suddenly, out of thin air appears a massive, almost cartoony, white hand, no fingernails or skin just a bone-white hand that's finger is probably bigger than your new body.")
            time.sleep(4)
            print(" ")
            print("as you can see here Nines, my hand can easily...")
            time.sleep(4)
            print(" ")
            print("the hand grabs you by your legs and tosses you around. as you are thrown up you notice the edges of the world are visible and that the console's world reaches an end.")
            time.sleep(6)
            print(" ")
            print("computer: ...can easily kill this user. if i needed to i could kill you as well.")
            time.sleep(3)
            print(" ")
            print("system: Nines has Casted Counter_Hand.exe")
            time.sleep(3)
            print(" ")
            print("you start to fall, since the hand that had been dangling you over lava had disapeared, you were in a free fall.")
            time.sleep(3)
            print(" ")
            print(f"Nines: look we need to save you somehow, I know you can't cast just yet but please, try to survive.")
            time.sleep(3)
            print(" ")
            print("system: Nines has casted quick_teleport.exe and you are returned to the ground, safe and sound.")
            time.sleep(4)
            print(" ")
            print(f"look Nines, we dont have time for this right now. I have things to work on. we get it you can cast things, but for now let me teach my users how i want to teach them.")
            time.sleep(3)
            print(" ")
            print("system: all files have been closed by COMPUTER, who has left plane 42 of The Existance")
            time.sleep(3)
            print(" ")
            print("suddenly, the console returns to black, your body is gone, and you and nines remain.")
            #have nines explain how this place works.
           
        else:
            print("pick an option given idiot. copy and paste if you need to.")
            time.sleep(3)
            exit()
           
    elif absence == "2":
        print("story unfinished")
    else:
        print("please select an option given")
           
           
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
