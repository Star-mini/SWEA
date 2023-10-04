t=int(input())

for i in range(1,t+1):
    n=int(input())

    a=0
    b=0
    c=0
    d=0
    e=0

    while n%2 ==0 :
        a=a+1
        n=n/2
    while n%3 ==0 :
        b=b+1
        n=n/3
    while n%5 ==0 :
        c=c+1
        n=n/5
    while n%7 ==0 :
        d=d+1
        n=n/7
    while n%11 ==0 :
        e=e+1
        n=n/11

    print(f"#{i} {a} {b} {c} {d} {e}")
