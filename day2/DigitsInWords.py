def word(a):
    if(a==0):
        return "zero"
    elif(a==1):
        return "one"
    elif(a==2):
        return "two"
    elif(a==3):
        return "three"
    elif(a==4):
        return "four"
    elif(a==5):
        return "five"
    elif(a==6):
        return "six"
    elif(a==7):
        return "seven"
    elif(a==8):
        return "eight"
    elif(a==9):
        return "nine"
    
def digits(n):
    f=0
    while(n>0):
        f=n%10
        print(word(f))
        n//=10
 
n=(int)(input("enter n\n"))
digits(n)