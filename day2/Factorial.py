def factorial(n):
    f=1
    while(n>=2):
        f*=n
        n-=1
    return f
n=(int)(input("enter n"))
print("factorial = ",factorial(n))