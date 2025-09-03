#
sno=(int)(input("enter std no"))
stdname=input("enter std name")
m1=(int)(input("enter sub1 marks"))
m2=(int)(input("enter sub2 marks"))
m3=(int)(input("enter sub3 marks"))
total=m1+m2+m3
avg=total/3
print("total marks =",total)
print("avg marks =",round(avg,2))