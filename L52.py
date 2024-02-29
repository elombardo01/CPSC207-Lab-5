#Emme and Mandy

def perfect(n):
    total=0
    for x in range(1,n):
        if n % x == 0:
            total= x+total
    if total == n:
        return True
    if total != n:
        return False






n = int(input("Give a number"))
x=1
while(x<n):
    result = perfect(x)
    if result == True:
        print(x)
    x=x+1



        
