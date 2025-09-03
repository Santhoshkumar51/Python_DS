def check(a):
    a1=['a','e','i','o','u','A','E','I','O','U']
    if(a in a1):
        return True
    else:
        return False
a=input("enter a character")
print(f"a is a vowel is {check(a)}")