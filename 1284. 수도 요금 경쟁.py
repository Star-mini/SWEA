T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    p,q,r,s,w=map(int,input().split())

    m=0
    m_a=p*w
    m_b=0

    if ( w-r > 0):
        m_b=q+(w-r)*s
    else:
        m_b=q

    if (m_a > m_b):
        m=m_b
    else:
        m=m_a

    print(f"#{test_case} {m}")