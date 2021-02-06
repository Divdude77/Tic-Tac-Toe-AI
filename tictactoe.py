import random


def changelists(xo, spot):
    if spot[0] == "a":
        if spot[1] == "1":
            ROW_A[0] = xo
            COL_1[0] = xo
            DIA1[0] = xo
        elif spot[1] == "2":
            ROW_A[1] = xo
            COL_2[0] = xo
        elif spot[1] == "3":
            ROW_A[2] = xo
            COL_3[0] = xo
            DIA2[0] = xo
    elif spot[0] == "b":
        if spot[1] == "1":
            ROW_B[0] = xo
            COL_1[1] = xo
        elif spot[1] == "2":
            ROW_B[1] = xo
            COL_2[1] = xo
            DIA1[1] = xo
            DIA2[1] = xo
        elif spot[1] == "3":
            ROW_B[2] = xo
            COL_3[1] = xo
    elif spot[0] == "c":
        if spot[1] == "1":
            ROW_C[0] = xo
            COL_1[2] = xo
            DIA2[2] = xo
        elif spot[1] == "2":
            ROW_C[1] = xo
            COL_2[2] = xo
        elif spot[1] == "3":
            ROW_C[2] = xo
            COL_3[2] = xo
            DIA1[2] = xo


def printboard():
    print("     1      2      3   ")
    c = 0
    for a in gameboard:
        print(alphalist[c], gameboard[a])
        c += 1


while True:
    ROW_A = ["a1", "a2", "a3"]
    ROW_B = ["b1", "b2", "b3"]
    ROW_C = ["c1", "c2", "c3"]
    COL_1 = ["a1", "b1", "c1"]
    COL_2 = ["a2", "b2", "c2"]
    COL_3 = ["a3", "b3", "c3"]
    DIA1 = ["a1", "b2", "c3"]
    DIA2 = ["a3", "b2", "c1"]
    gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"], "TAB_c": ["| |", "| |", "| |"]}
    running = True
    playagain = False
    alphalist = ["a", "b", "c"]
    FREE_SPACE = []
    print("----------------------- TIC-TAC-TOE -----------------------")
    print()
    print("1. Play against a bot")
    print("2. Play against a friend")
    print("3. Exit")
    print()
    z = int(input("How would you like to play?: "))
    if z == 1:
        print()
        print("------------------------ SOLO MODE ------------------------")
        while running:
            print()
            printboard()
            print()
            inputting = True
            choice = input("Where would you like to place your 'X'?: ")
            choice = choice.lower()
            while inputting:
                if choice in ROW_A or choice in ROW_B or choice in ROW_C:
                    changelists("X", choice)
                    inputting = False
                else:
                    print()
                    print("That's not an empty spot!")
                    print()
                    choice = input("Where would you like to place your 'X'?: ")
                    choice = choice.lower()

            s1 = "TAB_" + choice[0]
            s2 = int(choice[1]) - 1
            gameboard[s1][s2] = '|X|'

            if ROW_A.count("X") == 3 or ROW_B.count("X") == 3 or ROW_C.count("X") == 3 or COL_1.count(
                    "X") == 3 or COL_2.count("X") == 3 or COL_3.count("X") == 3 or DIA1.count("X") == 3 or DIA2.count(
                    "X") == 3:
                printboard()
                print()
                print("CONGRATULATIONS! You win!")
                while True:
                    yn = input("Would you like to play again? (Y/N): ")
                    yn = yn.lower()
                    if yn == "y":
                        ROW_A = ["a1", "a2", "a3"]
                        ROW_B = ["b1", "b2", "b3"]
                        ROW_C = ["c1", "c2", "c3"]
                        COL_1 = ["a1", "b1", "c1"]
                        COL_2 = ["a2", "b2", "c2"]
                        COL_3 = ["a3", "b3", "c3"]
                        DIA1 = ["a1", "b2", "c3"]
                        DIA2 = ["a3", "b2", "c1"]
                        gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"],
                                     "TAB_c": ["| |", "| |", "| |"]}
                        break
                    elif yn == "n":
                        print()
                        print("Returning back to menu...")
                        print()
                        running = False
                        break
                    else:
                        print("Please enter a correct value!")

            elif ROW_A.count("O") == 2 and ROW_A.count("X") != 1:
                for i in ROW_A:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif ROW_B.count("O") == 2 and ROW_B.count("X") != 1:
                for i in ROW_B:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif ROW_C.count("O") == 2 and ROW_C.count("X") != 1:
                for i in ROW_C:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif COL_1.count("O") == 2 and COL_1.count("X") != 1:
                for i in COL_1:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif COL_2.count("O") == 2 and COL_2.count("X") != 1:
                for i in COL_2:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif COL_3.count("O") == 2 and COL_3.count("X") != 1:
                for i in COL_3:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif DIA1.count("O") == 2 and DIA1.count("X") != 1:
                for i in DIA1:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif DIA2.count("O") == 2 and DIA2.count("X") != 1:
                for i in DIA2:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif ROW_A.count("X") == 2 and ROW_A.count("O") != 1:
                for i in ROW_A:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif ROW_B.count("X") == 2 and ROW_B.count("O") != 1:
                for i in ROW_B:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif ROW_C.count("X") == 2 and ROW_C.count("O") != 1:
                for i in ROW_C:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif COL_1.count("X") == 2 and COL_1.count("O") != 1:
                for i in COL_1:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif COL_2.count("X") == 2 and COL_2.count("O") != 1:
                for i in COL_2:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif COL_3.count("X") == 2 and COL_3.count("O") != 1:
                for i in COL_3:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif DIA1.count("X") == 2 and DIA1.count("O") != 1:
                for i in DIA1:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)

            elif DIA2.count("X") == 2 and DIA2.count("O") != 1:
                for i in DIA2:
                    if i != "O" and i != "X":
                        s1 = "TAB_" + i[0]
                        s2 = int(i[1]) - 1
                        gameboard[s1][s2] = '|O|'
                        changelists("O", i)
            else:
                FREE_SPACE = []
                for i in ROW_A:
                    if i != "X" and i != "O":
                        FREE_SPACE.append(i)
                for i in ROW_B:
                    if i != "X" and i != "O":
                        FREE_SPACE.append(i)
                for i in ROW_C:
                    if i != "X" and i != "O":
                        FREE_SPACE.append(i)
                if not FREE_SPACE:
                    print()
                    printboard()
                    print()
                    print("Tie Game!")
                    print()
                    while True:
                        yn = input("Would you like to play again? (Y/N): ")
                        yn = yn.lower()
                        if yn == "y":
                            ROW_A = ["a1", "a2", "a3"]
                            ROW_B = ["b1", "b2", "b3"]
                            ROW_C = ["c1", "c2", "c3"]
                            COL_1 = ["a1", "b1", "c1"]
                            COL_2 = ["a2", "b2", "c2"]
                            COL_3 = ["a3", "b3", "c3"]
                            DIA1 = ["a1", "b2", "c3"]
                            DIA2 = ["a3", "b2", "c1"]
                            gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"],
                                         "TAB_c": ["| |", "| |", "| |"]}
                            break
                        elif yn == "n":
                            print()
                            print("Returning back to menu...")
                            print()
                            running = False
                            break
                        else:
                            print("Please enter a correct value!")

                else:
                    bot_choice = random.choice(FREE_SPACE)
                    changelists("O", bot_choice)
                    s1 = "TAB_" + bot_choice[0]
                    s2 = int(bot_choice[1]) - 1
                    gameboard[s1][s2] = '|O|'

            if ROW_A.count('O') == 3 or ROW_B.count('O') == 3 or ROW_C.count('O') == 3 or COL_1.count(
                    "O") == 3 or COL_2.count(
                    "O") == 3 or COL_3.count("O") == 3 or DIA1.count("O") == 3 or DIA2.count("O") == 3:
                print()
                printboard()
                print()
                print("You lose! Better luck next time!")
                while True:
                    yn = input("Would you like to play again? (Y/N): ")
                    yn = yn.lower()
                    if yn == "y":
                        ROW_A = ["a1", "a2", "a3"]
                        ROW_B = ["b1", "b2", "b3"]
                        ROW_C = ["c1", "c2", "c3"]
                        COL_1 = ["a1", "b1", "c1"]
                        COL_2 = ["a2", "b2", "c2"]
                        COL_3 = ["a3", "b3", "c3"]
                        DIA1 = ["a1", "b2", "c3"]
                        DIA2 = ["a3", "b2", "c1"]
                        gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"],
                                     "TAB_c": ["| |", "| |", "| |"]}
                        print()
                        break
                    elif yn == "n":
                        print()
                        print("Returning back to menu...")
                        print()
                        running = False
                        break
                    else:
                        print("Please enter a correct value!")

    elif z == 2:
        print()
        print("-------------------- MULTIPLAYER MODE ---------------------")
        while running:
            print()
            printboard()
            print()
            inputting = True
            choice1 = input("P1: Where would you like to place your 'X'?: ")
            choice1 = choice1.lower()
            while inputting:
                if choice1 in ROW_A or choice1 in ROW_B or choice1 in ROW_C:
                    changelists("X", choice1)
                    inputting = False
                else:
                    print()
                    print("That's not an empty spot!")
                    print()
                    choice1 = input("P1: Where would you like to place your 'X'?: ")
                    choice1 = choice1.lower()

            s1 = "TAB_" + choice1[0]
            s2 = int(choice1[1]) - 1
            gameboard[s1][s2] = '|X|'
            print()
            printboard()
            if ROW_A.count('X') == 3 or ROW_B.count('X') == 3 or ROW_C.count('X') == 3 or COL_1.count(
                    "X") == 3 or COL_2.count(
                    "X") == 3 or COL_3.count("X") == 3 or DIA1.count("X") == 3 or DIA2.count("X") == 3:
                print()
                print("P1 wins!")
                while True:
                    yn = input("Would you like to play again? (Y/N): ")
                    yn = yn.lower()
                    if yn == "y":
                        ROW_A = ["a1", "a2", "a3"]
                        ROW_B = ["b1", "b2", "b3"]
                        ROW_C = ["c1", "c2", "c3"]
                        COL_1 = ["a1", "b1", "c1"]
                        COL_2 = ["a2", "b2", "c2"]
                        COL_3 = ["a3", "b3", "c3"]
                        DIA1 = ["a1", "b2", "c3"]
                        DIA2 = ["a3", "b2", "c1"]
                        gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"],
                                     "TAB_c": ["| |", "| |", "| |"]}
                        print()
                        playagain = True
                        break
                    elif yn == "n":
                        print()
                        print("Returning back to menu...")
                        print()
                        running = False
                        break
                    else:
                        print("Please enter a correct value!")

            else:
                FREE_SPACE = []
                for i in ROW_A:
                    if i != "X" and i != "O":
                        FREE_SPACE.append(i)
                for i in ROW_B:
                    if i != "X" and i != "O":
                        FREE_SPACE.append(i)
                for i in ROW_C:
                    if i != "X" and i != "O":
                        FREE_SPACE.append(i)

            if not playagain and FREE_SPACE and running:
                print()
                inputting = True
                choice2 = input("P2: Where would you like to place your 'O'?: ")
                choice2 = choice2.lower()
                while inputting:
                    if choice2 in ROW_A or choice2 in ROW_B or choice2 in ROW_C:
                        changelists("O", choice2)
                        inputting = False
                    else:
                        print()
                        print("That's not an empty spot!")
                        print()
                        choice2 = input("P2: Where would you like to place your 'O'?: ")
                        choice2 = choice2.lower()

                    s1 = "TAB_" + choice2[0]
                    s2 = int(choice2[1]) - 1
                    gameboard[s1][s2] = '|O|'

                if ROW_A.count('O') == 3 or ROW_B.count('O') == 3 or ROW_C.count('O') == 3 or COL_1.count(
                        "O") == 3 or COL_2.count(
                        "O") == 3 or COL_3.count("O") == 3 or DIA1.count("O") == 3 or DIA2.count("O") == 3:
                    print()
                    printboard()
                    print()
                    print("P2 wins!")
                    while True:
                        yn = input("Would you like to play again? (Y/N): ")
                        yn = yn.lower()
                        if yn == "y":
                            ROW_A = ["a1", "a2", "a3"]
                            ROW_B = ["b1", "b2", "b3"]
                            ROW_C = ["c1", "c2", "c3"]
                            COL_1 = ["a1", "b1", "c1"]
                            COL_2 = ["a2", "b2", "c2"]
                            COL_3 = ["a3", "b3", "c3"]
                            DIA1 = ["a1", "b2", "c3"]
                            DIA2 = ["a3", "b2", "c1"]
                            gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"],
                                         "TAB_c": ["| |", "| |", "| |"]}
                            print()
                            break
                        elif yn == "n":
                            print()
                            print("Exiting...")
                            running = False
                            break
                        else:
                            print("Please enter a correct value!")

            elif not FREE_SPACE and not playagain and running:
                print()
                print("Tie Game!")
                while True:
                    yn = input("Would you like to play again? (Y/N): ")
                    yn = yn.lower()
                    if yn == "y":
                        ROW_A = ["a1", "a2", "a3"]
                        ROW_B = ["b1", "b2", "b3"]
                        ROW_C = ["c1", "c2", "c3"]
                        COL_1 = ["a1", "b1", "c1"]
                        COL_2 = ["a2", "b2", "c2"]
                        COL_3 = ["a3", "b3", "c3"]
                        DIA1 = ["a1", "b2", "c3"]
                        DIA2 = ["a3", "b2", "c1"]
                        gameboard = {"TAB_a": ["| |", "| |", "| |"], "TAB_b": ["| |", "| |", "| |"],
                                     "TAB_c": ["| |", "| |", "| |"]}
                        break
                    elif yn == "n":
                        print()
                        print("Exiting...")
                        running = False
                        break
                    else:
                        print("Please enter a correct value!")

    elif z == 3:
        print()
        print("Exiting...")
        break
