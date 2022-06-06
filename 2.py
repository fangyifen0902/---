a=int(input("請輸入度數"))
if a<120:
    b=a*2.1
    c=a*2.1
    print("summer months:,%.2f"%b)
    print("Non-summer months:,%.2f"%c)
elif a>120 and a<=330:
    b=a*3.02
    c=a*2.68
    print("summer months:,%.2f"%b)
    print("Non-summer months:%.2f"%c)
elif a>330 and a<=500:
    b=a*4.39
    c=a*3.61
    print("summer months:%.2f"%b)
    print("Non-summer months:%.2f"%c)
elif a>500 and a<=700:
    b=a*4.97
    c=a*4.01
    print("summer months:%.2f"%b)
    print("Non-summer months:%.2f"%c)
else:
    b=a*5.63
    c=a*4.5
    print("summer months:%.2f"%b)
    print("Non-summer months:%.2f"%c)