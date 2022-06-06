b=["a","e","i","o","u"]
a1=""
a=(input("請輸入一串小寫英文:"))
for i in a:
    if i in b:
        a1=a1+"."
    else:
        a1=a1+i
print(a1)