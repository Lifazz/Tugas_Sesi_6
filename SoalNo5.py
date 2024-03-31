
a = 5
b = 5

for i in range(a,0,-1):
    for f in range(1,b +1):
        if f < i:
            print("_",end =" ")

        else:
            print(f,end =" ")

    print()
