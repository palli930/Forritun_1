word = input('Enter a word: ')

wordl = word.lower()
lenght = len(wordl)
wordf = wordl[0]
word2 = wordl[1]

if lenght >= 3:
    word3 = wordl[2]
if lenght >= 4:
    word4 = wordl[3]
if lenght >= 5:
    word5 = wordl[4]
if lenght >= 6:
    word6 = wordl[5]
if lenght >= 7:
    word7 = wordl[6]
if lenght >= 8:
    word8 = wordl[7]
if lenght >= 9:
    word9 = wordl[8]
if lenght >= 10:
    word10 = wordl[9]


if wordf == 'a' or wordf == 'e' or wordf == 'y' or wordf =='u' or wordf =='o' or wordf =='i':
    print(word+'yay')
else:
    if (word2 == 'a' or word2 == 'e' or word2 == 'y' or word2 =='u' or word2 =='o' or word2 =='i') and (word3 != 'a' or word3 != 'e' or word3 != 'y' or word3 !='u' or word3 !='o' or word3 !='i'):
        print(wordl[1:]+wordl[0]+'ay')
    elif (word3 == 'a' or word3 == 'e' or word3 == 'y' or word3 =='u' or word3 =='o' or word3 =='i') and (word4 != 'a' or word4 != 'e' or word4 != 'y' or word4 !='u' or word4 !='o' or word4 !='i'):
        print(wordl[2:]+wordl[:2]+'ay')
    elif (word4 == 'a' or word4 == 'e' or word4 == 'y' or word4 =='u' or word4 =='o' or word4 =='i') and (word5 != 'a' or word5 != 'e' or word5 != 'y' or word5 !='u' or word5 !='o' or word5 !='i'):
        print(wordl[3:]+wordl[:3]+'ay')
    elif (word5 == 'a' or word5 == 'e' or word5 == 'y' or word5 =='u' or word5 =='o' or word5 =='i') and (word6 != 'a' or word6 != 'e' or word6 != 'y' or word6 !='u' or word6 !='o' or word6 !='i'):
        print(wordl[4:]+wordl[:4]+'ay')
    elif (word6 == 'a' or word6 == 'e' or word6 == 'y' or word6 =='u' or word6 =='o' or word6 =='i') and (word7 != 'a' or word7 != 'e' or word7 != 'y' or word7 !='u' or word7 !='o' or word7 !='i'):
        print(wordl[5:]+wordl[:5]+'ay')


while word != '.':
    if word == '.':
        break

    word = input('Enter a word: ')

    wordl = word.lower()
    lenght = len(wordl)
    wordf = wordl[0]
    
    if lenght >=2:
        word2 = wordl[1]
    if lenght >= 3:
        word3 = wordl[2]
    if lenght >= 4:
       word4 = wordl[3]
    if lenght >= 5:
       word5 = wordl[4]
    if lenght >= 6:
       word6 = wordl[5]
    if lenght >= 7:
       word7 = wordl[6]
    if lenght >= 8:
       word8 = wordl[7]
    if lenght >= 9:
       word9 = wordl[8]
    if lenght >= 10:
       word10 = wordl[9]

    if word == '.':
        exit()
    elif (wordf == 'a' or wordf == 'e' or wordf == 'y' or wordf =='u' or wordf =='o' or wordf =='i'):
        print(word+'yay')
    else:
        if (word2 == 'a' or word2 == 'e' or word2 == 'y' or word2 =='u' or word2 =='o' or word2 =='i') and (word3 != 'a' or word3 != 'e' or word3 != 'y' or word3 !='u' or word3 !='o' or word3 !='i'):
            print(wordl[1:]+wordl[0]+'ay')
        elif (word3 == 'a' or word3 == 'e' or word3 == 'y' or word3 =='u' or word3 =='o' or word3 =='i') and (word4 != 'a' or word4 != 'e' or word4 != 'y' or word4 !='u' or word4 !='o' or word4 !='i'):
            print(wordl[2:]+wordl[:2]+'ay')
        elif (word4 == 'a' or word4 == 'e' or word4 == 'y' or word4 =='u' or word4 =='o' or word4 =='i') and (word5 != 'a' or word5 != 'e' or word5 != 'y' or word5 !='u' or word5 !='o' or word5 !='i'):
            print(wordl[3:]+wordl[:3]+'ay')
        elif (word5 == 'a' or word5 == 'e' or word5 == 'y' or word5 =='u' or word5 =='o' or word5 =='i') and (word6 != 'a' or word6 != 'e' or word6 != 'y' or word6 !='u' or word6 !='o' or word6 !='i'):
            print(wordl[4:]+wordl[:4]+'ay')
        elif (word6 == 'a' or word6 == 'e' or word6 == 'y' or word6 =='u' or word6 =='o' or word6 =='i') and (word7 != 'a' or word7 != 'e' or word7 != 'y' or word7 !='u' or word7 !='o' or word7 !='i'):
            print(wordl[5:]+wordl[:5]+'ay')


