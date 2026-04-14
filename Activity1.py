def number(n):
    ones=0
    zeros=0

    #while the number is greater than zero check last digit and right shift
    while (n):
        if (n&1==1):
            ones=ones+1
        else:
            zeros=zeros+1
        n>>=1
    print(f"Number of zeros= {zeros} \n Number of ones={ones}")

num=int(input("Enter a number"))
number(num)