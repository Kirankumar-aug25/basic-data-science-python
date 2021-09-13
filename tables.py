n = int(input(" enter the end value of table u want "))
for i in range (1,n):
    for j in range(1,20):
        print(i,"*",j,"=",end=" ")
        print(i*j)