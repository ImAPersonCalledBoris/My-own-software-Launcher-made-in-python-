import time as t
import os

print("========================================================================================================================")
print("===============================================VERSION 0.0.9============================================================")
print("========================================================================================================================")
t.sleep(1)
print("   ")
print("Hi! welcome to the main menu, from here you can access to the software Launcher or go to see the latest version of the changelog or see the credits")
t.sleep(1)
print("  ")
print("""a. go to the software Launcher
b. go to the changelog
c. go to  credits""")
print("  ")
main_menu_selection = input("what do you want to do? >  ")

for letter in main_menu_selection:
 if letter in "aA":
  print("you have chosen A")
  t.sleep(1)
  print("  ")
  print("I'm redirecting you to the software Launcher...")
  t.sleep(1)
  print("  ")
  print("""a. interactive book reader [BUGGED]
b. rock,paper,scissors game
c. calculator
d. animate your text!""")
  software_da_eseguire = input("which software you want to run?")
  t.sleep(1)
  
  for letter in software_da_eseguire:
   if letter in "aA":
        print("Starting INTERACTIVE BOOK READER ...")
        t.sleep(1)
        print("   ")
        print("MESSAGGIO_FROM_DEVELOPER: Hello, unfortunately this software is not finished yet and still does not have a graphical interface, but if you are running it in preview it may mean only two things, or you are a friend of mine to whom it relaxes all the updates or you are a beta tester of Github, Either way, if you want to give me feedback and advice you can easily write me about discord! @ info - Chan#8725 ")
        t.sleep(3)
        print("   ")
        print("===========-NEW STORIES COMING SOON!-======================================================================")
        print("=================-YOU ARE RUNNING THE PRE-ALPHA 0.1.0 VERSION OF INTERACTIVE PYTHON BOOK-==================")
        print("=======================================- TO SEND FEEDBACK WRITE ME ON DISCORD info - Chan #8725 -==========")
        print("     ")
        t.sleep(1)

        player_name = input("Hello! Before we begin, what’s your name? > ")
        print("Perfect, so you’re " + player_name + " right?")
        risposta_nome = input("> ")

        for letter in risposta_nome:
            if letter in "yesYES":
                print("Name entered correctly!")

        for letter in risposta_nome:
            if letter in "noNO":
                player_name = input("Isn’t that right? Rewrite it here! > ")

        print("  ")
        print("Ok " + player_name + " you can choose one of these stories [ IN THE FUTURE THERE WILL BE OTHERS ] ")
        t.sleep(1)
        print("   ")
        print("[ONE] = STYLE = Fantasy | TITLE = Arganock the Knight of Regalopia")
        t.sleep(1)
        print("[TWO] = COMING SOON...")
        t.sleep(1)
        print("[THREE] = COMING SOON...")
        t.sleep(1)
        print("NEW STORIES COMING SOON...")
        t.sleep(2)
        storia_da_leggere = input("So, what story do you want to read?? [WRITE THE NUMBER IN LETTERS] > ")
        for letter in storia_da_leggere:    
            if letter in "unoUNOoneONE":
                print("Selected story: Arganock the knight of Regalopia ") 
                t.sleep(1)
                print(" ")
                print("Once upon a time there was Arganock, a knight who lived in Regalopia, a city ruled by King Zog, here will be your first choice, Arganock will be male or female??")
                sesso_arganock = input(">  ")
                print("Okay, Arganock will be " + sesso_arganock + " !")
                t.sleep(1)
                print("Let's continue with our story!")
                t.sleep(1)
                print("   ")
                print("Arganock was a knight who was part of the King’s escort, and he was the most trusted member.")
                t.sleep(1)
                print("was a day like any other in Regalopia and Arganock was in the dorm along with a new recruit...")
                t.sleep(1)
                print("The new recruit asks if you can give her a tour of the castle, do you want to do it??")
                t.sleep(1)
                print("[here comes a new choice for you! ]")
                t.sleep(1)
                risposta_tour_recluta = input("Say YES or NO  > ") 
                for letter in risposta_tour_recluta:    
                    if letter in "YESyes":
                        print("so You have chosen " + risposta_tour_recluta)
                        t.sleep(1)
                        print("  ")
                        print("*Give the recruit a tour and in the meantime start talking and getting to know each other, the recruit asks you your name, you answer <<Arganock>> and she tells you...")
                        t.sleep(1)
                        print("  ")
                        nome_recluta = input("[What do you want the recruit to be called??] >  ")
                        t.sleep(1)
                        print("...and she says her name is " + nome_recluta + " ")
                        t.sleep(1)
                        print("STORY TO END")
                    
        for letter in storia_da_leggere:
            if letter in "twoTWO":
                print("LOADING HISTORY, WAITING...")
                t.sleep(1)
                print("STORY NOT YET IMPLEMENTED :( ")

        for letter in storia_da_leggere:
            if letter in "threeTHREE":
                print("LOADING HISTORY, WAITING...")
                t.sleep(1)
                print("STORY NOT YET IMPLEMENTED :( ")

                      


  for letter in software_da_eseguire:
   if letter in "bB":
    print("starting  ROCK,PAPER,SCISSORS GAME...")
    t.sleep(1)
    print("   ")
    from random import randint

    t = ["rock", "paper", "scissors"]


    computer = t[randint(0,2)]


    player = False
    while player == False:
        player = input("rock,paper or scissors? >  ")
        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose", computer, "cut", player)
            else:
                print("You win!", player, "covers")
        elif player == "scissors":
            if computer == "rock":
                print("You lose", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]

    
    
    for letter in software_da_eseguire:
        if letter in "cC":
            print("   ")
            print("you have chosen C")
            print("   ")
            t.sleep(1)
            print("starting calculator")
            t.sleep(1)
            print("  ")

            def add(x, y):
                return x + y
            
            def subtract(x, y):
                return x - y
            
            def multiply(x, y):
                return x * y
            
            def divide(x, y):
                return x / y
            
            print("Select operation.")
            print("1. Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while True:
                choice = input("Enter choice(1/2/3/4): ")

                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))
                    
                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))
                    
                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))

                    break
                else:
                    print("Invalid Input")


for letter in software_da_eseguire:
    if letter in "dD":
        print("  ")
        print("starting ANIMATE YOUR TEXT...")
        t.sleep(1)
        print("  ")
        import time as t
        import os

        def animate_text(text):
            numberOfCharacters=1
            while True:
                print("\n")
                print(text[0:numberOfCharacters])
                numberOfCharacters += 1
                if numberOfCharacters > len(text):
                    numberOfCharacters = 0
                t.sleep(0.2)  

        testo_da_animare = input("che testo vuoi che venga animato?? > ")
        animate_text(testo_da_animare) 



for letter in main_menu_selection:
 if letter in "bB":
  print("you have chosen B")
  t.sleep(1)
  print("  ")
  print("LOADING CHANGELOG...")
  t.sleep(1)
  print("""VERSION 0.0.8
  What's new??
        -added "animate you text" to the software launcher
        -added the calculator to the software launcher
        -added the rock,paper,scissors game in the software launcher
        -added interactive_book_reader.py in the software launcher
        -fixed changelog bug
        - added credits
        -added the changelog
        -added main menu
        
        
        
        
        
        
        """)
  print("  ")
  t.sleep(1)
  print(" To return to the main menu, restart the program :( ")

for letter in main_menu_selection:
 if letter in "cC":
  print("  ")
  t.sleep(1)
  print("you have chosen C")
  t.sleep(1)
  print("  ")
  print("Software created by Mario, if you want to leave a review or suggest an improvement you can write him on discord @ info -Chan#8725  ")
  print("   ")
  print("to return to the main menu restart the program :(  ")
