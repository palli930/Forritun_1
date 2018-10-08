
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
        print("{:<33}{:<33}{:<21}".format("Indicator","Min","Max"))
        print("".center(87,"-"))
        quit()
    return lines

#Safnar saman voldum elements ur lista og byr til nyjan lista.
#Tekur tvo arguments, nafn a lista og index numer a staki. 
def extract_data(listi,x):
    values = []
    for j in listi:
        values.append(j[x])
    return values

#Tekur inn lista sem argument og returna max og min value.
#Hunsar fyrsta stakid tar sem tad inniheldur nafnid a breytunni
def max_min(listi):
    x = []
    for j in listi[1:]:
        x.append(float(j))
    vmax = max(x)
    vmin = min(x)
    return vmax, vmin

#Finnur hvaða fylki hafa min og max gildi
#returnar vidkomandi fylki asamt max og min values
def fylki_max_min(listi,linur):
    vmax,vmin = max_min(listi)
    fylki = extract_data(linur,0)
    try:
        index_max = listi.index(str(vmax))
        index_min = listi.index(str(vmin))
    except:
        index_max = listi.index(str(vmax)+"0")
        index_min = listi.index(str(vmin)+"0")
    fylki_max = fylki[index_max]
    fylki_min = fylki[index_min]
    return fylki_min, vmin, fylki_max, vmax, 


filename = input("Enter filename containing csv data: ")

linur = get_lines(filename)

#Hearth disease death rate
hddr = extract_data(linur,1)
#Motor vehicle death rate
mvdr = extract_data(linur,5)
#Teen Birth Rate
tbr = extract_data(linur,7)
#Adult smoking
As = extract_data(linur,11)
#Adult obesity
ao = extract_data(linur,13)

min_hddr_f,hddr_min,max_hddr_f,hddr_max = fylki_max_min(hddr,linur)
min_mvdr_f,mvdr_min,max_mvdr_f,mvdr_max = fylki_max_min(mvdr,linur)
min_tbr_f,tbr_min,max_tbr_f,tbr_max = fylki_max_min(tbr,linur)
min_As_f,As_min,max_As_f,As_max = fylki_max_min(As,linur)
min_ao_f,ao_min,max_ao_f,ao_max = fylki_max_min(ao,linur)

print("{:<33}{:<33}{:<21}".format("Indicator","Min","Max"))
print("".center(87,"-"))
print("{:<33}{:<21}{:6}{:>6}{:<15}{:>6}".format(hddr[0]+":",min_hddr_f,hddr_min,"",max_hddr_f,hddr_max))
print("{:<33}{:<21}{:6}{:>6}{:<15}{:>6}".format(mvdr[0]+":",min_mvdr_f,mvdr_min,"",max_mvdr_f,mvdr_max))
print("{:<33}{:<21}{:6}{:>6}{:<15}{:>6}".format(tbr[0]+":",min_tbr_f,tbr_min,"",max_tbr_f,tbr_max))
print("{:<33}{:<21}{:6}{:>6}{:<15}{:>6}".format(As[0]+":",min_As_f,As_min,"",max_As_f,As_max))
print("{:<33}{:<21}{:6}{:>6}{:<15}{:>6}".format(ao[0]+":",min_ao_f,ao_min,"",max_ao_f,ao_max))






