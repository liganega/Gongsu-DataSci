
# coding: utf-8

# # Pandas 소개 2

# GonsSu24 내용에 이어서 Pandas 라이브러리를 소개한다.
# 
# 먼저 GongSu24를 임포트 한다.

# In[1]:

from GongSu24_Pandas_Introduction_1 import *


# ## 색인(Index) 클래스
# 
# Pandas에 정의된  색인(Index) 클래스는 Series와 DataFrame 자료형의 행과 열을 구분하는 이름들의 목록을 저장하는 데에 사용된다. 

# ### Series 객체에서 사용되는 Index 객체
# 
# * index 속성

# 아래와 같이 Series 객체를 생성한 후에 index를 확인해보자.

# In[2]:

s6 = Series(range(3), index=['a', 'b', 'c'])
s6


# index의 자료형이 Index 클래스의 객체임을 확인할 수 있다.

# In[3]:

s6_index = s6.index
s6_index


# Index 객체에 대해 인덱싱과 슬라이싱을 리스트의 경우처럼 활용할 수 있다. 

# In[4]:

s6_index[2]


# In[5]:

s6_index[1:]


# Index 객체는 불변(immutable) 자료형이다.

# In[6]:

s6_index[1] = 'd'


# 색인 객체는 변경될 수 없기에 자료 구조 사이에서 안전하게 공유될 수 있다.

# In[7]:

an_index = pd.Index(np.arange(3))
an_index


# 앞서 선언된 an_index를 새로운 Series 나 DataFrame 을 생성하는 데에 사용할 수 있으며, 사용된 index가 무엇인지를 확인할 수도 있다.

# In[8]:

s7= Series([1.5, -2.5, 0], index=an_index)
s7.index is an_index


# ### DataFrame 객체에서 사용되는 Index 객체
# 
# * index 속성
# * columns 속성

# In[9]:

df3


# columns와 index 속성 모두 Index 객체이다.

# In[10]:

df3.columns


# In[11]:

df3.index


# In[12]:

df3.columns[:2]


# #### `in` 연산자 활용하기
# 
# `in` 연산자를 활용하여 index 와 columns에 사용된 행과 열의 이름의 존재여부를 확인할 수 있다.

# In[13]:

'debt' in df3.columns


# In[14]:

'four' in df3.index


# 각각의 색인은 담고 있는 데이터에 대한 정보를 취급하는 여러 가지 메서드와 속성을 가지고 있다. [표 5-3]을 참고하자.

# ## Series와 DataFrame 관련 연산 및 주요 메소드
# 
# Series나 DataFrame 형식으로 저장된 데이터를 다루는 주요 연산 및 기능을 설명한다.

# ### 재색인(reindex) 메소드
# 
# `reindex()` 메소드는 지정된 색인을 사용해서 새로운 Series나 DataFrame 객체를 생성한다.

# #### Series의 경우 재색인

# In[15]:

s8 = Series([4.3, 9.2, 8.1, 3.9], index= ['b', 'c', 'a', 'd'])
s8


# `reindex()` 메소드를 이용하여 인덱스를 새로 지정할 수 있다. 
# 
# **주의:** 새로 사용되는 항목이 index에 추가되면 NaN이 값으로 사용된다.

# In[16]:

s9 = s8.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
s9


# 누락된 값을 지정된 값으로 채울 수도 있다.

# In[17]:

s8.reindex(['a','b','c','d','e', 'f'], fill_value=0.0)


# #### method 옵션
# 
# 시계열(time series) 등과 데이터 처럼 어떠 순서에 따라 정렬된 데이터를 재색인할 때 
# 보간법을 이용하여 누락된 값들을 채워 넣어야 하는 경우가 있다. 
# 이런 경우 method 옵션을 이용하며, `ffill`, `bfill`, `nearest` 등을 옵션값으로 활용한다.

# In[18]:

s9 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
s9


# In[19]:

s9.reindex(range(6))


# In[20]:

s9.reindex(range(6), method='ffill')


# In[21]:

s9.reindex(range(6), method='bfill')


# In[22]:

s9.reindex(range(6), method='nearest')


# #### DataFrame의 경우 재색인
# 
# 행과 열에 대해 모두 사용이 가능하다. 

# In[23]:

data = np.arange(9).reshape(3, 3)
data


# In[24]:

df6 = DataFrame(data, index=['a', 'b', 'd'], columns= ['Ohio', 'Texas', 'California'])
df6


# * index 속성의 재색인은 Series의 경우와 동일하다.

# In[25]:

df7 = df6.reindex(['a', 'b', 'c', 'd'])
df7


# * columns 속성의 재색인은 키워드(예약어)를 사용한다.

# In[26]:

states = ['Texas', 'Utah', 'California']
df6.reindex(columns=states)


# * `method` 옵션을 이용한 보간은 행 대해서만 이루어진다.

# In[27]:

df6.reindex(index=['a', 'b', 'c', 'd'], method='ffill')


# In[28]:

df6.reindex(index=['a', 'b', 'c', 'd'], method='bfill')


# In[29]:

df6.reindex(index=['a', 2, 3, 4])


# `method='nearest'`는 인덱스가 모두 숫자인 경우에만 적용할 수 있다.

# In[30]:

df6.reindex(index=['a', 'b', 'c', 'd'], method='nearest')


# #### 주의
# 
# reindex는 기존 자료를 변경하지 않는다.

# In[31]:

df6


# #### `loc` 메소드를 이용한 재색인
# 
# `loc` 메소드를 이용하여 재색인이 가능하다.

# In[32]:

states


# In[33]:

df6.loc[['a', 'b', 'c', 'd'], states]

