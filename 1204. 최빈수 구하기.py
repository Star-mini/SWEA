T = int(input())

for test_case in range(1, T + 1):
    #입력받기
    trash=input()
    a=list(map(int,input().split()))
    
    b={}

    for i in a:

        #없으면 딕셔너리에추가
        if i not in b:
            n=1
            b[i]=n
        #있으면 그 키의 횟수를 증가시킴
        else:
            b[i]+=1

    print(f"#{trash} {max(b,key=b.get)}")


'''
1.딕셔너리로 만들어서 숫자:횟수로 저장한다.
1-2.배열을 두개로 만든다.






ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
딕셔너리 키값에 여러가지 형태 가능
# 숫자를 키로 사용
b = {1: 'one', 2: 'two'}

# 튜플을 키로 사용
c = {(1, 2): 'coordinates', (3, 4): 'another coordinates'}

# 문자열을 키로 사용
d = {"apple": 1, "banana": 2}

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


최대 value에 대한 key 값 찾기
max(이름, key=이름.get)

'''