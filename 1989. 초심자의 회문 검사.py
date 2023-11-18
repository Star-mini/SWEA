T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=input()
    a=a.strip()
    a_l=len(a)
    b=a[a_l-1::-1]

    if a==b :
        print(f"#{test_case} 1")
    else:

        print(f"#{test_case} 0")




'''
바꾸기
복사하기

'''