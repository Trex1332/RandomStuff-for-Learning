import datetime

# get input from user for a any date after the time they are using
def main():
    a = int(input("Day: "))
    b = int(input("Month: "))
    c = int(input("Year: "))
    y = datetime.datetime.now()
    if c < y.year:
        print("wrong")
        main()

    x = datetime.datetime(c,b,a)
    difference = daysBetween(x,y)
    print(f"{difference} days till {x.day,x.month,x.year}")

#see how many days between that day and now
def daysBetween(target,y):
    return ( target-y).days



#show the amount of days with the 



main()