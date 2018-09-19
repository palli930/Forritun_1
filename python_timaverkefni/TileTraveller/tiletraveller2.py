#https://github.com/palli930/Forritun_1/tree/master/python_timaverkefni/TileTraveller

# 1) Seinni implementation var orlitid erfitari, 
# en bara vegna tess eg turfti adeins ad kynna mer hvernig functions virka

# 2) Audveldara ad lesa fyrri implementation, vegna tess i henni tarftu ekki ad skilja functions.

# 3) ???

x = 1 
y = 1

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
    
    
    
    


