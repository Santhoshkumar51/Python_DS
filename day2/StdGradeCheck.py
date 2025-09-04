def grade(a):
    if(a<=50):
        return "c"
    elif(a>50 and a<=70):
        return 'b'
    elif(a>70 and a<=80):
        return 'a'
    else:
        return 's'
sno=(int)(input("enter std no"))
stdname=input("enter std name")
m1=(int)(input("enter sub1 marks"))
m2=(int)(input("enter sub2 marks"))
m3=(int)(input("enter sub3 marks"))
if(m1<40 and m2<40 and m3<40):
    print("fail")
else:
    total=m1+m2+m3
    avg=total/3
    print("grade is ",grade(avg))
