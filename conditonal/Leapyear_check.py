year = int(input("enter the year: "))

if year % 4 ==0 and year % 100 != 0:
    print("its a leap year")
elif year % 400 == 0:
    print("its also leap year")
else:
    print("its not leapyear")