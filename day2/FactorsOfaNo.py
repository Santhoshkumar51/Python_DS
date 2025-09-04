def factors(n):
    f=1
    while(f<n):
        if(n%f==0):
            print(f,end=" ")
        f+=1
n=(int)(input("enter n"))
factors(n)