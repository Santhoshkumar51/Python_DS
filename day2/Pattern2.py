def patt(r,c):
    for i in range(r):
        for j in range(c):
            if(i==j or i+j==r-1):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
patt(4,4)