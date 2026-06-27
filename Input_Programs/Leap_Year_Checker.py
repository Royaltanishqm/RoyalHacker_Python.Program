LP=int(input("Enter the year: "))
if LP%4==0:
    if LP%100==0:
        if LP%400==0:
            print(LP,"is a leap year.")
        else:
            print(LP,"is not a leap year.")
    else:
        print(LP,"is a leap year.")
else:
    print(LP,"is not a leap year.")