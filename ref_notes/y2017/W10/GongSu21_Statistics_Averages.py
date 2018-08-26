
# coding: utf-8

# In[1]:

from __future__ import print_function, division


# #### 자료 안내: 여기서 다루는 내용은 아래 사이트의 내용을 참고하여 생성되었음.
# 
# https://github.com/rouseguy/intro2stats

# # 안내사항
# 
# 오늘 다루는 내용은 pandas 모듈의 소개 정도로 이해하고 넘어갈 것을 권장한다.
# 
# 아래 내용은 엑셀의 스프레드시트지에 담긴 데이터를 분석하여 평균 등을 어떻게 구하는가를 알고 있다면 어렵지 않게 이해할 수 있는 내용이다. 즉, 넘파이의 어레이에 대한 기초지식과 엑셀에 대한 기초지식을 활용하면 내용을 기본적으로 이해할 수 있을 것이다.
# 
# 좀 더 자세한 설명이 요구된다면 아래 사이트의 설명을 미리 읽으면 좋다(5.2절 내용까지면 충분함).
# 하지만, 아래 내용을 엑셀의 기능과 비교하면서 먼저 주욱 훑어 볼 것을 권장한다.
# 
# http://sinpong.tistory.com/category/Python%20for%20data%20analysis

# # 평균(Average) 구하기

# ## 오늘의 주요 예제

# 미국에서 거래되는 담배(식물)의 도매가격 데이터를 분석하여, 거래된 도매가의 평균을 구한다.
# 
# * 평균값(Mean)
# * 중앙값(Median)
# * 최빈값(Mode)
# 
# 평균에 대한 보다 자세한 설명은 첨부된 강의노트 참조: GongSu21-Averages.pdf

# ### 사용하는 주요 모듈
# 
# 아래는 통계분석에서 기본적으로 사용되는 모듈들이다.
# 
# * pandas: 통계분석 전용 모듈
#     * numpy 모듈을 바탕으로 하여 통계분석에 특화된 모듈임.
#     * 마이크로소프트의 엑셀처럼 작동하는 기능을 지원함
# * datetime: 날짜와 시간을 적절하게 표시하도록 도와주는 기능을 지원하는 모듈
# * scipy: 수치계산, 공업수학 등을 지원하는 모듈

# ## 팬더스(Pandas) 소개
# 
# * pandas란?
#     * 빠르고 쉬운 데이터 분석 도구를 지원하는 파이썬 모듈
#     * numpy를 기본적으로 활용함.
# 
# 
# * pandas의 기능
#     * 데이터 정렬 등 다양한 연산 기능 지원
#     * 강력한 색인 및 슬라이싱 기능
#     * 시계열(time series) 기능 지원
#     * 결측치(누락된 데이터) 처리
#     * SQL과 같은 DB의 관계연산 기능 지원
#     
# **주의:** pandas 모듈의 기능에 대한 보다 자세한 설명은 다음 시간에 다룬다.
# 여기서는 pandas 모듈을 어떻게 활용하는지에 대한 감을 잡기만 하면 된다.

# In[2]:

import numpy as np
import pandas as pd
from datetime import datetime as dt
from scipy import stats


# ## 데이터 불러오기 및 처리
# 
# 오늘 사용할 데이터는 다음과 같다.
# 
# * 미국 51개 주(State)별 담배(식물) 도매가격 및 판매일자: Weed_price.csv
# 
# 아래 그림은 미국의 주별 담배(식물) 판매 데이터를 담은 Weed_Price.csv 파일를 엑셀로 읽었을 때의 일부를 보여준다.
# 실제 데이터량은 22899개이며, 아래 그림에는 5개의 데이터만을 보여주고 있다.
# * 주의: 1번줄은 테이블의 열별 목록(column names)을 담고 있다.
# * 열별 목록: State, HighQ, HighQN, MedQ, MedQN, LowQ, LowQN, date
# 
# <p>
# <table cellspacing="20">
# <tr>
# <td>
# <img src="img/weed_price.png", width=600>
# </td>
# </tr>
# </table>
# </p>

# ### csv 파일 불러오기
# 
# * pandas 모듈의 read_csv 함수 활용
# * read_csv 함수의 리턴값은 DataFrame 이라는 특수한 자료형임
#     * 엑셀의 위 그림 모양의 스프레드시트(spreadsheet)라고 생각하면 됨.
# 
# 언급한 세 개의 csv 파일을 pandas의 read_csv 함수를 이용하여 불러들이자.
# 
# **주의**: Weed_Price.csv 파일을 불러들일 때, parse_dates라는 키워드 인자가 사용되었다. 
# * parse_dates 키워드 인자: 날짜를 읽어들일 때 다양한 방식을 사용하도록 하는 기능을 갖고 있다.
#     * 여기서 값을 [-1]로 준 것은 소스 데이터에 있는 날짜 데이터를 변경하지 말고 그대로 불러오라는 의미이다.
#     * 위 엑셀파일에서 볼 수 있듯이, 마지막 열에 포함된 날짜표시는 굳이 변경을 요하지 않는다.

# In[3]:

prices_pd = pd.read_csv("data/Weed_Price.csv", parse_dates=[-1])


# read_csv 함수의 리턴값은 DataFrame 이라는 자료형이다.

# In[4]:

type(prices_pd)


# #### DataFrame 자료형

# 자세한 설명은 다음 시간에 추가될 것임. 우선은 아래 사이트를 참조할 수 있다는 정도만 언급함.
# (5.2절 내용까지면 충분함)
# 
# http://sinpong.tistory.com/category/Python%20for%20data%20analysis

# #### DataFrame 자료형과 엑셀의 스프레드시트 비교하기

# 불러 들인 Weed_Price.csv 파일의 상위 다섯 줄을 확인해보면, 앞서 엑셀파일 그림에서 본 내용과 일치한다.
# 다만, 행과 열의 목록이 조금 다를 뿐이다.
# * 엑셀에서는 열 목록이 A, B, C, ..., H로 되어 있으며, 소스 파일의 열 목록은 1번 줄로 밀려 있다.
# * 엑셀에서의 행 목록은 1, 2, 3, ... 으로 되어 있다.
# 
# 하지만 read_csv 파일은 좀 다르게 불러 들인다.
# * 열 목록은 소스 파일의 열 목록을 그대로 사용한다.
# * 행 목록은 0, 1, 2, ... 으로 되어 있다.

# 데이터 파일의 상위 몇 줄을 불러들이기 위해서는 DataFrame 자료형의 head 메소드를 활용한다.
# 인자값을 주지 않으면 상위 5줄을 보여준다.

# In[5]:

prices_pd.head()


# 인자를 주면 원하는 만큼 보여준다.

# In[6]:

prices_pd.head(10)


# 파일이 매우 많은 수의 데이터를 포함하고 있을 경우, 맨 뒷쪽 부분을 확인하고 싶으면
# tail 메소드를 활용한다. 사용법은 head 메소드와 동일하다.
# 
# 아래 명령어를 통해 Weed_Price.csv 파일에 22899개의 데이터가 저장되어 있음을 확인할 수 있다.

# In[7]:

prices_pd.tail()


# #### 결측치 존재 여부
# 
# 위 결과를 보면 LowQ 목록에 NaN 이라는 기호가 포함되어 있다. NaN은 Not a Number, 즉, 숫자가 아니다라는 의미이며, 데이터가 애초부터 존재하지 않았거나 누락되었음을 의미한다.

# #### DataFrame의 dtypes
# 
# DataFrame 자료형의 dtypes 속성을 이용하면 열별 목록에 사용된 자료형을 확인할 수 있다.
# 
# Weed_Price.csv 파일을 읽어 들인 prices_pd 변수에 저장된 DataFrame 값의 열별 목록에 사용된 자료형을 보여준다.
# 
# **주의:** 
# * numpy의 array 자료형의 dtype 속성은 하나의 자료형만을 담고 있다.
# * 열별 목록에는 하나의 자료형 값들만 올 수 있다.
#     즉, 열 하나하나가 넘파이의 array에 해당한다고 볼 수 있다.
# * State 목록에 사용된 object 라는 dtype은 문자열이 저장된 위치를 가리키는 포인터를 의미한다.
#     * 문자열의 길이를 제한할 수 없기 때문에 문자열을 어딘가에 저장하고 포인터가 그 위치를 가리키며, 
#         필요에 따라 포인터 정보를 이용하여 저장된 문자열을 확인한다.
# * 마지막 줄에 표시된 "dtype: object"의 의미는 복잡한 데이터들의 자료형이라는 의미로 이해하면 됨.

# In[8]:

prices_pd.dtypes


# ### 정렬 및 결측치 채우기

# #### 정렬하기
# 주별로, 날짜별로 데이터를 정렬한다.

# In[9]:

prices_pd.sort_values(['State', 'date'], inplace=True)


# #### 결측치 채우기
# 
# 평균을 구하기 위해서는 결측치(누락된 데이터)가 없어야 한다.
# 여기서는 이전 줄의 데이터를 이용하여 채우는 방식(method='ffill')을 이용한다.
# 
# **주의:** 앞서 정렬을 먼저 한 이유는, 결측치가 있을 경우 가능하면 동일한 주(State), 
# 비슷한 시점에서 거래된 가격을 사용하고자 함이다.

# In[10]:

prices_pd.fillna(method='ffill', inplace=True)


# 정렬된 데이터의 첫 부분은 아래와 같이 알라바마(Alabama) 주의 데이터만 날짜별로 순서대로 보인다.

# In[11]:

prices_pd.head()


# 정렬된 데이터의 끝 부분은 아래와 같이 요밍(Wyoming) 주의 데이터만 날짜별로 순서대로 보인다.
# 이제 결측치가 더 이상 존재하지 않는다.

# In[12]:

prices_pd.tail()


# ## 데이터 분석하기: 평균(Average)
# 
# 캘리포니아 주를 대상으로해서 담배(식물) 도매가의 평균(average)을 구해본다.

# ### 평균값(Mean)
# 
# * 평균값 = 모든 값들의 합을 값들의 개수로 나누기
#     * $X$: 데이터에 포함된 값들을 대변하는 변수
#     * $n$: 데이터에 포함된 값들의 개수
#     * $\Sigma\, X$: 데이터에 포함된 모든 값들의 합
# 
# $$\text{평균값}(\mu) = \frac{\Sigma\, X}{n}$$

# 먼저 마스크 인덱스를 이용하여 캘리포니아 주의 데이터만 추출해야 한다.

# In[13]:

california_pd = prices_pd[prices_pd.State == "California"].copy(True)


# 캘리포니아 주에서 거래된 첫 5개의 데이터를 확인해보자.

# In[14]:

california_pd.head(20)


# HighQ 열 목록에 있는 값들의 총합을 구해보자.
# 
# **주의:** `sum()` 메소드 활용을 기억한다.

# In[15]:

ca_sum = california_pd['HighQ'].sum()
ca_sum


# HighQ 열 목록에 있는 값들의 개수를 확인해보자.
# 
# **주의:** `count()` 메소드 활용을 기억한다.

# In[16]:

ca_count = california_pd['HighQ'].count()
ca_count


# 이제 캘리포니아 주에서 거래된 HighQ의 담배가격의 평균값을 구할 수 있다.

# In[17]:

# 캘리포니아 주에서 거래된 상품(HighQ) 담배(식물) 도매가의 평균값
ca_mean = ca_sum / ca_count
ca_mean


# ### 중앙값(Median)
# 
# 캘리포니아 주에서 거래된 HighQ의 담배가격의 중앙값을 구하자.
# 
# * 중앙값 = 데이터를 크기 순으로 정렬하였을 때 가장 가운데에 위치한 수
#     * 데이터의 크기 n이 홀수일 때: $\frac{n+1}{2}$번 째 위치한 데이터
#     * 데이터의 크기 n이 짝수일 때: $\frac{n}{2}$번 째와 $\frac{n}{2}+1$번 째에 위치한 데이터들의 평균값   

# 여기서는 데이터의 크기가 449로 홀수이다.

# In[18]:

ca_count


# 따라서 중앙값은 $\frac{\text{ca_count}-1}{2}$번째에 위치한 값이다.
# 
# **주의:** 인덱스는 0부터 출발한다. 따라서 중앙값이 하나 앞으로 당겨진다.

# In[19]:

ca_highq_pd = california_pd.sort_values(['HighQ'])
ca_highq_pd.head()


# 인덱스 로케이션 함수인 `iloc` 함수를 활용한다.
# 
# **주의:** `iloc` 메소드는 인덱스 번호를 사용한다. 
# 위 표에서 보여주는 인덱스 번호는 Weed_Price.csv 파일을 처음 불러왔을 때 사용된 인덱스 번호이다.
# 하지만 ca_high_pd 에서는 참고사항으로 사용될 뿐이며, `iloc` 함수에 인자로 들어가는 인덱스는 다시 0부터 세는 것으로 시작한다.
# 따라서 아래 코드처럼 기존의 참고용 인덱스를 사용하면 옳은 답을 구할 수 없다.

# In[20]:

# 캘리포니아에서 거래된 상품(HighQ) 담배(식물) 도매가의 중앙값
ca_median = ca_highq_pd.HighQ.iloc[int((ca_count-1)/ 2)]
ca_median


# ### 최빈값(Mode)
# 
# 캘리포니아 주에서 거래된 HighQ의 담배가격의 최빈값을 구하자.
# 
# * 최빈값 = 가장 자주 발생한 데이터
# 
# **주의:** `value_counts()` 메소드 활용을 기억한다.

# In[21]:

# 캘리포니아 주에서 가장 빈번하게 거래된 상품(HighQ) 담배(식물)의 도매가
ca_mode = ca_highq_pd.HighQ.value_counts().index[0]
ca_mode


# ## 연습문제

# ### 연습
# 
# 지금까지 구한 평균값, 중앙값, 최빈값을 구하는 함수가 이미 DataFrame과 Series 자료형의 메소드로 구현되어 있다.
# 
# 아래 코드들을 실행하면서 각각의 코드의 의미를 확인하라.

# In[22]:

california_pd.mean()


# In[23]:

california_pd.mean().HighQ


# In[24]:

california_pd.median()


# In[25]:

california_pd.mode()


# In[26]:

california_pd.mode().HighQ


# In[27]:

california_pd.HighQ.mean()


# In[28]:

california_pd.HighQ.median()


# In[29]:

california_pd.HighQ.mode()


# ### 연습 
# 
# 캘리포니아 주에서 2013년, 2014년, 2015년에 거래된 HighQ의 담배(식물) 도매가격의 평균을 각각 구하라.
# 
# **힌트:** `california_pd.iloc[0]['date'].year`

# #### 견본답안1
# 2014년에 거래된 도매가의 평균값을 아래와 같이 계산할 수 있다.
# 
# * sum 변수: 2014년도에 거래된 도매가의 총합을 담는다.
# * count 변수: 2014년도의 거래 횟수를 담는다.

# In[30]:

sum = 0
count = 0

for index in np.arange(len(california_pd)):
    if california_pd.iloc[index]['date'].year == 2014:
        sum += california_pd.iloc[index]['HighQ']
        count += 1
sum/count


# #### 견본답안2
# 아래와 같은 방식을 이용하여 인덱스 정보를 구하여 슬라이싱 기능을 활용할 수도 있다.
# 슬라이싱을 활용하여 연도별 평균을 구하는 방식은 본문 내용과 동일한 방식을 따른다.

# In[31]:

years = np.arange(2013, 2016)
year_starts = [0]

for yr in years:
    for index in np.arange(year_starts[-1], len(california_pd)):
        if california_pd.iloc[index]['date'].year == yr:
            continue
        else:
            year_starts.append(index)
            break

year_starts


# `year_starts`에 담긴 숫자들의 의미는 다음과 같다.
# 
# * 0번줄부터 2013년도 거래가 표시된다.
# 
# * 5번줄부터 2014년도 거래가 표시된다.
# 
# * 369번줄부터 2015년도 거래가 표시된다.

# In[32]:

california_pd.iloc[4]


# In[33]:

california_pd.iloc[5]


# In[34]:

california_pd.iloc[368]


# In[35]:

california_pd.iloc[369]

