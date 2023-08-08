
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=input().split()

    #정수화 하기
    for i in range(10):
        a[i]=int(a[i])
        
    s=0

    #홀수만 더하는 작업

    for i in range(10):
        if a[i] % 2 != 0 :
            s=s+a[i]
            
    print('#%d %d'%(test_case,s))