T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=list(map(int,input().split()))
    max_v=max(a)
    min_v=min(a)

    sum_v=sum(a)
    sum_v=sum_v-max_v-min_v
    sum_v=sum_v/8

    print(f"#{test_case} {round(sum_v)}")

'''
소수점 반올림
x = round(2.54, 1)

소수점 제거
int(a)

'''