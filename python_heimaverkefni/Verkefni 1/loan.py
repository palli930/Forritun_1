HS = int(input("Input the cost of the item in $: "))

HV= 0
m = 0

if HS <= 1000:
    while HS >=0:
        if HS > 50:
            m += 1
            vextir = HS * 0.015
            g = 50.0
            HS = (HS -g) + vextir
            print('Month:',m,'Payment:',round(g,2),'Interest paid:',round(vextir,2),'Remaining debt:',round(HS,2))
            HV += vextir
        else:
            m += 1
            vextir = HS * 0.015
            g = HS  + vextir
            HS = (HS -g) 
            print('Month:',m,'Payment:',round(g,2),'Interest paid:',round(vextir,2),'Remaining debt:',round((HS - HS),2))
            HV += vextir
    print()   
    print('Number of months:',m) 
    print('Total interest paid:',round(HV,2))
else:
    while HS >=0:
        if HS > 50:
            m += 1
            vextir = HS * 0.02
            g = 50.0 
            HS = (HS -g) + vextir
            print('Month:',m,'Payment:',round(g,2),'Interest paid:',round(vextir,2),'Remaining debt:',round(HS,2))
            HV += vextir
        else:
            m += 1
            vextir = HS * 0.02
            g = HS  + vextir
            HS = (HS -g) 
            print('Month:',m,'Payment:',round(g,2),'Interest paid:',round(vextir,2),'Remaining debt:',round((HS - HS),2))
            HV += vextir
    print()       
    print('Number of months:',m) 
    print('Total interest paid:',round(HV,2))



