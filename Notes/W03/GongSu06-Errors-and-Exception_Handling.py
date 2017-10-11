
# coding: utf-8

# # 오류 및 예외 처리

# ## 개요
# 
# * 코딩할 때 발생할 수 있는 다양한 **오류** 살펴 보기
#     
# * **오류 메시지** 정보 확인 방법
# 
# * **예외 처리**, 즉 오류가 발생할 수 있는 예외적인 상황을 미리 고려하는 방법 소개

# ## 오늘의 주요 예제
# 
# 

# 아래 코드는 `raw_input()` 함수를 이용하여 사용자로부터 숫자를 입력받아 그 숫자의 제곱을 리턴하고자 하는 내용을 담고 있다. 코드를 실행하면 숫자를 입력하라는 창이 나오며, 
# 여기에 숫자 3을 입력하면 정상적으로 작동한다. 
# 하지만, 예를 들어, 3.2를 입력하면 값 오류(value error)가 발생한다. 

# In[1]:

from __future__ import print_function

input_number = raw_input("A number please: ")
number = int(input_number)

print("제곱의 결과는", number**2, "입니다.")


# **주의:** 파이썬 3의 경우 `input()` 함수를 `raw_input()` 대신에 사용해야 한다.
# 
# 위 코드는 정수들의 제곱을 계산하는 프로그램이다. 
# 하지만 사용자가 경우에 따라 정수 이외의 값을 입력하면 시스템이 다운된다. 
# 이에 대한 해결책을 다루고자 한다.

# ## 오류 예제
# 
# 먼저 오류의 다양한 예제를 살펴보자.
# 다음 코드들은 모두 오류를 발생시킨다.

# ### 예제: 0으로 나누기 오류
# 
# ```python
# 4.6/0
# ```
# 
# 오류 설명: 0으로 나눌 수 없다.

# ### 예제: 문법 오류
# 
# ```python
# sentence = 'I am a sentence
# ```
# 
# 오류 설명: 문자열 양 끝의 따옴표가 짝이 맞아야 한다.
# * 작은 따옴표끼리 또는 큰 따옴표끼리

# ### 예제: 들여쓰기 문법 오류
# 
# ```python
# for i in range(3):
#     j = i * 2
#       print(i, j)
# ```
# 
# 오류 설명: 2번 줄과 3번 줄의 들여쓰기 정도가 동일해야 한다.

# ### 예제: 자료형 오류
# 
# ```python
# new_string = 'cat' - 'dog'
# new_string = 'cat' * 'dog'
# new_string = 'cat' / 'dog'
# 
# new_string = 'cat' + 3
# new_string = 'cat' - 3
# new_string = 'cat' / 3
# ```
# 
# 오류 설명: 문자열 자료형끼리의 합, 문자열과 정수의 곱셈만 정의되어 있다.

# ### 예제: 이름 오류
# 
# ```python
# print(party)
# ```
# 
# 오류 설명: 미리 선언된 변수만 사용할 수 있다.

# ### 예제: 인덱스 오류
# 
# ```python
# a_string = 'abcdefg'
# a_string[12]
# ```
# 
# 오류 설명: 인덱스는 문자열의 길이보다 작은 수만 사용할 수 있다.

# ### 예제: 값 오류
# 
# ```python
# int(a_string)
# ```
# 
# 오류 설명: `int()` 함수는 정수로만 구성된 문자열만 처리할 수 있다.

# ### 예제: 속성 오류
# 
# ```python
# print(a_string.len())
# ```
# 
# 오류 설명: 문자열 자료형에는 `len()` 메소드가 존재하지 않는다.
# 
# **주의:** `len()` 이라는 함수는 문자열의 길이를 확인하지만 문자열 메소드는 아니다. 
# 이후에 다룰 리스트, 튜플 등에 대해서도 사용할 수 있는 함수이다.

# ## 오류 확인
# 
# 앞서 언급한 코드들을 실행하면 오류가 발생하고 어디서 어떤 오류가 발생하였는가에 대한 정보를 
# 파이썬 해석기가 바로 알려 준다. 

# ### 예제

# In[2]:

sentence = 'I am a sentence


# 오류를 확인하는 메시지가 처음 볼 때는 매우 생소하다. 
# 위 오류 메시지를 간단하게 살펴보면 다음과 같다.
# 
# * `File "<ipython-input-37-a6097ed4dc2e>", line 1`
# 
#     1번 줄에서 오류 발생
# 
# 
# * `sentence = 'I am a sentence` 
#                              ^
# 
#     오류 발생 위치 명시
# 
# 
# * `SyntaxError: EOL while scanning string literal`
# 
#     오류 종류 표시: 문법 오류(SyntaxError)
# 
# 

# ### 예제
# 
# 아래 예제는 0으로 나눌 때 발생하는 오류를 나타낸다.
# 오류에 대한 정보를 잘 살펴보면서 어떤 내용을 담고 있는지 확인해 보아야 한다.

# In[3]:

a = 0
4/a


# ## 오류의 종류
# 
# 앞서 예제들을 통해 살펴 보았듯이 다양한 종류의 오류가 발생하며,
# 코드가 길어지거나 복잡해지면 오류가 발생할 가능성은 점차 커진다.
# 오류의 종류를 파악하면 어디서 왜 오류가 발생하였는지를 보다 쉽게 파악하여
# 코드를 수정할 수 있게 된다.
# 
# 따라서 코드의 발생원인을 바로 알아낼 수 있어야 하며 이를 위해서는 오류 메시지를 
# 제대로 확인할 수 있어야 한다. 
# 하지만 여기서는 언급된 예제 정도의 수준만 다루고 넘어간다.
# 
# 코딩을 하다 보면 어차피 다양한 오류와 마주치게 될 텐데 그때마다
# 스스로 오류의 내용과 원인을 확인해 나가는 과정을 통해 
# 보다 많은 경험을 쌓는 길 외에는 달리 방법이 없다.

# ## 예외 처리
# 
# 코드에 문법 오류가 포함되어 있는 경우 아예 실행되지 않는다. 
# 그렇지 않은 경우에는 일단 실행이 되고 중간에 오류가 발생하면 바로 멈춰버린다.
# 
# 이렇게 중간에 오류가 발생할 수 있는 경우를 미리 생각하여 대비하는 과정을 
# **예외 처리(exception handling)**라고 부른다. 
# 
# 예를 들어, 오류가 발생하더라도 오류발생 이전까지 생성된 정보들을 저장하거나, 오류발생 이유를 좀 더 자세히 다루거나, 아니면 오류발생에 대한 보다 자세한 정보를 사용자에게 알려주기 위해 예외 처리를 사용한다. 

# ### 예제 
# 
# 아래 코드는 `raw_input()` 함수를 이용하여 사용자로부터 숫자를 입력받아 그 숫자의 제곱을 리턴하고자 하는 내용을 담고 있으며, 코드에는 문법적 오류가 없다. 
# 
# 그리고 코드를 실행하면 숫자를 입력하라는 창이 나온다. 
# 여기에 숫자 3을 입력하면 정상적으로 작동하지만 
# 예를 들어, 3.2를 입력하면 값 오류(value error)가 발생한다. 

# In[4]:

from __future__ import print_function

number_to_square = raw_input("A number please")

# number_to_square 변수의 자료형이 문자열(str)임에 주의하라. 
# 따라서 연산을 하고 싶으면 정수형(int)으로 형변환을 먼저 해야 한다. 

number = int(number_to_square)

print("제곱의 결과는", number**2, "입니다.")


# 3.2를 입력했을 때 오류가 발생하는 이유는 `int()` 함수가 정수 모양의 문자열만 
# 처리할 수 있기 때문이다. 
# 
# 사실 정수들의 제곱을 계산하는 프로그램을 작성하였지만 경우에 따라 
# 정수 이외의 값을 입력하는 경우가 발생하게 되며, 이런 경우를 대비해야 한다.
# 즉, 오류가 발생할 것을 미리 예상해야 하며, 어떻게 대처해야 할지 준비해야 하는데, 
# `try ... except ...`문을 이용하여 예외를 처리하는 방식을 활용할 수 있다.

# In[5]:

number_to_square = raw_input("A number please:")

try: 
    number = int(number_to_square)
    print("제곱의 결과는", number ** 2, "입니다.")
except:
    print("정수를 입력해야 합니다.")


# 오류 종류에 맞추어 다양한 대처를 하기 위해서는 오류의 종류를 명시하여 예외처리를 하면 된다.
# 아래 코드는 입력 갑에 따라 다른 오류가 발생하고 그에 상응하는 방식으로 예외처리를 실행한다.

# #### 값 오류(ValueError)의 경우

# In[6]:

number_to_square = raw_input("A number please: ")

try: 
    number = int(number_to_square)
    a = 5/(number - 4)
    print("결과는", a, "입니다.")
except ValueError:
    print("정수를 입력해야 합니다.")
except ZeroDivisionError:
    print("4는 빼고 하세요.")


# #### 0으로 나누기 오류(ZeroDivisionError)의 경우

# In[7]:

number_to_square = raw_input("A number please: ")

try: 
    number = int(number_to_square)
    a = 5/(number - 4)
    print("결과는", a, "입니다.")
except ValueError:
    print("정수를 입력해야 합니다.")
except ZeroDivisionError:
    print("4는 빼고 하세요.")


# **주의:** 이와 같이 발생할 수 예외를 가능한 한 모두 염두하는 프로그램을 구현해야 하는 일은
# 매우 어려운 일이다.

# 앞서 보았듯이 오류의 종류를 정확히 알 필요가 발생한다. 
# 
# 다음 예제에소 보듯이 오류의 종류를 틀리게 명시하면 예외 처리가 제대로 작동하지 않는다.

# In[8]:

try:
    a = 1/0
except ValueError:
    print("This program stops here.")


# ### `raise` 함수
# 
# 강제로 오류를 발생시키고자 하는 경우에 사용한다.

# ### 예제
# 
# 어떤 함수를 정확히 정의하지 않은 상태에서 다른 중요한 일을 먼저 처리하고자 할 때 
# 아래와 같이 함수를 선언하고 넘어갈 수 있다.
# 
# 그런데 아래 함수를 제대로 선언하지 않은 채로 다른 곳에서 호출하면 
# 
#     "아직 정의되어 있지 않음"
#     
# 이란 메시지로 정보를 알려주게 된다. 

# In[9]:

def to_define():
    """아주 복잡하지만 지금 당장 불필요"""
    raise NotImplementedError("아직 정의되어 있지 않음")


# In[10]:

print(to_define())


# **주의:** 오류 처리를 사용하지 않으면 오류 메시지가 보이지 않을 수도 있음에 주의해야 한다.

# In[11]:

def to_define1():
    """아주 복잡하지만 지금 당장 불필요"""


# In[12]:

print(to_define1())


# ## 코드의 안전성 문제
# 
# 문법 오류 또는 실행 중에 오류가 발생하지 않는다 하더라도 **코드의 안전성**이 보장되지는 않는다. 
# 코드의 안정성이라 함은 코드를 실행할 때 기대하는 결과가 산출된다는 것을 보장한다는 의미이다. 

# ### 예제
# 
# 아래 코드는 숫자의 제곱을 리턴하는 `square()` 함수를 제대로 구현하지 못한 경우를 다룬다.

# In[13]:

def square( number ):
    """
    정수를 인자로 입력 받아 제곱을 리턴한다.
    """
    
    square_of_number = number * 2
    
    return square_of_number


# 위 함수를 아래와 같이 호출하면 오류가 전혀 발생하지 않지만,
# 엉뚱한 값을 리턴한다.

# In[14]:

square(3)


# **주의:** `help()` 를 이용하여 어떤 함수가 무슨 일을 하는지 내용을 확인할 수 있다.
# 단, 함수를 정의할 때 함께 적힌 문서화 문자열(docstring) 내용이 확인된다.
# 따라서, 함수를 정의할 때 문서화 문자열에 가능한 유효한 정보를 입력해 두어야 한다.

# In[15]:

help(square)


# ### 오류에 대한 보다 자세한 정보
# 
# 파이썬에서 다루는 오류에 대한 보다 자세한 정보는 아래 사이트들에 상세하게 안내되어 있다.
# 
# * 파이썬 기본 내장 오류 정보 문서:
#     https://docs.python.org/3.4/library/exceptions.html
# 
# * 파이썬 예외처리 정보 문서: 
#     https://docs.python.org/3.4/tutorial/errors.html

# ## 연습문제

# ### 연습
# 
# 아래 코드는 100을 입력한 값으로 나누는 함수이다.
# 다만 0을 입력할 경우 0으로 나누기 오류(`ZeroDivisionError`)가 발생한다.

# In[16]:

from __future__ import print_function

number_to_square = raw_input("A number to divide 100: ")

number = int(number_to_square)
print("100을 입력한 값으로 나눈 결과는", 100/number, "입니다.")


# 아래 내용이 충족되도록 위 코드를 수정하라.
# 
# * 나눗셈이 부동소수점으로 계산되도록 한다. 
# * 0이 아닌 숫자가 입력될 경우 100을 그 숫자로 나눈다.
# * 0이 입력될 경우 0이 아닌 숫자를 입력하라고 전달한다. 
# * 숫자가 아닌 값이 입력될 경우 숫자를 입력하라고 전달한다.

# 견본답안:

# In[17]:

number_to_square = raw_input("A number to divide 100: ")

try: 
    number = float(number_to_square)
    print("100을 입력한 값으로 나눈 결과는", 100/number, "입니다.")
except ZeroDivisionError:
    raise ZeroDivisionError('0이 아닌 숫자를 입력하세요.')
except ValueError:
    raise ValueError('숫자를 입력하세요.')    


# In[18]:

number_to_square = raw_input("A number to divide 100: ")

try: 
    number = float(number_to_square)
    print("100을 입력한 값으로 나눈 결과는", 100/number, "입니다.")
except ZeroDivisionError:
    raise ZeroDivisionError('0이 아닌 숫자를 입력하세요.')
except ValueError:
    raise ValueError('숫자를 입력하세요.')    

