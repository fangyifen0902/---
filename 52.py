a='紅豆生南國春來發幾枝勸君多采擷此物最相思'
b='春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少'
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)