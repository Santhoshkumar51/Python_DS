#Simple intrest and total amount in hand
p=(int)(input("enter principle amount"))
r=(int)(input("enter rate of interest"))
t=(int)(input("enter time"))
si=(p*t*r)/100
print("simple interest=",si)
total_amount=p+si
print("total=",total_amount)