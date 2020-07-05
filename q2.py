def leap(year):
    return (year%400 ==0 or (year % 4 ==0 and year %100 !=0))

year = int(input("Enter the year: "))
isLeap = leap(year)

if isLeap:
    print(f" {year} is Leap year")
else:
    print(f" {year} is not Leap year")


    
