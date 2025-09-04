def bill(t):
    if(t<=50):#6.30 7.50
        return t*3.80
    elif(t<=100):
        return (50*3.80)+(t-50)*4.20
    elif(t<=200):
        return (50*3.80)+50*4.20+(t-100)*5.10
    elif(t<=300):
        return (50*3.80)+50*4.20+100*5.10+(t-200)*6.30
    else:
        (50*3.80)+50*4.20+100*5.10+100*6.30+(t-300)*7.50
cno=(int)(input("enter consumer no"))
cname=input("enter consumer name")
pmr=(int)(input("enter present month reading"))
lmr=(int)(input("enter last month reading"))
total=pmr-lmr
print("bill =",bill(total))
print(f"reading = {total} bill = {bill}")