# else를 사용하여 두 방향으로 분기
 # if 조건식:
 #    코드1
 # else:
 #    코드2
x = 5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')
 # 변수에 값 할당을 if, else로 축약하기
x = 5
if x == 10:
    y = x
else:
    y = 0
print(y)
  # if, else에서 변수에 값을 할당할 때는 "변수 = 값 if 조건문 else 값" 형식으로 축약 가능(조건부 표현식, conditional expression)
x = 5
y = x if x == 10 else 0
print(y)
 # else는 if와 들여쓰기 규칙이 같음.
x = 5

if x == 10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')

x = 10
if x == 10: # x가 10이라 조건식이 참이면
    print('10입니다.')  # 출력
else:
    print('x에 들어있는 숫자는') # x가 10이라는 조건식이 거짓이면 출력
print('10이 아닙니다.') # 출력되지 않아야 하는데 출력됨 (else도 같은 들여쓰기여야 함)

 # if 조건문의 동작 방식
if True:
    print('참') # True는 참
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓') # False는 거짓

if None:
    print('참')
else:
    print('거짓') # None은 거짓
 # True는 if의 코드가 실행, False는 거짓의 코드가 실행되며, None은 False로 취급되므로 else의 코드가 실행
 # if 조건문에 숫자 지정
  # 숫자는 정수(2진수, 10진수, 16진수), 실수와 관게없이 0이면 거짓, 0이 아닌 수는 참
if 0:
    print('참')
else:
    print('거짓') # 0은 거짓
if 1:
    print('참') # 1은 참
else:
    print('거짓')

if 0x1F: # 16진수
    print('참') # 0x1F는 참
else:
    print('거짓')

if 0b1000: # 2진수
    print('참') # 0b1000은 참
else:
    print('거짓')

if 13.5: # 실수
    print('참') # 13.5는 참
else:
    print('거짓')
 # if 조건문에 문자열 지정
  # 문자열은 내용이 있을 때 참, 없을 때 거짓
if 'Hello': #문자열
    print('참') # 문자열이 있으면 참
else:
    print('거짓')
if '': # 빈 문자열
    print('참')
else:
    print('거짓') # 빈 문자열은 거짓
 # 0, None, 빈 문자열을 not으로 뒤집을 경우 True가 되므로 if를 동작시킬 수 있음
if not 0:
    print('참') # not 0은 참
else:
    print('거짓')
if not None:
    print('참') # not None은 참
else:
    print('거짓')
if not '':
    print('참') # not 빈 문자열은 참
else:
    print('거짓')

 # 조건식을 여러 개 지정하기
  # if 조건문에는 논리 연산자를 사용하여 조건식을 여러 개 지정할 수 있음
x = 10
y = 20
if x == 10 and y == 20:  # x가 10이면서 y가 20일 경우
    print('참')
else:
    print('거짓')
 # 중첩 if 조건문과 논리 연산자
  # 보통 여러 조건을 판단할 때 if를 게속 나열해서 중첩 if 조건문으로 만드는 경우가 많음.
if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다')
if x > 0 and x < 20:
    print('20보다 작은 양수입니다.') # 위 중첩 if조건문을 논리 연산자로 묶음.
if 0 < x < 20:
    print('20보다 작은 양수입니다.') # and 논리 연산자를 사용하지 않고 부등호를 사용하여 축약

# 연습문제
 # A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서 코딩 시험을 통과해야 합격이라고 정했습니다(코딩 시험 통과 여부는 True, False로 구분).
 # 다음 소스 코드를 완성하여 '합격', '불합격'이 출력되게 만드세요.
written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')
 