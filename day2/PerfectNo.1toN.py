def perfect(n):
    for i in range(1,n):
        c=i
        p=0
        f=1
        while(f<i):
            if(i%f==0):
                p+=f
            f+=1
        if(c==p):
            print(c,end=" ")
n=(int)(input("enter n"))
perfect(n)