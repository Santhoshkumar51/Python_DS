def check(a):
    if(a>='a' and a<='z'):
        return True
    else:
        return False
a=input("enter a char")
print(f"a is a alphabet is {check(a)}")