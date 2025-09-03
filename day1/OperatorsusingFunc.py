def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def division(a,b):
    return a/b
def remainder(a,b):
    return a%b
def exponent(a,b):
    return a**b
def floorDivison(a,b):
    return a//b
a=(int)(input("enter first no."))
b=(int)(input("enter second no."))
print(f"sum={add(a,b)}\ndifference={subtract(a,b)}\nproduct={mul(a,b)}\nquotient={division(a,b)}\nrem={remainder(a,b)}\nfloorQuotient={floorDivison(a,b)}\na power of b = {exponent(a,b)}")