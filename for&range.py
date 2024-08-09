# for와 range 사용하기
 # for 반복문은 다양하게 사용할 수 있음. range와 사용하면 반복 횟수를 지정할 수 있음
 # for 변수 in range(횟수):
 #      반복할 코드
  # for 다음 줄에 오는 코드는 반드시 들여쓰기를 해야함(규칙은 if, elif, else와 같음)
for i in range(100):
    print('Hello, world!')
 # for 반복문은 반복 횟수가 정해져 있을 때 주로 사용 (루프)

 # 반복문에서 변수의 변화 확인하기
for i in range(100):
    print('Hello, world!', i)

 # 시작하는 숫자와 끝나는 숫자 지정
  # for 변수 in range(시작, 끝):
for i in range(5, 12):      # 5부터 11가지 반복
    print('Hello, World!', i)
 # 증가폭 사용
  # for 변수 in range(시작, 끝, 증가폭):
for i in range(0, 10, 2):       # 0부터 8까지 2씩 증가
    print('Hello, world!', i)
 # 숫자 감소
for i in range(10, 0, -1):       # range(10, 0)은 동작하지 않음.(기본 증가폭 값이 양수 1임) 반드시 증가폭 -1을 지정해줘야 함.
    print('Hello, world!', i)
  # 증가폭을 음수로 지정하는 방법 말고 reversed를 사용하면 숫자의 순서를 반대로 뒤집음
   # for 변수 in reversed(range(횟수))
   # for 변수 in reversed(range(시작, 끝))
   # for 변수 in reversed(range(시작, 끝, 증가폭))
for i in reversed(range(10)):   # range에 reversed를 사용하여 숫자의 순서를 반대로 뒤집음
    print('Hello, world!', i)   # 9부터 0까지 10번 반복 -> range(10)으로 0부터 9까지 숫자를 생성한 후 reversed를 사용하여 숫자를 뒤집었기 때문

 # 입력한 횟수대로 반복
count = int(input('반복할 횟수를 입력하세요: '))    # input으로 입력 값을 int로 정수로 변환하여 count 변수에 저장
for i in range(count):
    print('Hello, world!', i)

 # 시퀀스 객체 반복하기
  # for 은 리스트, 튜플, 문자열 등 시퀀스 객체로 반복할 수 있음
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':         # for에 문자열을 지정하면 문자를 하나씩 꺼내서 반복
    print(letter, end=' ')      # 문자열 'Python' 의 문자가 하나씩 분리되어 출력, print에 end=' '을 지정했으므로 공백으로 띄워져서 출력

for letter in reversed('Python'):       # reversed를 사용하여 문자열을 뒤집기
    print(letter, end=' ')

# 연습문제 : 리스트의 요소에 10을 곱해서 출력하기
 # 다음 소스 코드를 완성하여 리스트 x에 들어있는 각 숫자(요소)에 10을 곱한 값이 출력되게 만드세요. 
 # 모든 숫자는 공백으로 구분하여 한 줄로 출력되어야 합니다.

x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10, end=' ')
