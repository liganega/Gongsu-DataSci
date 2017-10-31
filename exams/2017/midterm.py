
# coding: utf-8

# In[39]:

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


# In[8]:

get_ipython().magic(u'matplotlib inline')


# ## 파이썬 기본 자료형

# ### 문제 
# 
# 실수(부동소수점)를 하나 입력받아, 그 숫자를 반지름으로 하는 원의 면적과 둘레의 길이를 튜플로 리턴하는 함수 `circle_radius`를 구현하는 코드를 작성하라,

# ```
# 
# .
# ```

# ## 문자열 자료형

# 아래 사이트는 커피 콩의 현재 시세를 보여준다.
# 
#     http://beans-r-us.appspot.com/prices.html
# 
# 위 사이트의 내용을 html 소스코드로 보면 다음과 같으며, 검색된 시간의 커피콩의 가격은 
# `Current price of coffee beans` 문장이 담겨 있는 줄에 명시되어 있다.
# 
# ```html
# <html><head><title>Welcome to the Beans'R'Us Pricing Page</title>
# <link rel="stylesheet" type="text/css" href="beansrus.css" />
# </head><body>
# <h2>Welcome to the Beans'R'Us Pricing Page</h2>
# <p>Current price of coffee beans = <strong>$5.94</strong></p>
# <p>Price valid for 15 minutes from Sun Sep 10 12:21:58 2017.</p>
# </body></html>
# ```

# ### 문제
# 
# 아래 코드가 하는 일을 설명하라.
# ```
# from __future__ import print_function
# 
# import urllib2
# import time
# 
# def price_setter(b_price, a_price):
#     bean_price = b_price
#     while 5.5 < bean_price < 6.0:
#         time.sleep(1)
# 
#         page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html")
#         text = page.read().decode("utf8")
# 
#         price_index = text.find(">$") + 2
#         bean_price_str = text[price_index : price_index + 4]
#         bean_price = float(bean_price_str)
#         
#     print("현재 커피콩 가격이", bean_price, "달러 입니다.")
# 
#     if bean_price <= 5.5:
#         print("아메리카노 가격을", a_price, "달러만큼 인하하세요!")
#     else:
#         print("아메리카노 가격을", a_price, "달러만큼 인상하세요!")
# ```

# ## 오류 및 예외 처리

# ### 아래 코드가 하는 일을 설명하라.
# 
# ```
# number_to_square = raw_input("A number to divide 100: ")
# 
# try: 
#     number = float(number_to_square)
#     print("100을 입력한 값으로 나눈 결과는", 100/number, "입니다.")
# except ZeroDivisionError:
#     raise ZeroDivisionError('0이 아닌 숫자를 입력하세요.')
# except ValueError:
#     raise ValueError('숫자를 입력하세요.')    
# ```

# ## 리스트

# ### 문제 
# 
# 아래 설명 중에서 리스트 자료형의 성질에 해당하는 항목을 모두 골라라.
# 
# 1. 가변 자료형이다.
# * 불변 자료형이다.
# * 인덱스와 슬라이싱을 활용하여 항목의 내용을 확인하고 활용할 수 있다.
# * 항목들이 임의의 자료형을 가질 수 있다.
# * 리스트 길이에 제한이 있다.
# * 신성정보 등 중요한 데이터를 보관할 때 사용한다.

# ```
# 
# ```

# 견본답안: 1, 3, 4

# ## 사전

# ## 오늘의 주요 예제
# 
# `record_list.txt` 파일은 여덟 명의 수영 선수의 50m 기록을 담고 있다.
# 
# ```txt
# player1 21.09 
# player2 20.32 
# player3 21.81 
# player4 22.97 
# player5 23.29 
# player6 22.09 
# player7 21.20 
# player8 22.16
# ```

# ### 문제
# 
# 아래코드가 하는 일을 설명하라.
# 
# ```python
# from __future__ import print_function
# 
# record_f = open("record_list.txt", 'r')
# record = record_f.read().decode('utf8').split('\n')
# 
# record_dict = {}
# 
# for line in record:
#     (player, p_record) = line.split()
#     record_dict[p_record] = player
# 
# record_f.close()
# 
# record_list = record_dict.keys()
# record_list.sort()
# 
# for i in range(3):
#     item = record_list[i]
#     print(str(i+1) + ":", record_dict[item], item)
# ```    

# ## 튜플

# ### 문제 
# 
# 아래 설명 중에서 튜플 자료형의 성질에 해당하는 항목을 모두 골라라.
# 
# 1. 가변 자료형이다.
# * 불변 자료형이다.
# * 인덱스와 슬라이싱을 활용하여 항목의 내용을 확인하고 활용할 수 있다.
# * 항목들이 임의의 자료형을 가질 수 있다.
# * 튜플 길이에 제한이 있다.
# * 신성정보 등 중요한 데이터를 보관할 때 사용한다.

# ```
# 
# ```

# 견본답안: 2, 3, 4, 6

# ## 리스트 조건제시법

# 아래 코드는 0부터 1000 사이의 홀수들의 제곱의 리스트를 조건제시법으로 생성한다

# In[75]:

odd_1000 = [x**2 for x in range(0, 1000) if x % 2 == 1]

# 리스트의 처음 다섯 개 항목
odd_1000[:5]


# ### 문제
# 
# 0부터 1000까지의 숫자들 중에서 홀수이면서 7의 배수인 숫자들의 리스트를 조건제시법으로 생성하는 코드를 작성하라.

# ```
# 
# 
# 
# .
# ```

# 모범답안:

# In[84]:

odd_3x7 = [x for x in range(0, 1000) if x % 2 == 1 and x % 7 == 0]

# 리스트의 처음 다섯 개 항목
odd_3x7[:5]


# ### 문제
# 
# 0부터 1000까지의 숫자들 중에서 홀수이면서 7의 배수인 숫자들을 제곱하여 1을 더한 값들의 리스트를 조건제시법으로 생성하는 코드를 작성하라.
# 힌트: 아래와 같이 정의된 함수를 활용한다.
# 
# $$f(x) = x^2 + 1$$

# In[86]:

def square_plus1(x):
    return x**2 + 1

odd_3x7_spl = [square_plus1(x) for x in odd_3x7]
# 리스트의 처음 다섯 개 항목
odd_3x7_spl[:5]


# ### 문제
# 
# 0부터 1000까지의 숫자들 중에서 홀수이면서 3의 배수인 숫자들의 리스트를 조건제시법으로 생성하는 코드를 작성하라.
# 
# 
# ```
# def f(x):
#     return x**2 + 1
# ``` 
# 
# 
# 
# 

# ## csv 파일 읽어들이기

# 위 도표의 데이터는 `'Seoul_pop2.csv'` 파일에 아래와 같이 저장되어 있다.

# In[55]:

get_ipython().system(u'cat Seoul_pop2.csv')

# 윈도우의 경우:
# !type Seoul_pop2.csv


# 확장자가 csv인 파일은 데이터를 저장하기 위해 주로 사용한다. 
# csv는 Comma-Separated Values의 줄임말로 데이터가 쉼표(콤마)로 구분되어 정리되어 있는 파일을 의미한다. 
# 
# csv 파일을 읽어드리는 방법은 `csv` 모듈의 `reader()` 함수를 활용하면 매우 쉽다.

# In[56]:

import csv

with open('Seoul_pop2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0 or row[0][0] == '#':
            continue
        else:
            print(row)


# ### 문제
# 
# 위 코드에서 5번 째 줄을 아래와 같이 하면 오류 발생한다.
# ```
# if row[0][0] == '#' or len(row) == 0:
# ```
# 이유를 간단하게 설명하라.

# ```
# 
# 
# 
# .
# ```

# ## 넘파이 활용 기초 1

# 넘파이 어레이를 생성하는 방법은 몇 개의 기본적인 함수를 이용하면 된다.
# 
# * `np.arange()`
# * `np.zeros()`
# * `np.ones()` 
# * `np.diag()` 
# 
# 예제:

# In[43]:

np.arange(3, 10, 3)


# In[29]:

np.zeros((2,3))


# In[31]:

np.ones((2,))


# In[32]:

np.diag([1, 2, 3, 4])


# In[22]:

np.ones((3,3)) * 2


# ### 문제
# 
# 아래 모양의 어레이를 생성하는 코드를 작성하라.
# 단, 언급된 네 개의 함수들만 사용해야 하며, 수동으로 생성된 리스트나 어레이는 허용되지 않는다.
# 
# $$\left [ \begin{matrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{matrix} \right ]$$

# 견본답안:

# In[44]:

np.diag(np.ones((3,))*2)


# ### 문제
# 
# 아래 모양의 어레이를 생성하는 코드를 작성하라.
# 단, 언급된 네 개의 함수만 사용해야 하며, 수동으로 생성된 리스트나 어레이는 허용되지 않는다.
# 
# $$\left [ \begin{matrix} 2 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 6 \end{matrix} \right ]$$

# 견본답안:

# In[42]:

np.diag(np.arange(2, 7, 2))


# ## 넘파이의 `linspace()` 함수 활용

# numpy 모듈의 `linspace()` 함수는 지정된 구간을 정해진 크기로 일정하게 쪼개는 어래이를 생성한다.
# 예를 들어, 0부터 3사이의 구간을 균등하게 30개로 쪼개고자 하면 아래와 같이 실행하면 된다.

# In[13]:

xs = np.linspace(0, 3, 30)
xs


# ### 문제
# 
# 0부터 1사이의 구간을 균등하게 10개로 쪼개어 각 항목을 제곱하는 코드를 작성하라.

# ```
# 
# 
# 
# .
# ```

# 견본답안:

# In[53]:

np.linspace(0,1, 10) ** 2


# ## 넘파이 활용 기초 2

# `population.txt` 파일은 1900년부터 1920년까지 캐나다 북부지역에서 서식한 산토끼(hare)와 스라소니(lynx)의 숫자, 
# 그리고 채소인 당근(carrot)의 재배숫자를 순수 텍스트 데이터로 담고 있다.

# In[2]:

get_ipython().system(u'cat populations.txt')
# 윈도우 경우 아래 명령어 사용
# !type populations.txt


# In[5]:

data = np.loadtxt('populations.txt')
year, hares, lynxes, carrots = data.T


# ### 문제
# 위 코드에서 `np.loadtxt` 함수의 작동방식을 간단하게 설명하라.

# ```
# 
# 
# 
# 
# .
# ```

# ### 문제
# 위 코드에서 `data.T`에 대해 간단하게 설명하라.

# ```
# 
# 
# 
# 
# .
# ```

# In[10]:

plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))


# ### 문제
# 
# 위 코드에서 `plt.plot(year, hares, year, lynxes, year, carrots)` 를 간단하게 설명하라.

# ```
# 
# 
# 
# 
# .
# ```

# ### 문제
# 
# 산토끼, 스라소니, 당근의 예제에서 1900년부터 1921년 사이에 개체별 개체수의 변화에 대해 어떤 분석을 할 수 있는지 그래프를 이용하여 간단하게 설명하라.

# ```
# 
# 
# 
# 
# .
# ```
