g = input("enter the total gold bars ")
g = int(g)
answer = []
for x in range(1, g+1):
    lst = []
    defaulter = x
    for y in range(1, 1000000000000):
        lst.append(defaulter)
        if(sum(lst)==g):
            answer.append(x)
            break
        else:
            pass
        if(sum(lst)<g):
            defaulter = defaulter+1
        else:
            break

for x in range(len(answer)):
    print("Case #" + str(x+1)+":", answer[x])