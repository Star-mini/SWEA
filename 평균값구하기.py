
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=input().split()
    for i in range(10):
        a[i]=int(a[i])
    b=sum(a)/10
    print('#%d %d'%(test_case,round(b)))

#round, sum사용