num=int(input("Enter a number"))

position=1

while num>0:
    if num%2==1:
        print(f"Set bit at {position}")
        break
    num=num//2
    position=position+1

