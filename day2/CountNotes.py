def count(a):
    c=0
    c+=a//2000
    a%=2000
    c+=a//500
    a%=500
    c+=a//200
    a%=200
    c+=a//50
    a%=50
    c+=a//10
    a%=10
    c+=a//2
    a%=2
    c+=a//1
    a%=1
    return c
a=(int)(input("enter amount"))
print("count=",count(a))
