import random
PL1_HIGH_SCORE=PL2_HIGH_SCORE = 0
win={1:3,2:1,3:2}
def game():
    global PL1_HIGH_SCORE,PL2_HIGH_SCORE
    while True:
        print("\nCHOICES:\n1. START Game\n2. PLAYER1 High Score\n3. PLAYER2 High Score\n4. QUIT Game")
        try:
            CH = int(input("\nEnter your Choice(1/2/3/4): "))
        except ValueError:
            print("Invalid Input")
            continue

        if CH == 1:
            PL1_TOTAL=PL2_TOTAL = 0
            print("\nLet's Start the Game !")
            try:
                PL = int(input("\nEnter number of Players: "))
                numG = int(input("\nEnter number of Games you want to play: "))
            except ValueError:
                print("Invalid Input")
                continue
            print("\n1. Rock\n2. Paper\n3. Scissors")

            for g in range(numG):
                try:
                    PL1 = int(input("\nPLAYER1 Enter your Choice (1,2,3): "))
                except ValueError:
                    print("Invalid Input, Enter (1,2,3) only")
                    continue
                if PL==1:
                    PL2 = random.randrange(1, 4)
                    print("\nComputer's Choice(Player 2): ",PL2)
                elif PL==2:
                    try:
                        PL2=int(input("\nPlayer2 Enter your Choice(1,2,3): "))
                    except ValueError:
                        print("Invalid Input")
                        continue
                else:
                    print("\nInvalid Number of Players")
                    
                if PL1==PL2:
                    print("\nTIE")
                elif win[PL1] == PL2:
                    print("\nPLAYER1 WINS")
                    PL1_TOTAL+=1                    
                    PL1_HIGH_SCORE=max(PL1_TOTAL,PL1_HIGH_SCORE)
                else:
                    print("\nPLAYER2 WINS")
                    PL2_TOTAL+=1
                    PL2_HIGH_SCORE=max(PL2_TOTAL,PL2_HIGH_SCORE)
            
            if PL1_TOTAL > PL2_TOTAL:
                print("\n\nPLAYER1 is the WINNER of this Game")
            elif PL1_TOTAL < PL2_TOTAL:
                print("\n\nPLAYER2 is the WINNER of this Game")
            else:
                print("\n\nIt's a TIE")
                
        elif CH == 2:
            print("\nPLAYER1 High Score is: ", PL1_HIGH_SCORE)
        elif CH == 3:
            print("\nPLAYER2 High Score is: ", PL2_HIGH_SCORE)
        elif CH == 4:
            print("\nThankyou for Playing")
            break
        else:
            print("\nINVALID CHOICE")


game()