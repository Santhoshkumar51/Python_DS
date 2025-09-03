def check(a):
    if(a%5==0 and a%11==0):
        return True
    else:
        return False
a=(int)(input("enter a no."))
print(f"a is divisible by 5 and 11 is {check(a)}")