
#Les inn linur ur skra og byr til lista af listum. 
#Tekur eitt argument, nafn a skra.
def get_lines(filename):
    try:
        dataFile = open(filename,"r")
        lines = []
        for i in dataFile:
            lines.append(i.replace("%","").split(','))
    except:
        lines = ""
        print("Cannot find file "+filename)
    return lines

#safnar saman voldum elements ur lista.
#Tekur tvo arguments, nafn a lista og index numer a staki. 
def extract_data(list,x):

filename = input("Enter filename containing csv data: ")

linur = get_lines(filename)
print(linur)