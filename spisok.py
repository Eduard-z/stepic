# put your python code here
lst = []
while 5:
    a = input().split()
    if a == ['end']:
        break
    b = [int(i) for i in a]
    lst.append(b)
print(lst)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j - len(lst) + 1] + lst[i][j - 1] + lst[i - 1][j] + lst[i - len(lst) + 1][j], end=' ')
    print('')
