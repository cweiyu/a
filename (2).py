num = eval(input())
alist = list()
for x in range(1,num+1):
    if x%3 != 0 and x%5 != 0:
        alist.append(x)
    if x%3 == 0 and x%6 == 0:
        alist.append(x)
print(len(alist))
