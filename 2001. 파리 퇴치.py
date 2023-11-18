n,m=map(int,input().split())

a=[]

#입력받기
for i in range(n):
    a.append(list(map(int,input().split())))

s=0
s_s=0
#최댓값 체크하기
for i in range(n-m+1):
    for j in range(n-m+1):
        #더하기 작업
        for h in range(n):
            s_s=s_s+a[i][j+n]
        if s>=s_s:
            s=s
        else:
            s=s_s
print(s)
        
