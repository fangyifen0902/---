n=int(input("整數n:"))
if n>0 and n<1000000:
    print("數列:",n,end=" ")
    for i in range(n):
        if n==1 :
            break
        elif (n%2==1):
            n=3*n+1
            print(int(n),end=" ")
        elif n%2==0:
            n=n/2
            print(int(n),end=" ")