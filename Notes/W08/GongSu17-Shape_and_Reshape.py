
# coding: utf-8

# # 넘파이 어레이: 어레이 모양 변경

# ## 주요 내용
# 
# 어레이의 모양(shape)을 임의로 변경시키는 방법을 다룬다. 
# 
# * reshape 함수 활용
# * 어레이 자료형의 shape 속성 활용

# In[1]:

import numpy as np


# ## reshape 함수 활용

# 먼저 1차원 어레이를 생성해보자.

# In[2]:

a_1D_array = np.arange(1,7)


# 이제 아래 모양의 어레이를 생성해보자.
# 
# $$\left [ \begin{matrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{matrix} \right ]$$

# 아래와 같이 직접 작성할 수 있다.

# In[3]:

a_2D_array_1 = np.array([[1,2], [3, 4], [5,6]])
a_2D_array_1


# 하지만 shape 속성을 변경하는 방식으로 a_1D_array로부터 구할 수도 있다.

# In[4]:

a_2D_array = np.reshape(a_1D_array, (3,2))
a_2D_array


# **주의:** 기존의 a_1D_array는 변경되지 않았다.

# In[5]:

a_1D_array


# 앞서 다룬 `reshape()` 함수는 넘파이 모듈의 함수이다.
# 하지만, 동일한 이름의 어레이 메소드가 존재한다.

# In[6]:

a_2D_array_2 = a_1D_array.reshape(2,3)
a_2D_array_2


# **주의:** `np.reshape()` 함수와 `reshape()` 메소드는 내부적으로는 동일한 함수이다.

# ### 뷰(View) 방식
# 
# reshape 함수를 이용하여 a_1D_array로부터 생성된 a_2D_array는 a_1D_array와 상호 의존적인 관계를 유지한다. 
# 따라서 a_1D_array의 특정 위치의 값이 변하면 a_2D_array에서 그 위치에 해당한 값도 동일하게 변한다.
# 이렇게 작동하는 방식을 **뷰(View) 방식**이라고 부른다. 
# 
# 뷰 방식을 이용하는 함수의 결과물은 완전히 새로운 값을 생성하는 것이 아니라 기존의 값을 지켜보면서 정해진 규칙에 따라 모양만을 바꾸어 값을 리턴하는 방식을 따른다. 
# 따라서 기존의 데이터에 변경이 발생이 발생하면 뷰 방식의 결과도 그에 상응하여 다른 값을 갖게 된다.
# 
# **주의:** 뷰 방식은 역 방향으로도 영향을 미친다.
# 예를 들어, a_2D_array의 값을 변경하면 a_1D_array의 값도 변경된다.

# In[7]:

a_2D_array[2][0] = -1
a_2D_array


# In[8]:

a_1D_array


# 뷰 방식으로 어레이의 모양을 변경하는 다양한 방식이 존재한다. 
# 대표적으로 전치행렬을 생성하는 T 속성이 그렇다.
# 
# **주의:** 전치행렬은 기존 행렬의 행과 열을 서로 바꾼 행렬이다. 예를 들어,
# `3 x 2` 행렬의 전치행렬은 `2 x 3` 행렬이 된다.
# (아래 그림 참조)
# 
# $$\left [ \begin{matrix} a_1 & a_2 \\ b_1 & b_2 \\ c_1 & c_2 \end{matrix} \right ]
# \quad\Longrightarrow\quad
# \left [ \begin{matrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \end{matrix} \right ]$$

# In[9]:

a_2D_array


# a_2D_array의 모양은 (3, 2)이며, 따라서 행과 열을 서로 바꾼 전치행렬의 모양은 (2,3)이 된다.

# In[10]:

a_transposed_2D = a_2D_array.T
a_transposed_2D


# 이제 전치행렬을 변경해보자. 

# In[11]:

a_transposed_2D[0][1] = -2
a_transposed_2D


# 그러면 원래 행렬도 동일한 방식으로 변경된다.

# In[12]:

a_2D_array


# ### 뷰 방식 사용하지 않기
# 
# 뷰 방식을 이용할 때 예상치 못한 결과를 얻을 수도 있음을 보여주는 예제가 매우 많다.
# (연습문제 참조)
# 
# 따라서 경우에 따라 뷰 방식을 따르지 않도록 설정하는 것이 필요하며, 그럴 때는 `copy()` 메소드를 활용하면 된다.
# 즉, 복사하여 완전히 분리해서 사용하도록 한다.

# In[13]:

a_transposed_2D_1 = a_2D_array.T.copy()
a_transposed_2D_1


# 이제 a_transposed_2D_1 행렬을 변경해보자.

# In[14]:

a_transposed_2D_1[0][1] = -5
a_transposed_2D_1


# 하지만 원래 행렬은 변하지 않았음을 확인할 수 있다.

# In[15]:

a_2D_array


# `np.reshape()` 함수와 `reshape()` 메소드의 경우도 동일하다.

# In[16]:

a_transposed_2D_2 = a_1D_array.reshape((3,2)).copy()
a_transposed_2D_2


# In[17]:

a_transposed_2D_2[2][1] = 0
a_transposed_2D_2


# In[18]:

a_1D_array


# In[19]:

a_transposed_2D_3 = np.reshape(a_1D_array, (3,2)).copy()
a_transposed_2D_3


# In[20]:

a_transposed_2D_3[2][0] = -8
a_transposed_2D_3


# In[21]:

a_1D_array


# ## shape 속성 활용

# 넘파이의  어레이는 가변자료형이다. 
# 즉, 어레이의 내용과 모양을 변경시킬 수 있다. 

# ### 항목 변경
# 
# 항목 변경은 인덱싱 기능을 이용한다. 
# 인덱싱에 대한 보다 자세한 설명은 다음 장에서 다루며, 
# 여기서는 리스트의 인덱싱 방식과 동일한 방식으로 설명한다.

# #### 예제
# 
# a_1D_array의 2번 인덱스 항목을 9로 변경하려면 아래와 같이 하면 된다.

# In[22]:

a_1D_array[2] = 9
a_1D_array


# #### 예제
# 
# a_2D_array의 2번 인덱스 항목의 1번 인덱스 항목을 8로 변경하려면 아래와 같이 하면 된다.

# In[23]:

a_2D_array[2][1] = 8
a_2D_array


# ### 모양 변경
# 
# 어레이 자료형의 shape 속성을 이용하여 어레이의 모양을 변경시키는 방법을 배운다.
# 
# a_1D_array는 1차원 어레이이며 길이가 6이다.

# In[24]:

a_1D_array.shape


# shape 속성값을 다른 모양으로 바꿀 수 있다. 
# 대신에, 새로 생성된 모양 역시 동일한 숫자의 항목을 포함해야 한다.

# In[25]:

a_1D_array.shape = (3,2)
a_1D_array


# `3 * 2 = 6` 임에 주의하라. 그렇지 않으면 오류가 발생한다.

# In[26]:

a_1D_array.shape = (4, 2)


# shape를 (4, 2)로 변경하면 8개의 값이 필요한데 기존에 6개의 값만 사용되었기에 오류가 발생하는 것이다.
# 
# 원래 모양으로 되돌리기 위해서는 다시 shape 을 변경시켜주면 된다.

# In[27]:

a_1D_array.shape = (6,)
a_1D_array


# ### flatten 메소드
# 
# 어떠한 모양의 어레이도 1차원 어레이로 변경시켜주는 특별한 어레이 메소드가 `flatten()` 이다.

# In[28]:

array_flattened = a_2D_array.flatten()


# In[29]:

array_flattened


# **주의:** `flatten()` 메소드는 뷰 방식으로 작동하지 않는다.

# In[30]:

array_flattened[0] = -3
array_flattened


# In[31]:

a_2D_array


# ## 연습문제

# 전치행렬이 뷰 방식에 따라 사용되기에 아래와 같은 함수를 호출할 때 조심해야 한다.
# 
# 아래 코드의 경우 두 개의 행렬을 각 항목별로 더하는 방식을 취한다.
# 따라서 행렬 `a`와 `a.T`를 인자로 입력하면 대칭행렬이 리턴되는 것을 기대할 수 있다.
# 하지만 결과는 다르게 나온다. 이유는 `a.T` 가 뷰 방식을 따르고 중첩 `for`문이 진행되는 
# 동안 항목 값들이 계속해서 변하기 때문이다.

# In[32]:

def mat_add(a, b):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a[i,j] += b[i,j]
    return a


# In[33]:

c = np.arange(9).reshape((3,3))
c


# 어레이 `c`는 다음 행렬에 대응한다. 
# 
# $$\left [ \begin{matrix} 
# 0 & 1 & 2 \\ 
# 3 & 4 & 5 \\ 
# 6 & 7 & 8
# \end{matrix} \right ]$$
# 
# 따라서 `c.T`는 다음 행렬에 대응한다. 
# 
# $$\left [ \begin{matrix} 
# 0 & 3 & 6 \\ 
# 1 & 4 & 7 \\ 
# 2 & 5 & 8
# \end{matrix} \right ]$$
# 
# 이제 `mat_add(c, c.T)`는 아래의 대칭행렬이 될 것으로 기대한다.
# 
# $$\left [ \begin{matrix} 
# 0 & 4 & 8 \\ 
# 4 & 8 & 12 \\ 
# 8 & 12 & 16
# \end{matrix} \right ]$$
# 
# 하지만 결과가 다르게 나온다.

# In[34]:

mat_add(c, c.T)


# 이유가 무엇일까? 먼저 0번 행의 경우는 예상과 일치한다.
# 그런데 1번 행부터 값이 달라졌다. 
# 이는, 예를 들어 `(i, j) = (1, 0)` 의 경우 
# `c.T[1, 0]`의 값이 `c[0, 1]`인데 0번 행을 계산하면서 값이 `1`에서 
# 이미 `4`로 변경되었기 때문이다. 
# 따라서 
# 
#     c[1,0] + c.T[1,0] = c[1,0] + c[0,1] = 3 + 4 = 7
#     
# 이 되는 것이다.    
