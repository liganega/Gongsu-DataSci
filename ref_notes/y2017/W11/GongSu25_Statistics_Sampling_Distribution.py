
# coding: utf-8

# In[1]:

from __future__ import print_function, division


# #### 자료 안내: 여기서 다루는 내용은 아래 사이트의 내용을 참고하여 생성되었음.
# 
# https://github.com/rouseguy/intro2stats

# # 표본분포와 신뢰구간

# ## 주요내용
# 
# 앞서 [GongSu22](https://github.com/liganega/Gongsu-DataSci/blob/master/Notes/W10/GongSu22_Statistics_Population_Variance.ipynb)에서 표본 데이터를 이용하여 모집단의 평균과 분산에 대한 점추정을 알아보았다.
# 여기서는 표본분포를 이용하여 미국 51개 주에서 거래된 담배(식물) 도매가의 평균에 대한 신뢰구간을 구하는 방법을 알아본다.

# ## 주요 예제
# 
# * 캘리포니아 주에서 2014년에 거래된 상품 담배(식물)의 도매가
# * 도매가의 표본분포 구하기
# * 도매가의 평균값 추정치의 신뢰구간 구하기

# ## 주요 모듈
# 
# numpy와 pandas 이외에 통계전용 모듈인 stats 모듈을 임포트 한다.

# In[2]:

import numpy as np
import pandas as pd
from scipy import stats


# ## 연도별, 월별 데이터 추출하기

# Weed_Price.csv의 date 열에는 거래일자가 2014-01-01의 형식으로 포함되어 있다.
# 이 정보를 이용하여 연도별, 월별 데이터를 구하려면 거래일자로부터 연도 또는 월에 대한 정보만을 추출할 수 있어야 한다.
# 
# 여기서는 Timestamp 자료형의 속성을 활용하여 필요한 정보를 얻는 방식을 배운다.

# ### csv 파일 불러오기
# 
# 먼저 Weed_Price.csv 파일의 내용을 다시 불러 온다.

# In[3]:

weed_pd = pd.read_csv("data/Weed_Price.csv", parse_dates=[-1])


# In[4]:

weed_pd.head()


# ### Timestamp 자료형
# 
# date 열에는 거래일자 정보가 들어 있는데, 각 정보의 자료형은 Timestamp 라고 불린다.
# 
# 0번 줄의 date 정보를 확인하면 Timestamp 자료형이 사용된 것을 확인할 수 있다.

# In[5]:

weed_pd.date[0]


# Timestamp 자료형에는 year, month, day 등 거래일자에 대한 구체적인 구체적인 정보를 담고 있는 속성이 포함되어 있다.

# In[6]:

weed_pd.date[0].year


# In[7]:

weed_pd.date[0].month


# In[8]:

weed_pd.date[0].day


# ### apply 함수 활용
# 
# 위 속성들을 이용하여 거래일자에서 연도별, 월별 정보를 추출하여 새로운 열(컬럼)으로 추가할 수 있다.
# 이를 위해 apply() 함수를 활용한다.
# 
# **주의:** Series와 DataFrame 자료형에 apply 함수와 동일한 기능을 가진 apply 메소드가 선언되어 있다.

# 먼저 weed_pd.date 의 자료형이 Series 임을 확인한다.

# In[9]:

type(weed_pd.date)


# x가 Timestamp 자료형일 때, x 에서 연도 정보를 추출하는 함수를 아래와 같이 정의할 수 있다.

# In[10]:

def getYear(x):
    return x.year


# 동일한 방식으로 x가 Timestamp 자료형일 때, x 에서 월에 정보를 추출하는 함수를 아래와 같이 정의할 수 있다.

# In[11]:

def getMonth(x):
    return x.month


# 이제 두 함수를 이용하여 거래년도 만을 담는 칸을 추가할 수 있다. 
# 
# 먼저 아래 코드를 실행해보자.

# In[12]:

year_col = weed_pd.date.apply(getYear)
year_col.head()


# 위 결과의 자료형은 Series 이다.

# In[13]:

type(year_col)


# 동일한 방식으로 month_col을 추출한다.

# In[14]:

month_col = weed_pd.date.apply(getMonth)
month_col.head()


# ### DataFrame에 열 추가하기
# 
# 추출한 두 시리즈를 weed_pd 에 새로운 열로 추가한다.

# In[15]:

weed_pd["month"] = month_col
weed_pd["year"] = year_col


# 두 개의 열이 추가되었음을 확인할 수 있다.

# In[16]:

weed_pd.head()


# ## 캘리포니아 주에서 2014년도 거래된 담배(식물) 도매가 추출하기

# 마스크 인덱싱을 활용하여 캘리포니아 주에서 2014년도에 거래된 데이터만 추출할 수 있다.
# 
# **주의:** year 열을 추가하였기에 가능하다.

# In[17]:

weed_ca_2014 = weed_pd[(weed_pd.State=="California") & (weed_pd.year==2014)]
weed_ca_2014.head()


# ### 캘리포니아 주에서 2014년도에 거래된 상품 담배(식물)의 도매가의 평균분포

# #### 평균분포의 평균값

# In[18]:

ca_2014_mean = weed_ca_2014.HighQ.mean()
ca_2014_mean


# #### 평균분포의 분산

# In[19]:

ca_2014_std = weed_ca_2014.HighQ.std()
ca_2014_std


# #### 신뢰구간
# 
# 신뢰수준 95%에 대한 신뢰구간을 구할 수 있다.

# In[20]:

stats.norm.interval(0.95, loc=ca_2014_mean, scale = ca_2014_std/np.sqrt(len(weed_ca_2014)))


# 신뢰구간 설명: Weed_Price.csv 파일에는 거래된 담배의 도매가의 일부 데이터들의 표본을 담고 있다. 
# 하지만 이 정보를 이용하여 미국 전체에서 거래된 모든 모대가에 대한 정보를 추정할 수 있다. 
# 이를 위해 표본분포를 활용하며, 앞서 구한 신뢰구간의 의미는 다음과 같다.
# 
# > 캘리포니아 주에서 2014년도에 거래된 모든 상품(HighQ) 담배(식물)의 도매가의 평균값은 앞서 구한 신뢰구간에 위치할 확률이 95%이다.
