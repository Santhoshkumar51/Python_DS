def check(c):
    if((c>='a' and c<='z') or (c>='A' and c<='Z')):
        return "Alphabet"
    elif(c>='0' and c<='9'):
        return "digit"
    else:
        return "special Character"
a=(input("enter a char"))
print("a is a ",check(a))