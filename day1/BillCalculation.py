#calculating reading and bill
cno=(int)(input("enter consumer no"))
cname=input("enter consumer name")
pmr=(int)(input("enter present month reading"))
lmr=(int)(input("enter last month reading"))
total=pmr-lmr
bill=total*3.80
'''print("total reading =",total)
print("bill =",round(bill,2))'''
print(f"reading = {total} bill = {bill}")