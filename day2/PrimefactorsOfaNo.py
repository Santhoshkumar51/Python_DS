def prime(n):
    f=2
    while(f<n):
        if(n%f==0):
            return False
        f+=1
    return True
def Primefactors(n):
    f=1
    while(f<n):
        if(n%f==0 and prime(f)):
            print(f,end=" ")
        f+=1
n=(int)(input("enter n"))
Primefactors(n)