def digit(n):
    x = n % 10
    y = int(n / 10)
    if y < 10:
       if x**3+ y**3 == n:
           print("arm strong number")
       else:
           print("not an armstrong number")

    else:
        z = y % 10
        a = int(y / 10)
        if x**3 + z**3 + a**3== n:
            print("arm strong number")
        else:
            print("not an armstrong number")
digit(153)