def Distanceconvertion(km):
    return km*0.621
km=(int)(input("enter distance in kilometers\n"))
print("Distance in miles =",Distanceconvertion(km))
def DaysConvertion(days):
    months=(int)(days/30);
    years=(int)(days/365)# months/12
    return months,years
d=(int)(input("enter no.of days"))
a,b=DaysConvertion(d);
print(f"months={a} years={b}")