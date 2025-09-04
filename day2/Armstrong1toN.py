def Armstrong(n):
    for i in range(1,n):
        c=i
        f=0
        while(i>0):
            f+=(i%10)**3
            i//=10
        if(c==f):
            print(c,end=" ")
n=(int)(input("enter n"))
Armstrong(n)