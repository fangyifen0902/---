a=(input("輸入值為:"))
b=a.split(",")
c=a.split(",")
d=""
e=""
if (len(b)<=7 and len(b)>=1) or (len(c)<=7 and len(c)>=1):
    b.sort()
    b.reverse()
    c.sort()
    for i in range(len(b)):
        d+=b[i]
    for i in range(len(c)):
        e+=c[i]
print("最大值數列與最小值數列差值為:",int(d)-int(e))