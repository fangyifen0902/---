m=int(input("請輸入一正整數(<10):"))
n=0
for i in range(1,m+1):
    for j in range(1,i+1):
        c=i*j
        print("%4d"%(c),end="")
    print()