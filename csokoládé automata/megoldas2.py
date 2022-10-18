f = open("be1.txt", "r")

osszeg,N = list(map(int, f.readline().split(" ")))
ermek=list(map(int, f.readline().split(" ")))

fizethet=[]
m=N
for i in range(N):
    for j in range(i,N):
        fizethet.append(ermek[j-1])
        s=sum(fizethet)
        if s>osszeg:
            fizethet.pop(j-1)
        if s==osszeg:
            k=len(fizethet)
            if k<m:
                m=k
            print(fizethet)
    fizethet.clear()
    s=0
#if k=0:
    #print("Nem lehet kifizetni")
