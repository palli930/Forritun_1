#https://github.com/palli930/Forritun_1/tree/master/python_timaverkefni/TileTraveller

x = 1 
y = 1

if x == 1 and y == 1:
    print("You can travel: (N)orth.")
    while x == 1 and y == 1:
        move = input("Direction: ")
        if move == 'N' or move == 'n':
            y += 1
        else:
            print("Not a valid direction!")

if x == 1 and y == 2:
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    while x == 1 and y == 2:
        move = input("Direction: ")
        if move == "N" or move == 'n':
            y += 1
        elif move == "S" or move == "s":
            y -= 1
        elif move == "E" or move == "e":
            x += 1
        else:
            print("Not a valid direction!")

if x == 2 and y == 2:
    print("You can travel: (E)ast or (S)outh.")
    while x == 2 and y == 2:
        move = input("Direction: ")
        if move == "E" or move == "e":
            x -= 1
        elif move == "S" or move == "s":
            y -= 1
        else:
            print("Not a valid direction!")

if x == 2 and y == 1:
    print("You can travel: (N)orth.")
    while x == 2 and y == 1:
        move = input("Direction: ")
        if move == "N" or move == 'n':
            y += 1
        else:
            print("Not a valid direction!")

if x == 1 and y == 3:
    print("You can travel: (E)ast or (S)outh.")
    while x == 1 and y == 3:
        move = input("Direction: ")
        if move == "S" or move == "s":
            y -=1
        elif move == "E" or move == "e":
            x += 1
        else:
            print("Not a valid direction!")

if x ==2 and y == 3:
    print("You can travel: (E)ast or (W)est.")
    while x == 2 and y == 3:
        move = input("Direction: ")
        if move == "E" or move == "e":
            x += 1
        elif move =="W" or move == "w":
            x -= 1
        else:
            print("Not a valid direction!")

if x == 3 and y == 3:
    print("You can travel: (S)outh or (W)est.")
    while x == 3 and y == 3:
        move = input("Direction: ")
        if move == "S" or move == "s":
            y -= 1
        elif move == "W" or move == "w":
            x -= 1
        else:
            print("Not a valid direction!")

if x == 3 and y == 2:
    print("You can travel: (N)orth or (S)outh.")
    while x == 3 and y == 2:
        move = input("Direction: ")
        if move == "N" or move == 'n':
            y += 1
        elif move =="S" or move == "s":
            y -= 1
        else:
            print("Not a valid direction!")

if x == 3 and y == 1:
    print("Victory!")
    
    


