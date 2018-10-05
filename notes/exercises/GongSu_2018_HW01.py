# coding: utf-8
import math

# # 공업수학_2018_HW1

# ``````````````````````````````````
#
#
#
#
# `````````````````````````````````

# # 문제 1.
# ## 자연수 `n`을 입력받아 `n!`을 리턴하는 함수 `factorial()`를 구현하라.
# ## ex) `factorial(3) = 6`

# ## [확인]
# ## 1. `factorial(6)`
# ## 2. `factorial(12)`
# ## 3. `factorial(15)`

# @@ 의견 : 재귀함수 이용 혹은 for 문 돌려서

def factorial(n):

    if(n == 0):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6)) # 720
print(factorial(12)) # 479001600
print(factorial(15)) # 1307674368000

# ``````````````````````````````````
#
#
#
#
# `````````````````````````````````

# # 문제 2.
# ## 문자열 `kebap`을 이용하여 문자열 `pkeba`을 생성하는 코드를 작성하라.

# @@ 의견 : 슬라이싱 붙이기

m = "kebap"
re_m = m[-1] + m[:-1]
print(re_m)
# ``````````````````````````````````
#
#
#
#
# `````````````````````````````````

# # 문제 3.
# ## 자연수 `n`이 주어였을 때, `n`이 소수인지 아닌지를 판별하는 함수 `is_PrimeNumber()`를 구현하라.
# ## ex) `is_PrimeNumber(3) = True`
# ## ex) `is_PrimeNumber(4) = False`

# ## [확인]
# ## 1. `is_PrimeNumber(167)`
# ## 2. `is_PrimeNumber(227)`
# ## 3. `is_PrimeNumber(303)`

# @@ 의견 :  n 이 될 때 까지 2 부터 1씩 증가시키면 나누어본다.
#           루트n 값이 될 때 까지 나누어 보면 시간 단축 (이유 : 1과 자신 외에 다른 수로 나누어 진다면 그 수와 짝이 되는 수가 존재하기 때문이다)

def is_PrimeNumber(n):
    isPrime = 'True'
    if n == 1 :
        isPrime = '1 is not a prime'
    else:
        for i in range(2, math.floor(math.sqrt(n) + 1)):
            if ((n % i) == 0):  # i로 나눈 나머지가 0 : 나누어 떨어짐
                isPrime = 'False'
                break

    print('is_PrimeNumber('+ str(n) +') = '+ isPrime)

is_PrimeNumber(167)  # True
is_PrimeNumber(227)  # True
is_PrimeNumber(303)  # False
is_PrimeNumber(2)    # True
is_PrimeNumber(1)    # False
is_PrimeNumber(991)  # True
is_PrimeNumber(978)  # False
# ``````````````````````````````````
#
#
#
#
# `````````````````````````````````

# # 문제 4.
# ## 다음은 KBS 기상 정보의 일부이다.
weather = "오늘은 해안을 중심으로 강한 바람이 불겠습니다. 현재 기온은 어제 이 시각보다 조금 높습니다. 한낮 기온은 광주 25도, 대전과 대구 24도, 서울 22도로 어제보다 1도에서 5도 가량 낮겠습니다. 제주 해상, 남해상, 동해상의 물결이 최고 2.5m로 비교적 높게 일겠습니다. 내일은 가을비 치고는 꽤 많은 양의 비가 내리겠습니다. 내일 전국에 비가 내리다가 오후에 대부분 그치겠습니다."

# ## (1) 위의 문자열에서 `비` 가 등장하는 횟수를 셈하는 코드를 작성하라.
# ## (2) 위의 문자열에서 광주와 서울의 한낮 기온을 찾고, 그 차를 구하는 코드를 작성하라.

# @@ 의견 :  == '비' 면 ++ , 한낮 기온 이후 처음 나오는 광주, 서울 뒤 숫자 저장후 차 출력

def count_bi(s):
    print(s.count('비'))

def find_temp(s):
    Gwangju_temp = s[s.find('광주')+3:s.find('광주')+5]
    Seoul_temp = s[s.find('서울')+3:s.find('서울')+5]

    print(abs(int(Gwangju_temp)-int(Seoul_temp))) # 절대값


count_bi(weather) # 4 개
find_temp(weather) # 3도 차이
# ``````````````````````````````````
#
#
#
#
# `````````````````````````````````

# # 문제 5.
# ## 몸무게, 키, 나이, 성별을 인자로 하여 기초대사율을 구하는 함수 `Bmr()`를 작성하라.
#
# ## 기초대사율(BMR)을 구하는 미플린 공식은 다음과 같다.
# ## P = (10 m + 6.25 h - 0.5 a + s)
# ## s는 남자의 경우 +5, 여자의 경우 -161
# ## 이때, P는 완전한 휴식 상태에서 총 열 생산량(kcal/day), m은 몸무게(kg), h는 키(cm), a는 나이(year), M 은 남자, F는 여자.

# ## [확인]
# ## 1. `Bmr(30, 120, 10, M)`
# ## 2. `Bmr(40, 140, 11, F)`
# ## 3. `Bmr(60, 160, 50, M)`

    # @@ 의견 : 따라서 잘 입력

def Bmr(m, h, a, mf):
    if mf == 'M':
        s = 5
    else:
        s = -161
    P = ((10 * m) + (6.25 * h) - (0.5 * a) + s)
    print(P)

Bmr(30, 120, 10, 'M')  # 1050.0
Bmr(40, 140, 11, 'F')  # 1108.5
Bmr(60, 160, 50, 'M')  # 1580.0

# ``````````````````````````````````
#
#
#
#
# `````````````````````````````````
