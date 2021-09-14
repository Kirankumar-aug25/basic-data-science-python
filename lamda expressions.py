###lambda is a anonymous fuction because no name,it will be having argument but it is single expression####
## normal fuction
## lambba functions are used for only one expression and n number of parameters or arguments
def add(x,y):

    result = x+y
    print(result)
add(25,30)
## vs lambda expression
## in this we have to use lambda key word ,finally we are combining fuction and atrribute in a same line .

result = lambda a,b:a+b
print(result(30,25))

####
y = lambda x : x

print(y(2))

##map
def even (x):
    if (x%2==0):
        print("even")
    else:
        print("odd")

list = [2,3,4,5,5,6,6,7,8,9,12,13,8,12]
for i in list:
    even(i)

    ######lambda function is used by map , filter
    ###syntax of map (function , iterable)
n = [2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 12, 13, 8, 12]
z = map(lambda x : (x%2==0), n)

for i in z:
    list(i)



