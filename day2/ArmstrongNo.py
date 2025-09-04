def Armstrong(n):
    c=n
    f=0
    while(n>0):
        f+=(n%10)**3
        n//=10
    if(c==f):
        return True
    return False
n=(int)(input("enter n\n"))
print("n is a armstrong is ",Armstrong(n))