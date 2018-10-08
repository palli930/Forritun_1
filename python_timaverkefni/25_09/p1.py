import string

sentence = input("Input a sentence: ")
sentence1 = sentence.replace(' ', '')

d = {}

for i in sentence1:
    if i.isalpha(): 
        d[i] = sentence1.count(i)

f = list(d)
print('Unique letters:',f)

