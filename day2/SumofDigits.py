def digitsSum(n):
    f=0
    while(n>0):
        f+=n%10
        n//=10
    return f
n=(int)(input("enter n\n"))
print("factorial = ",digitsSum(n))