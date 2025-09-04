def day(week):
    if(week==1):
        return "sunday"
    elif(week==2):
        return "monday"
    elif(week==3):
        return "tueday"
    elif(week==4):
        return "wednesday"
    elif(week==5):
        return "thursday"
    elif(week==6):
        return "friday"
    elif(week==7):
        return "saturday"
    else:
        print("invalid week no.")
a=(int)(input("enter week no."))
print("day=",day(a))