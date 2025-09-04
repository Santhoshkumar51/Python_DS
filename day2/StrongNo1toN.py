def factorial(n):
    f=1
    while(n>=2):
        f*=n
        n-=1
    return f
def Strong(n):
    for i in range(1,n):
        c=i
        f=0
        while(i>0):
            f+=factorial(i%10)
            i//=10
        if(c==f):
            print(c,end=" ")
n=(int)(input("enter n"))
Strong(n)