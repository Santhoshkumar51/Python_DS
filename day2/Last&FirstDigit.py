def digitsSum(n):
    l=n%10
    '''while(n>0):
        f=n%10
        n//=10'''
    s=(str)(n)
    f=n//(10**(len(s)-1))
    return f,l
n=(int)(input("enter n\n"))
print("factorial = ",digitsSum(n))