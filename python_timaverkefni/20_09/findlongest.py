with open("words.txt", "r") as f:
    listi = list(f)
    h = [len(i) for i in listi]

longest = max(listi, key=len)
longstrp = longest.strip("\n")

x = 0
for u in h:
    if u > x:
        x = u

print("Longest word is {} of lenght {}".format(longstrp,(x-1)))

   
