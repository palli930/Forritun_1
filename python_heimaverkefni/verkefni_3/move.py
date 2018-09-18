Upphaf = 1
Endir = 10

pos = int(input("Input a position between "+str(Upphaf)+" and "+str(Endir)+": "))

current_pos = pos #Nuverandi stadsetning



def afram(x):
    global current_pos
    current_pos +=  1
    return current_pos

def bakka(x):
    global current_pos
    current_pos -= 1
    return current_pos 

print("l - for moving left")
print("r - for moving right") 
print("Any other letter for quitting")

r = 'r'
l = 'l'

hreyfing = input('Input your choice: ')

while hreyfing =='l' or hreyfing =='r':
    if hreyfing == 'r' and current_pos != Endir:
        afram(current_pos)
        print('New position is:',current_pos)
    elif hreyfing == 'r' and current_pos == Endir:
        print('New position is:',current_pos)
    elif hreyfing == 'l' and current_pos != Upphaf:
        bakka(current_pos)
        print('New position is:',current_pos)
    elif hreyfing == 'l' and current_pos == Upphaf:
        print('New position is:',current_pos)
    
    print("l - for moving left")
    print("r - for moving right") 
    print("Any other letter for quitting")
    hreyfing = input('Input your choice: ')

    if hreyfing != 'l' and hreyfing != 'r':
        print('New position is:',current_pos)
        break



    



