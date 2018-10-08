
x = 1 
y = 1
C = 0

def north(y):
    y += 1
    return y

def south(y):
    y -= 1
    return y 

def east(x):
    x += 1
    return x

def west(x):
    x -=1
    return x 

def lever(c):
    lever = input("Pull a lever (y/n): ")
    if lever == "y" or lever == "Y":
        c += 1
        print("You received 1 coins, your total is now {}.".format(C+1))
    else:
        c += 0
    return c


while x != 3 or y != 1:
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        while x == 1 and y == 1:
            move = input("Direction: ")
            if move == 'N' or move == 'n':
                y = north(y)
            else:
                print("Not a valid direction!")
    
    if x == 1 and y == 2:
        C = lever(C)
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        while x == 1 and y == 2:
            move = input("Direction: ")
            if move == "N" or move == 'n':
                y = north(y)
            elif move == "S" or move == "s":
                y = south(y)
            elif move == "E" or move == "e":
                x = east(x)
            else:
                print("Not a valid direction!")
    
    if x == 2 and y == 2:
        C = lever(C)
        print("You can travel: (S)outh or (W)est.")
        while x == 2 and y == 2:
            move = input("Direction: ")
            if move == "W" or move == "w":
                x = west(x)
            elif move == "S" or move == "s":
                y = south(y)
            else:
                print("Not a valid direction!")
    
    if x == 2 and y == 1:
        print("You can travel: (N)orth.")
        while x == 2 and y == 1:
            move = input("Direction: ")
            if move == "N" or move == 'n':
                y = north(y)
            else:
                print("Not a valid direction!")
    
    if x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        while x == 1 and y == 3:
            move = input("Direction: ")
            if move == "S" or move == "s":
                y = south(y)
            elif move == "E" or move == "e":
                x = east(x)
            else:
                print("Not a valid direction!")
    
    if x ==2 and y == 3:
        C = lever(C)
        print("You can travel: (E)ast or (W)est.")
        while x == 2 and y == 3:
            move = input("Direction: ")
            if move == "E" or move == "e":
                x = east(x)
            elif move =="W" or move == "w":
                x = west(x)
            else:
                print("Not a valid direction!")
    
    if x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
        while x == 3 and y == 3:
            move = input("Direction: ")
            if move == "S" or move == "s":
                y = south(x)
            elif move == "W" or move == "w":
                x = west(x)
            else:
                print("Not a valid direction!")
    
    if x == 3 and y == 2:
        C = lever(C)
        print("You can travel: (N)orth or (S)outh.")
        while x == 3 and y == 2:
            move = input("Direction: ")
            if move == "N" or move == 'n':
                y = north(y)
            elif move =="S" or move == "s":
                y = south(y)
            else:
                print("Not a valid direction!")


if x == 3 and y == 1:
    print("Victory!")
    
    