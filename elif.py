# elif 사용하기
 # elif는 조건식을 여러 개 지정하여 각 조건 마다 다른 코드를 실행할 수 있음
 # if 조건식:
 #      코드1
 # elif 조건식:
 #      코드2 ...
x = 20
if x == 10:              # 우선 if에서 10인지 검사
    print('10입니다.')   # if 식이 참이면 출력, 아닐 경우 elif로 넘어감
elif x == 20:           # elif 20인지 검사
    print('20입니다.')   # elif가 참이면 출력
 # if, elif, else 모두 사용
  # if 조건식:
  #     코드1
  # elif 조건식:
  #     코드2
  # else:
  #     코드3
x = 30
if x == 10:         # x가 10일때
    print('10입니다.')
elif x == 20:       # x가 20일때
    print('20입니다.')
else:               # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')
    
 # if와 else는 한번만 사용이 가능하지만, elif는 여러번 가능
button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

#연습문제
 # 다음 소스 코드를 완성하여 변수 x가 11과 20 사이면 '11~20', 21과 30 사이면 '21~30', 아무것도 해당하지 않으면 '아무것도 해당하지 않음'이 출력되게 만드세요.

x = int(input())

if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')
