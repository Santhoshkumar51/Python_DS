def check(a,b,c):
    if(a>b):
        if(a>c):
            print("a is max")
        else:
            if(b>c):
                print("b is max")
    else:
        if(b>c):
            print("b is max")
        else:
            print("c is max")
a=(int)(input("enter a first no."))
b=(int)(input("enter a second no."))
c=(int)(input("enter a third no."))
check(a,b,c)