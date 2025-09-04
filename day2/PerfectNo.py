def perfect(n):
    c=0
    f=1
    while(f<n):
        if(n%f==0):
            c+=f
        f+=1
    if(c==n):
        return True
    return False
n=(int)(input("enter n"))
print("n is a perfect no. is  ",perfect(n))