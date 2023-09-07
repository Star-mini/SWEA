a=input()

a=int(a)

b=list(map(int,input().split()))

b.sort()

if a %2 ==0 :
    print(b[(a//2)-1])
else:
    print(b[(a//2)])