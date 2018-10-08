def shares_digits():
    shares = input("Enter number of shares: ")
    while shares.isdigit() == False:
        try:
            shares/1
        except:
            print("Invalid number!")
            shares = input("Enter number of shares: ")
    return int(shares)

def price_digits():
    price = input("Enter price (dollars, numerator, denominator): ")
    dollars, num, denom = price.split(' ')
    while dollars.isdigit() == False or num.isdigit() == False or denom.isdigit()== False:
        try:
            dollars/1
            num/1
            denom/1
        except:
            print("Invalid price!")
            price = input("Enter price (dollars, numerator, denominator): ")
            dollars, num, denom = price.split(' ')
    return int(dollars), int(num), int(denom)

def price_f(s, p, n, d):
    price = s * (p + (n/d))
    return float(price)

c = 'y'

while c == 'y' or c == 'Y':
    s = shares_digits()
    p, n, d = price_digits()
    price = price_f(s, p, n, d)
    print("{} shares with market price {} {}/{} have value ${:0.2f}".format(s,p,n,d,price))
    c = input("Continue: ")






