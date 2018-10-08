import random
import string


# les inn hverja linu i file.txt og setur i einn langan streng  
def get_word_string(filename):
    try:
        dataFile = open(filename,"r")
        wordString = ''
        for line in dataFile:
            wordString += line
    except:
        wordString = ""
        print("File "+filename+" not found")

    return wordString

#fall sem:
#1 fjarlaegir "\n", splittar kommur og punkta.
#2 shufflar stofum i hverju ordi, ad undanskyldum fyrsta og seinasta stafi
#3 breytir listanum aftur i streng 
def scramble_string(word_string):
    wordstring1 = word_string.split(" ")
    wordstring2 = []
    wordstring3 = []
    #1
    for i in wordstring1:
        i = i.replace("\n", "")
        if "," in i:
          j,k = i.split(",")
          wordstring2.append(j)
          wordstring2.append(",")
          wordstring2.append(k)
        elif "." in i :
            j,k = i.split(".")
            wordstring2.append(j)
            wordstring2.append(".")
            wordstring2.append(k)
        else:
            wordstring2.append(i)
#2
    for i in wordstring2:
        l = len(i)
        if l >= 4:
            first = i[0]
            last = i[(l-1)]
            k = i[1:-1]
            f = []
            for e in k:
                f.append(e)
            
            random.shuffle(f)
            str1 = ''.join(f)
            str2 = first+str1+last
            wordstring3.append(str2)
        else:
            wordstring3.append(i)
#3
    scrambled_string = ' '.join(wordstring3)
    scrambled_string = scrambled_string.replace(" ,", ",")
    scrambled_string = scrambled_string.replace(" .", ".")
    return scrambled_string

    

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)