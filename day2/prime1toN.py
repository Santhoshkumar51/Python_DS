def prime(n):
    for i in range(2,n):
        f=2
        while(f<i):
            if(i%f==0):
                break
            f+=1
        if(f==i):
            print(i,end=" ")
n=(int)(input("enter n"))
prime(n)