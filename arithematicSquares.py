ini = int(input("enter"))
lstOffinals = []
for x in range(ini):
    g00, g01, g02 = input("").split()
    g00 = int(g00) 
    g01 = int(g01) 
    g02 = int(g02) 
    g10 ,g12= input("").split()
    g10 = int(g10)
    g12 = int(g12)
    g20, g21, g22= input("").split()
    g20 = int(g20)
    g21 = int(g21)
    g22 = int(g22)
    lstOfCounters = []
    for y in range(1, 51):
        g11 = y
        counter = 0
        if(g01-g00 == g02-g01):
            counter +=1
        if(g11-g10 == g12-g11):
            counter +=1
        if(g21-g20 == g22-g21):
            counter +=1
        if(g11-g00 == g22-g11):
            counter +=1
        if(g11-g02 == g20-g11):
            counter +=1
        if(g10-g00 == g20-g10):
            counter +=1
        if(g12-g02 == g22-g12):
            counter +=1
        if(g11-g01 == g21-g11):
            counter+=1
        lstOfCounters.append([counter, x])
    counts = []
    for sols in lstOfCounters:
        counts.append(sols[0])

    num = max(counts)
    ind_max = counts.index(num)
    solx = lstOfCounters[ind_max]
    val = "Case #" + str(x) +" : " + str(solx[0])
    lstOffinals.append(val)
[print(x) for x in lstOffinals]