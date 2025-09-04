def palindrome(n):
    for i in range(2,n):
        s=(str)(i)
        if(s==s[::-1]):
            print(i,end=" ")
n=(int)(input("enter n"))
palindrome(n)