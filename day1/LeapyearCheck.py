def check(year):
    if(year%400==0 or (year%100!=0 and year%4==0)):
        return True
    else:
        return False
a=(int)(input("enter a year"))
print(f"The year is a leap year is {check(a)}")