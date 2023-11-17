n=int(input())

for i in range(1,n+1):
    cnt=0
    i=str(i)
    for j in i:
        if ( "3" in j or "6" in j or "9" in j):
            cnt=cnt+1

    if cnt >0 :
        for h in range( cnt ):
            print("-",end='')
    else:
        print(i,end='')
    print(' ',end='')