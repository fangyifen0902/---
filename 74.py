a=['red','blue','red','green']
n=0
while n<=10:
    b=str(input("依序輸入四個顏色(中間以空白間隔)"))
    n+=1
    if n==10 and b!='red blue red green':
        print("挑戰失敗")
        break
    else:
        if b=='red blue red green':
            print("正確答案")
            break
        else:
            c=""
            d=b.split(" ")
            for i in range(0,4):
                if a[i]==d[i]:
                    c+="1"
                elif a[i]!=d[i] and a.count(d[i])>0:
                    c+="2"
                else:
                    c+="3"
            print(c)
