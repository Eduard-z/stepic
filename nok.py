# put your python code here
a = int(input())
b = int(input())

if a == b:
    d = a
else:
    if a>b:
        maxx = a
        minn = b
    elif a<b:
        maxx = b
        minn = a
    while maxx%minn != 0:
        ostatok = maxx%minn
        maxx = minn
        minn = ostatok
    else:
        nod = minn
    d = a*b/nod
print(d)