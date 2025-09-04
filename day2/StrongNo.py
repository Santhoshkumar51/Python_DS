def factorial(n):
    f=1
    while(n>=2):
        f*=n
        n-=1
    return f
def Strong(n):
    c=n
    f=0
    while(n>0):
        f+=factorial(n%10)
        n//=10
    if(c==f):
        return True
    return False
n=(int)(input("enter n\n"))
print("n is a armstrong is ",Strong(n))