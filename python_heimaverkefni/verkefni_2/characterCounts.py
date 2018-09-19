setning = input("Enter a sentence: ")

lower = 0
upper = 0
digits = 0
punct = 0

for x in setning:
    if x.islower():
        lower += 1

for y in setning:
    if y.isupper():
        upper += 1

for z in setning:
    if z.isdigit():
        digits += 1

for q in setning:
    if q.count('.'):
        punct += 1
    if q.count(','):
        punct += 1
    if q.count('-'):
        punct += 1
    if q.count('?'):
        punct += 1
    if q.count('!'):
        punct += 1
    if q.count('"'):
        punct += 1
    if q.count("'"):
        punct += 1
print('{:>15}'.format('Upper case')+'{:>5}'.format(upper))
print('{:>15}'.format('Lower case')+'{:>5}'.format(lower))
print('{:>15}'.format('Digits')+'{:>5}'.format(digits))
print('{:>15}'.format('Punctuation')+'{:>5}'.format(punct))

