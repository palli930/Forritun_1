month = input("Month: ")
date = input("Day: ")


firstL = date[0]
capital = firstL.upper()

if month == 'january' and date == '1':
    print(capital+date[1:],"=>","New year's day")
elif month == 'june' and date == '17':
    print(capital+date[1:],"=>","National holiday")
elif month =='december' and date == '25':
    print(capital+date[1:],"=>","Christmas day")
else:
    print("Not a holiday")

