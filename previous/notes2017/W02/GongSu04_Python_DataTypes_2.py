
# coding: utf-8

# # 파이썬 기본 자료형 2부

# ## 요약
# 
# * 문자열 자료형 다루기
# * 문자열 메소드 활용
# * 응용: 웹 상에 있는 데이터를 가져와서 정보 활용하기

# ### 최종 목표
# 
# * 아래 사이트에서 커피콩의 가격정보 자동으로 확인하여 응용하기
# 
# http://beans-r-us.appspot.com/prices.html
# 
# 위 사이트를 방문하면 실시간으로 변하는 커피콩의 시세를 아래와 같은 내용으로 확인할 수 있다. 
# 
# 참조: Head First Programming(한빛미디어) 2장

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/strings/coffee-beans01.jpg", width=600>
# </td>
# </tr>
# <tr>
# <td>
# http://beans-r-us.appspot.com/prices.html
# </td>
# </tr>
# 
# </table>
# </p>

# 이번 장에서는 언급된 웹사이트를 직접 방문하지 않으면서 실시간으로 변하는 
# 커피콩 가격(위 그림에서는 5달러 27센트)을 확인하는 방법을 배운다. 
# 
# 기본적으로 두 가지 기술이 필요하다. 
# 
# 1. 웹사이트 내용 읽어 들이기
# 2. 문자열로 저장된 데이터에서 필요한 정보 확인하기

# ## 웹사이트 내용 읽어 들이기

# 웹사이트 주소를 이용하여 해당 사이트의 내용 전체를 읽어 들일 수 있다.
# 예를 들어 앞서 언급된 사이트의 소스코드 전체를 아래 방식으로 가져올 수 있다.

# In[1]:

import urllib2

page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html")
text_str = page.read()


# 실제로 확인하면 웹사이트의 내용 전체가 하나의 문자열로 저장되어 있다.
# 
# **주의:** html 관련 이해할 수 없는 기호들은 여기서는 일단 무시하고 넘어가는 게 좋다.
# 또한, 위 코드를 자세히 이해하지 못해도 상관 없다. 
# 특정 웹사이트의 소스크드를 가져오기 위해 위 코드 형식을 사용한다는 것만 기억해 두면 된다. 

# In[2]:

text_str


# ### 문자열 자료형: `str` 과 `unicode`
# 
# #### 문자열(`str`)
# 
# `text_str`에 저장된 값의 자료형은 문자열이다.

# In[3]:

type(text_str)


# #### 유니코드(`unicode`)
# 
# 웹 상에서 정보를 추출할 경우 유니코드(`Unicode`) 방식을 사용하는 것을 권장하며,
# 문자열(`str`)을 유니코드로 형변환하기 위해서는 `decode()` 메소드를 활용한다. 

# In[4]:

text = text_str.decode("utf8")
type(text)


# In[5]:

text


# **주의**: `text`를 애초부터 아래처럼 선언해도 된다.
#     
#     text = page.read().decode("utf8")
#     
# 파이썬 3의 경우에는 아래와 같이 사용한다. 
# ```
# import urllib.request
# 
# page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
# text = page.read().decode("utf8")
# ```

# #### 유니코드 대 문자열
# 
# 두 자료형은 거의 동일하며, 영어와 같은 라틴어 계열 이외에 
# 한국어, 일어 등의 언어를 처리하기 위해서 유니코드가 표준으로 사용된다.
# 하지만 일반적으로 문자열(`str`)로 통일해서 부른다. 
# 
# 여기서는, 텍스트에 한국어, 일어, 중국어 등이 사용되었을 경우 unicode 방식으로 
# 처리해 주어야 한다는 정도로만 기억하고 넘어간다.

# ### 웹사이트 소스코드 확인 방법
# 
# 실제로 해당 웹사이트의 소스코드를 확인해보면 동일한 결과를 확인할 수 있다.
# 
# 주의: 커피콩의 가격은 실시간으로 변한다. 하지만 가격 이외의 문장은 변하지 않는다.

# * 윈도우 크롬
# 
# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/strings/coffee-beans04.jpg", width=600>
# </td>
# </tr>
# </table>
# </p>

# * 맥 크롬
# 
# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/strings/coffee-beans02.png", width=600>
# 
# </td>
# </tr>
# 
# </table>
# </p>

# #### 크롬에서 소스코드 확인하는 법
# 
# * 윈도우 크롬
# 
# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/strings/coffee-beans05.jpg", width=600>
# </td>
# </tr>
# </table>
# </p>

# * 맥 크롬
# 
# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/strings/coffee-beans03.png", width=600>
# 
# </td>
# </tr>
# 
# </table>
# </p>

# ## 문자열로 저장된 데이터에서 필요한 정보 확인하기

# `text`에 저장된 문자열을 다시 확인해보자.

# In[6]:

print(text)


# 위 문자열에서 원하는 정보인 커피콩의 가격을 어떻게 추출할 것인가? 
# 
# 커피콩의 가격은 실시간으로 변한다. 하지만 다섯째 줄 끝부분에 위치하고
# 달러기호(`$`)로 시작하며 `x.xx` 형식의 소수로 표현된 부분이 커피콩의 가격 정보이다.
# 
# 따라서, 예를 들어 문자열인 `">$"`의 위치를 알면 커피콩 가격정보를 얻을 수 있다.
# 그런데 특정 문자열 또는 문자의 위치를 어떻게 알 수 있을까?
# 바로 인덱스 정보와 슬라이싱 기능을 활용하면 된다.

# ### 인덱스
# 
# 문자열에 사용되는 모든 문자의 위치는 인덱스(`index`)라는 고유한 번호를 갖는다.
# 인덱스는 0부터 시작하며 오른쪽으로 한 문자씩 이동할 때마다 1씩 증가한다. 
# 
# **주의:** 파이썬을 포함해서 많은 대부분의 프로그래밍 언어에서 인덱싱은 0부터 시작한다. 
# 따라서 첫 째 문자를 확인하고자 할 때는 1이 아닌 0을 인덱스로 사용해야 한다. 
# 
# 예제를 통해 인덱스와 친숙해질 필요가 있다.

# In[7]:

a_food = "kebap"


# 특정 인덱스에 위치한 문자의 정보는 다음과 같이 확인한다.
# 
# * 0번 인덱스 값, 즉 첫째 문자

# In[8]:

a_food[0]


# * 1번 인덱스 값, 즉, 둘째 문자

# In[9]:

a_food[1]


# * 2번 인덱스 값, 즉, 셋째 문자

# In[10]:

a_food[2]


# 등등.

# #### -1번 인덱스
# 
# 문자열이 길 경우 맨 오른편에 위치한 문자의 인덱스 번호를 확인하기가 어렵다.
# 그래서 파이썬에서는 -1을 마지막 문자의 인덱스로 사용한다. 
# 
# 즉, 맨 오른편의 인덱스는 -1이고, 그 왼편은 -2, 등등으로 진행한다. 

# In[11]:

a_food[-1]


# In[12]:

a_food[-2]


# 등등.

# #### 문자열의 길이와 인덱스
# 
# 문자열의 길이보다 같거나 큰 인덱스를 사용하면 오류가 발생한다.
# 문자열의 길이는 `len()` 함수를 이용하여 확인할 수 있다.

# In[13]:

a_food[5]


# In[14]:

len(a_food)


# ### 슬라이싱
# 
# 문자열의 하나의 문자가 아닌 특정 구간 및 부분을 추출하고자 할 경우 슬라이싱을 사용한다. 
# 슬라이싱은 다음과 같이 실행한다.
# 
#     문자열변수[시작인덱스 : 끝인덱스 : 계단(step)]
# 
# * 시작인덱스: 해당 인덱스부터 문자를 추출한다.
# * 끝인덱스: 해당 인덱스 **전**까지 문자를 추출한다.
# * 계단: 시작인덱스부터 몇 계단씩 건너뛰며 문자를 추출할지 결정한다. 예를 들어 계단값이 2라면 하나 건너 추출한다. 

# In[15]:

a_food


# `kebap`에서 `ke` 부분을 추출하고 싶다면 다음과 같이 하면 된다:

# In[16]:

a_food[0 : 2 : 1]


# 즉, 문자열 처음부터 2번 인덱스 전까지, 즉 두 번째 문자까지 모두 추출하는 것이다. 
# 반면에 하나씩 건너서 추출하려면 다음처럼 하면 된다:

# In[17]:

a_food[0 : 4 : 2]


# 시작인덱스, 끝인덱스, 계단 각각의 인자가 경우에 따라 생략될 수도 있다. 
# 그럴 때는 각각의 위치에 기본값(default)이 들어 있는 것으로 처리되며, 각 자리의 기본값은 다음과 같다.
# 
# * `시작인덱스`의 기본값 = `0`
# * `끝인덱스`의 기본값 = 문자열의 길이
# * `계단`의 기본값 = `1`

# In[18]:

a_food[0 : 2]


# In[19]:

a_food[: 2]


# In[20]:

a_food[: 4 : 2]


# In[21]:

a_food[ : : 2]


# 양수와 음수를 인덱스로 섞어서 사용할 수도 있다.

# In[22]:

a_food[ : -1 : 2]


# **주의**: -1은 문자열의 끝인덱스를 의미한다.

# 끝인덱스가 문자열의 길이보다 클 수도 있다. 
# 다만 문자열의 길이 만큼만 문자를 확인한다. 

# In[23]:

a_food[: 10]


# 아래와 같이 아무 것도 입력하지 않으면 해당 문자열 전체를 추출한다.

# In[24]:

a_food[:]


# 시작인덱스 값이 끝 인덱스 값보다 같거나 작아야 제대로 추출한다. 
# 그렇지 않으면 공문자열이 추출된다.

# In[25]:

a_food[3 : 1]


# 이유는 슬라이싱은 기본적으로 작은 인덱스에 큰 인덱스 방향으로 확인하기 때문이다.
# 역순으로 추출하고자 한다면 계단을 음수로 사용하면 된다.

# In[26]:

a_food[3 : 1 : -1]


# In[27]:

a_food[-1 : : -1]


# ### `find()` 메소드 활용하기

# 인덱스와 슬라이싱의 기능을 이해하였다면 이제 `text` 변수에 할당된 문자열에서 `">$"`라는
# 문자열의 시작위치를 알아내기만 하면 된다. 
# 
# 아주 간단한 방법이 있다. 0번부터 시작해서 주욱 세어가면서 `">$"`의 시작 문자인
# `">"`의 인덱스를 확인하면 된다. 
# 하지만 이런 방식은 아래와 같은 이유로 매우 위험하다.
# 
# * 셈이 틀릴 수 있다.
# * 문자열이 길 경우 셈 자체가 불가능할 수 있다.
# * 문자열이 조금만 변경되어도 새로 처음부터 세어야 하기 때문에 경우에 따라 재활용이 불가능하다.
# 
# 이런 문제를 해결하는 좋은 방법이 있다. 
# 바로 `find()`라는 문자열 메소드를 활용하면 된다.

# In[28]:

text.find(">$")


# 이제, 찾고자 하는 `">$"` 문자열이 232번 인덱스에서 시작한다는 것을 알았다.
# 따라서 커피콩의 가격정보는 인덱스가 2보다 큰 234번이고 거기서부터 길이가 4인
# 부분문자열에 담겨 있게 된다.

# In[29]:

print(text[234: 238])


# 하지만, 여기서 234를 사용하기 보다는 `find()` 메소드를 
# 직접 활용하는 것이 더욱 좋다.

# In[30]:

price_index = text.find(">$") + 2
bean_price_str = text[price_index : price_index + 4]
print(bean_price_str)


# **주의:**
# 
# `bean_price_str` 에 저장된 커피콩의 가격정보는 문자열로 저장되어 있다.

# In[31]:

type(bean_price_str)


# 그래서 예를 들어 커피콩 가격이 6달러 이상이면 커피숍의 아메리카노 가격을 올리고,
# 그렇지 않으면 가격을 그대로 유지하는 것을 실행하도록 하는 
# 코드를 작성할 수가 없다.
# 
# 이유는, 문자열은 숫자가 아니라서 문자열과 숫자를 직접 비교할 수 없기 때문이다.
# 하지만 숫자로만 이루어닌 문자열을 진짜 숫자로 형변환시킬 수 있다.
# 예를 들어 `int()` 또는 `float()` 함수를 이용한다. 

# In[32]:

a_number = int('4')

print(a_number)
print(type(a_number))


# `float()` 함수를 이용하면 부동소수점 모양의 문자열을 부동소수점으로 형변환시킬 수 있다.

# In[33]:

float('4.2') * 2


# **주의:** 문자열과 숫자의 곱은 의미가 완전히 다르다.

# In[34]:

'4.2' * 2


# **주의:** `int()` 함수는 정수모양의 문자열에만 사용할 수 있다.

# In[35]:

int('4.2') * 2


# 부동소수점 모양의 문자열이 아니면 `float()` 함수도 오류를 발생시킨다.

# In[36]:

float('4.5GB')


# ## 커피콩 가격 정보 활용 코드 예제
# 
# 지금까지 배운 내용을 이용하여 커피콩 가격이 6.0달러 이상이면 커피숍의 아메리카노 가격을 올리고, 그렇지 않으면 가격을 그대로 유지하는 것을 실행하도록 하는 코드를 작성하면 다음과 같다. 
# 가격 확인은 1초에 한 번 하는 것으로 한다. 
# 
# 시차를 두고 코드를 실행하기 위해 `time` 모듈의 `sleep()` 함수를 활용할 수 있다.

# **주의:** 기준 가격을 높게 책정하면 너무 오랫동안 기다려야 할 수도 있다.

# In[37]:

import urllib2
import time             # 시간과 관련된 함수들의 모듈

bean_price = 5.0

while bean_price < 6.0:
    time.sleep(1)       # 코드 실행을 1초 정지한다.
    
    page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    
    price_index = text.find(">$") + 2
    bean_price_str = text[price_index : price_index + 4]
    bean_price = float(bean_price_str)
    
    print(bean_price)

print("커피콩 현재 가격이 %.2f입니다. 아메리카노 가격을 인상하세요!" % bean_price)


# **주의:** 파이썬 3에서 `print()` 함수의 활용법이 보다 편리해졌다.
# 아래와 같이 파일 맨 위에 적어 놓으면 파이썬 3의 `print()` 함수처럼 사용할 수 있다.
# 
#     from __future__ import print_function

# In[38]:

from __future__ import print_function

import urllib2
import time             # 시간과 관련된 함수들의 모듈

bean_price = 5.0

while bean_price < 6.0:
    time.sleep(1)       # 코드 실행을 1초 정지한다.
    
    page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    
    price_index = text.find(">$") + 2
    bean_price_str = text[price_index : price_index + 4]
    bean_price = float(bean_price_str)
    
    print(bean_price)

print("커피콩 현재 가격이", bean_price, "입니다. 아메리카노 가격을 인상하세요!")


# ## 문자열 관련 메소드
# 
# `find()` 메소드처럼 문자열 자료형에만 사용하는 함수들이 있다. 
# 이와같이 특정 자료형에만 사용하는 함수들을 __메소드__라 부른다.
# 
# 보다 자세한 설명은 여기서는 하지 않는다.
# 다만 `find()` 메소드의 활용을 통해 보았듯이 특정 자료형을 잘 다루기 위해서는 
# 어떤 경우에 어떤 메소드를 유용하게 활용할 수 있는지를 잘 파악해두는 것이 매우 
# 중요하다는 점만 강조한다.

# ### 메소드 호출 방법
# 
# 앞서 `find()` 메소드를 호출하는 방법을 기억해야 한다. 
# 
#     text.find("<$")
# 
# 메소드는 일반적인 함수들과는 달리, 특정 자료형의 값이 먼저 언급된 다음에
# 호출된다. 
# 
# **주의:** 메소드의 호출방식은 다른 자료형의 경우에도 동일하다. 

# ### 문자열 메소드 추가 예제
# 
# `find()` 메소드 이외에 문자열과 관련된 메소드는 매우 많다. 
# 여기서는 가장 많이 사용되는 메소드 몇 개를 소개하고자 한다.
# 
# * `strip()`
# * `split()`
# * `replace()`
# * `upper()`
# * `lower()`
# * `capitalize()`
# * `title()`
# * `startswith()`
# * `endswith()`
# 
# 예제를 통해 각 메소드의 활용법을 간략하게 확인한다.
# 
# 먼저 `week_days` 변수에 요일들을 저장한다.

# In[39]:

week_days = " Mon, Tue, Wed, Thu, Fri, Sat, Sun "


# * `strip()` 메소드는 문자열의 양 끝을 지정한 문자열 기준으로 삭제하는 방식으로 정리한다.
# 
# 예를 들어, 문자열 양끝에 있는 스페이스를 삭제하고자 할 경우 아래와 같이 실행한다.

# In[40]:

week_days.strip(" ")


# `strip()` 메소드를 인자 없이 호출하는 경우와 동일하다.

# In[41]:

week_days.strip()


# * `split()` 메소드는 지정된 부분문자열을 기준으로 문자열을 쪼개어 문자열들의 리스트로 반환한다.
#     리스트 자료형은 이후에 자세히 다룬다. 여기서는 기본적으로 알고 있는 내용으로 이해하면 된다.
# 
# 아래 예제는 `", "`, 즉 콤마와 스페이스를 기준으로 문자열을 쪼갠다.

# In[42]:

week_days.split(", ")


# 두 개 이상의 메소드를 조합해서 활용할 수도 있다.
# 
# 예를 들어, `strip()` 메소드를 먼저 실행한 다음에 그 결과에 `split()` 메소드를 실행하면
# 좀 더 산뜻한 결과를 얻을 수 있다.

# In[43]:

week_days.strip(" ").split(", ")


# * `replace()` 메소드는 하나의 문자열을 다른 문자열로 대체한다.
# 
# 예를 들어, `" Mon"`을 `"Mon"`으로 대체할 경우 아래와 같이 실행한다.

# In[44]:

week_days.replace(" Mon", "Mon")


# * `upper()` 메소드는 모든 문자를 대문자로 변환시킨다.

# In[45]:

week_days.upper()


# In[46]:

week_days.strip().upper()


# * `lower()` 메소드는 모든 문자를 소문자로 변환시킨다.

# In[47]:

week_days.lower()


# In[48]:

week_days.strip().lower()


# In[49]:

week_days.strip().lower().split(", ")


# * `capitalize()` 메소드는 제일 첫 문자를 대문자로 변환시킨다.
# 
# 아래 예제는 변화가 없어 보인다. 이유는 첫 문자가 스페이스이기 때문이다.

# In[50]:

week_days.capitalize()


# In[51]:

week_days.strip().capitalize()


# * `title()` 메소드는 각각의 단어의 첫 문자를 대문자로 변환시킨다.
# 
# 참조: 영문 책 제목의 타이틀에서 각 단어의 첫 알파벳이 대문자로 쓰여지는 경우가 많다.

# In[52]:

week_days.title()


# In[53]:

week_days.strip().title()


# * `startswith()` 메소드는 문자열이 특정 문자열로 시작하는지 여부를 판단해준다.

# In[54]:

week_days.startswith(" M")


# * `endswith()` 메소드는 문자열이 특정 문자열로 끝나는지 여부를 판단해준다.

# In[55]:

week_days.endswith("n ")


# ## 불변 자료형
# 
# 파이썬의 문자열 자료형의 값들은 변경이 불가능하다. 
# 앞서  `week_days`에 할당된 문자열에 다양한 메소드를 적용하여 새로운 문자열을 생성하였지만
# `week_days`에 할당된 문자열 자체는 전혀 변하지 않았음을 아래와 같이 확인할 수 있다.

# In[56]:

week_days


# 이와 같이 한 번 정해지면 절대 변경이 불가능한 자료형을 불변(immutable) 자료형이라 부른다.
# 
# 주어진 문자열을 이용하여 새로운 문자열을 생성하고 활용하려면 새로운 변수에 저장하여 활용해야 한다.

# In[57]:

stripped_week_days = week_days.strip()


# In[58]:

stripped_week_days


# ## 연습문제

# 애완동물의 목록을 할당받는 `pets` 변수가 아래와 같이 선언되어 있다. 

# In[59]:

pets = 'dog cat hedgehog pig swan fish bird'


# ### 연습
# 
# 애완동물의 종류를 의미하는 단어의 첫알파벳을 대문자로 바꾸려면 어떻게 해야 하는가? 
# 단, 특정 메소드를 사용하여 한 줄 코드로 작성해야 한다.

# 견본답안:

# In[60]:

pets.title()


# ### 연습
# 
# `pets`으로부터 대문자 `C` 문자 하나를 추출하라.

# 견본답안:

# In[61]:

pets.title()[4]


# ### 연습
# 
# `hedgehog`을 추출하려면?

# 견본답안:

# In[62]:

pets[8 : 16]


# ### 연습 (이전 문제 이어서)
# 
# `hdeo`을 추출하려면?

# 견본답안:

# In[63]:

pets[8 : 16 : 2]


# ### 연습
# 
# `gohegdeh`을 추출하려면?

# 견본답안:

# In[64]:

pets[15: 7 : -1]


# ### 연습
# 
# `dogs`와 `cats` 두 개의 변수가 다음과 같이 선언되었다.

# In[65]:

dogs, cats = '8', '4'


# * 강아지와 고양이를 몇 마리씩 갖고 있는지 확인하는 방법은?
# * 강아지가 고양이보다 몇 마리 더 많은지 확인하는 방법은?

# 견본답안:

# In[66]:

print(int(dogs))


# In[67]:

print(int(cats))


# In[68]:

print(abs(int(dogs) - int(cats)))


# ### 연습
# 
# 입력받은 문자열이 `dog`라는 부분문자열을 갖고 있는지 여부를 판별하는 함수 
# `find_dog`를 구현하라.
# 
# 
#     find_dog('Bull dog')
#     True
#     
#     find_dog('강아지')
#     False

# 힌트: 특정 문자열이 주어진 문자열에 부분문자열로 포함되어 있는지 여부를 판단해 주는 방식을
# 활용한다. 아래 예제들을 참조하라.

# In[69]:

'ab' in 'abc'


# In[70]:

'cat' in 'casting'


# 견본답안:

# In[71]:

def find_dog(word):
    if 'dog' in word:
        found_dog = True
    else:
        found_dog = False
    
    return found_dog


# In[72]:

find_dog('Bull dog')


# In[73]:

find_dog('강아지')


# ### 연습
# 
# 아래 코드는 커피콩의 현재 가격을 알아내어 일정 가격 이상이면 
# 커피숍의 아메리카노 가격을 인상할 것을 권유하는 프로그램이다.
# 
# ----
# ```
# from __future__ import print_function
# 
# import urllib2
# import time             # 시간과 관련된 함수들의 모듈
# 
# bean_price = 5.0
# 
# while bean_price < 6.0:
#     time.sleep(1)       # 코드 실행을 1초 정지한다.
#     
#     page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html")
#     text = page.read().decode("utf8")
#     
#     price_index = text.find(">$") + 2
#     bean_price_str = text[price_index : price_index + 4]
#     bean_price = float(bean_price_str)
#     
#     print(bean_price)
# 
# print("커피콩 현재 가격이", bean_price, "입니다. 아메리카노 가격을 인상하세요!")
# ```
# ----

# 위 코드를 수정하여, 아래 내용을 수행하는 함수를 작성하라.
# 
# * 함수 이름: `price_setter`
# 
# 
# * 함수에 사용되는 인자 두 개
#     * 첫째 인자(`b_price`): 기존의 커피콩 가격
#     * 둘째 인자(`a_price`): 아메리카노 인상 또는 인하 가격
# 
# 
# * `price_setter(b_price, a_price)`를 실행할 때
#     * `b_price`는 커피콩의 기존 가격을 의미한다. 
#         서버의 특징 상 5.5와 6.0 사이의 숫자로 주는 게 좋다.
#     * 커피콩의 실시간 가격이 `b_price` 보다 0.5 달러 이하면
#         아메리카노 가격을 `a_price` 만큼 내릴 것을 권유
#     * 커피콩의 실시간 가격이 `b_price` 보다 0.5 달러 이상이면
#         아메리카노 가격을 `a_price` 만큼 올릴 것을 권유

# 견본답안:

# In[76]:

from __future__ import print_function

import urllib2
import time             # 시간과 관련된 함수들의 모듈

def price_setter(b_price, a_price):
    bean_price = b_price
    while 5.5 < bean_price < 6.0:
        time.sleep(1)       # 코드 실행을 1초 정지한다.

        page = urllib2.urlopen("http://beans-r-us.appspot.com/prices.html")
        text = page.read().decode("utf8")

        price_index = text.find(">$") + 2
        bean_price_str = text[price_index : price_index + 4]
        bean_price = float(bean_price_str)
        
    print("현재 커피콩 가격이", bean_price, "달러 입니다.")

    if bean_price <= 5.5:
        print("아메리카노 가격을", a_price, "달러만큼 인하하세요!")
    else:
        print("아메리카노 가격을", a_price, "달러만큼 인상하세요!")


# 예를 들어, 현재 커피콩의 가격이 5.7달러이고, 커피콩의 실시간 가격이
# 5.2달러 이하이면 아메리카노의 가격을 50센트 내리고
# 6.2달러 이상이면 50센트 올리라고 권유하고자 한다면 아래와 같이 
# `price_setter()` 함수를 호출하면 된다.

# In[77]:

price_setter(5.7, 0.5)

