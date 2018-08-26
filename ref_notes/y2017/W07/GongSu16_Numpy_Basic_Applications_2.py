
# coding: utf-8

# # 넘파이 활용 기초 2

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[2]:

get_ipython().magic(u'matplotlib inline')


# ## 주요 내용
# 
# * 이미지 데이터 다루기
# 
# * 이미지 파일(png, jpg, pdf 등)을 다루는 방법을 예제를 이용하여 알아 본다.

# ## 이미지 데이터 불러오기 1
# 
# 먼저 아래 코드는 너구리 사진 데이터를 불러온다.
# 코드에 사용된 이미지 데이터는 `scipy.misc` 모듈에 포함되어 있는 `face()` 함수의 리턴값이다.
# 
# **주의:** `scipy` 모듈에 대해서는 나중에 다룬다.

# In[3]:

import scipy.misc

img = scipy.misc.face()


# `img`에 저장된 데이터를 이미지로 보는 방법은 아래와 같다.

# In[4]:

plt.imshow(img)


# `img` 변수에 저장된 값은 넘파이 어레이이다.

# In[5]:

type(img)


# 실제로 아래의 값을 갖는다.

# In[6]:

img


# 즉, `img`는 3차원 어레이이며, 각 항목의 값은 uint8, 즉 8비트 값의 (부호없는) 정수들이다.

# In[7]:

img.shape


# In[8]:

img.dtype


# ## 이미지 데이터 어레이 자료형
# 
# 8비트 값의 (부호없는) 정수형 이외에 이미지 데이터를 다루는 어레이에 사용되는 숫자들의 자료형은 아래와 같다.
# <p>
# <table cellspacing="20">
# <tr>
# <td>
# <img src="images07/img_dtypes.png", width=350>
# </td>
# </tr>
# </table>
# </p>

# ## 이미지 데이터를 사진으로 저장하기
# 
# `img`에 저장된 데이터를 실제 이미지로 변형하여 저장할 수도 있다.
# 
# 아래 코드는 `img` 변수에 저장된 넘파이 어레이를 사진으로 변경하여 `images07` 디렉토리 안에 
# `raccoon.png` 라는 파일명으로 저장하는 코드이다.

# In[9]:

from PIL import Image

raccoon = Image.fromarray(img)
raccoon.save('images07/raccoon.png')


# `raccoon.png` 파일은 정말로 동일한 이미지를 저장하고 있다.
# 
# <p>
# <table cellspacing="20">
# <tr>
# <td>
# <img src="images07/raccoon.png", width=300>
# </td>
# </tr>
# </table>
# </p>
# 

# ## 이미지 데이터 불러오기 
# 
# 이번엔 저장된 이미지 파일로부터 이미지 데이터를 불러오려면 예를 들어,
# `plt.imread()` 함수를 이용하면 된다.

# In[10]:

img_raccoon = plt.imread('images07/raccoon.png')
img_raccoon


# **주의: **  `img`와 `img_raccoon` 변수에 저장된 값들이 다르다. 
# 하지만 두 데이터는 동일한 이미지를 다루는 데이터이며, 다만 사용되는 숫자들의 자료형이 다를 뿐이다.

# **주의:** `plt.imread()` 함수는 임의의 이미지 파일을 넘파이 어레이 파일로 읽어서 리턴한다.

# In[11]:

img_raccoon.dtype


# In[12]:

plt.imshow(img_raccoon)


# ## 이미지 픽셀 정보와 3차원 어레이
# 
# `img`, `img_raccoon` 변수에 저장된 어레이의 모양(shape)은 다음과 같다.

# In[13]:

img_raccoon.shape


# 즉, 3차원 어레이이다. 3차원 어레이는 일반적으로 상상하기가 매우 어렵다.
# 하지만 사진 데이터의 경우에는 다음처럼 이해하면 매우 쉽다.
# 
# * 먼저, 해당 사진에 세로(row)를 균등하게 768개로 쪼개고, 가로(column)를 1024개로 쪼갠다.
#     그러면 `768 x 1024` 크기의 격자 모양으로 사진을 쪼개었다고 생각할 수 있다. 
# <p>
# <table cellspacing="20">
# <tr>
# <td>
# <img src="images07/pixelgrid01.png", width=250>
# </td>
# </tr>
# </table>
# </p>
# 
# * 이제 각각의 격자 칸에 픽셀(화소) 정보가 저장되며, 저장된 정보에 따라 다양한 색들이 보여진다. 
#     픽셀 정보는 RGB 정보를 담고 있으며, 
#     R은 빨강색(Red), G는 녹색(Green), B는 파랑색(Blue)을 대표한다.
# <p>
# <table cellspacing="20">
# <tr>
# <td>
# <img src="images07/pixelgrid02.gif", width=180>
# </td>
# </tr>
# </table>
# </p>
# 
# * 각 칸에 들어 있는 픽셀 정보는 길이가 3 또는 4인 어레이로 표현되어 있으며, 
#     위 너구리 사진은 아래 모양의 길이가 3인 픽셀 정보를 사용한다.
#         
#         [ 0.4627451 ,  0.60392159,  0.36078432]
#     
#     세 개 항목은 각각 R, G, B에 대한 정보이다.
#     만약에 아래 모양처럼 픽셀 정보가 길이가 4인 경우에는 마지막 항목은 색의 투명도를 나타낸다.
#     
#         [ 0.4627451 ,  0.60392159,  0.36078432, 1.0 ]

# ## 썸네일 이미지 만들기
# 
# 웹에서 작동하는 갤러리 같은 애플리케이션를 사용하다 보면 이미지의 썸네일을 많이 접하게 된다. 
# 여기서 썸네일을 만들기 위해 이미지를 어떻게 수정하는지 알아본다.
# 
# 먼저, 어떤 이미지의 썸네일은 기존 이미지의 화소수, 즉 화소의 숫자를 조정해서 만들며,
# 일반적으로 매우 화소수를 크게 줄인다.
# 그런데 화소수를 줄이면서 전체 이미지를 유지하기 위해서는 없어진 화소들을 **색 보간법**을 이용하여 픽셀 정보를 보정해야 한다. 
# 
# 일반적으로 아래 과정을 따른다. 
# 
# * 사진 크기 조정: 사진 크기를 조정하기 위해 Pillow 팩키지에 포함된 `Image` 모듈의 `open()` 함수를 이용한다.
# 
# * 색 보간법 사용: `plt.imshow()` 함수의 키워드 인자 중에서 `interpolation` 인자를 활용한다.

# ### 색 보정 미활용 경우
# 
# 먼저 색을 보정하지 않을 경우를 살펴본다. 그러면 마치 모자이크처리가 된 것처럼 보일 것이다.
# 
# 아래 코드에 사용딘 `Image.open()` 함수의 리턴값의 자료형은 이미지를 다루는 클래스이다.
# (여기서는 클래스 이름이 중요하지 않다.) 
# 그리고 해당 클래스의 썸네일(`thumnail`) 메소드를 활용하여 이미지의 화소수를 조정하는 방식을 보여준다.
# 
# `thumnail` 메소드에 사용된 두 개의 인자는 다음과 같다.
# * 첫째 인자: 화소수 지정 (세로 x 가로)
# * 둘째 인자: `Image.ANTIALIAS`는 그림을 처리하는 다양한 방법 중 하나를 나타낸다.
#     여기서는 자세히 다루지 않는다.

# In[14]:

from PIL import Image

img_raccoon_small = Image.open('images07/raccoon.png')
resized = img_raccoon_small.thumbnail((77, 103), Image.ANTIALIAS)
imgplot = plt.imshow(img_raccoon_small)


# 위 그림은 픽셀수를 줄였음에도 불구하고 원본 그림과 동일한 크기로 확대해서 보인 결과물이다.
# 따라서 모자이크처리를 한 것처럼 흐리게 보인다.
# 조정된 사진의 실제 크기는 다음과 같다.

# In[15]:

img_raccoon_small


# #### 색 보정 활용 활용
# 
# 색을 보정하는 색 보간법을 활용하려면 
# `plt.imshow()` 함수의 키워드 인자인 `interpolation` 인자를 활용한다. 
# `interpolation` 키워드 인자값으로 `nearest`, `bicubic` 등이 있으며 `bicubic`이 가장 선호되는 옵션이다.

# In[16]:

imgplot = plt.imshow(img_raccoon_small, interpolation="bicubic")


# ## 연습문제

# ### 연습
# 
# 색 보간법에 사용되는 `interpolation` 키워드의 인자값들 모두 확인해 보아라.
