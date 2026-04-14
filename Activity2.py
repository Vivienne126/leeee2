def setornot(number,n):
    if number&(1<<(n-1)):
        print("SET")
    else:
        print("Not a set")

number=int(input("Enter the number"))
n=int(input("Enter the bit number"))
setornot(number , n)