#####using for loop####
def factorial(n):
    k = 1
    if (n < 0):
        print("factorial of ", n, "=", 0)
    elif (n == 0 or n == 1):
        print("factorial of ", n, "=", 1)

    else:

        for i in range(n, 0, -1):
            k = k * i
    print(k)
factorial(9)
###using while loop##
def factorial(n):
    k = 1
    if (n < 0):
        print("factorial of ", n, "=", 0)
    elif (n == 0 or n == 1):
        print("factorial of ", n, "=", 1)

    else:

        while(n>1):
            k = k * n
            n=n-1
    print(k)
factorial(9)

