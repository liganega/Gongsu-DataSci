
# coding: utf-8

# # 아나콘다(Anaconda) 소개

# ## 아나콘다 패키지 소개
# 
# * 파이썬 프로그래밍 언어 개발환경 
# * 파이썬 기본 패키지 이외에 데이터분석용 필수 패키지 포함 
# * 기본적으로 스파이더 에디터를 활용하여 강의 진행

# ## 아나콘다 패키지 다운로드
# 
# 아나콘다 패키지를 다운로드 하려면 아래 사이트를 방문한다
# 
# https://www.anaconda.com/download/
#     
# 이후 아래 그림을 참조하여 다운받는다.
# 
# #### _주의: 강의에서는 파이썬 2.7 버전을 사용한다._

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda01.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda02.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda03.PNG", height=60>
# </td>
# </tr>
# 
# </table>
# </p>
# 
# 

# ## 아나콘다 패키지 설치
# 
# 아래 그림에 표시된 부분에 주의하여 설치한다.
# 
# * 주의: 경로설정 부분은 무슨 의미인지 알고 있는 경우 체크 가능. 모르면 해제 권장.

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda04.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda05.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda06.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda07.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda08.PNG", height=60>
# </td>
# 
# </tr>
# 
# </table>
# </p>
# 
# 

# ## 스파이더(Spyder) 파이썬 편집기 실행
# 
# * 윈도우키를 누른 후 스파이더(Spyder) 선택
# * 방화벽 설정은 기본 사용
# * 업데이트 확인 부분은 체크 해제

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda09.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda10.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda11.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda12.PNG", height=60>
# </td>
# </tr>
# 
# </table>
# </p>
# 
# 

# ## 스파이더(Spyder) 파이썬 편집기 활용
# 
# * 주의: 업그레이드 확인 부분은 체크 해제할 것. 업그레이드를 임의로 하지 말 것. 
# * 스파이더는 편집기 기능과 터미널 기능을 동시에 제공
# * 편집기 부분은 긴 코드를 작성할 때 사용
# * 터미널 부분은 짧은 코드를 테스트할 때 사용

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda13.PNG", height=60>
# </td>
# </tr>
# 
# </table>
# </p>

# 실행버튼을 처음으로 눌렀을 경우 파이썬 해석기와 관련된 설정창이 뜬다. 
# 설정을 굳이 변경할 필요 없이 Run 버튼을 누른다.

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda14.PNG", height=60>
# </td>
# </tr>
# 
# </table>
# </p>

# ## 스파이더(Spyder) 파이썬 편집기 활용 예제
# 
# * 편집기 부분과 터미널 부분은 파이썬 해석기를 공유한다.
# * 편집기 부분에 코드 입력 후 실행하면, 터미널 부분에서도 편집기 부분에서 정의된 변수, 함수 등 사용 가능
# * 또한 터미널 부분에서 정의된 변수, 함수 등도 편집기에서 사용 가능.
#     * 주의: 이 방식은 추천하지 않음. 편집기 부분을 저장할 때 터미널 부분에 정의된 코드는 저장되지 않음.

# <p>
# <table cellspacing="20">
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda15.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda16.PNG", height=60>
# </td>
# </tr>
# 
# <tr>
# <td>
# <img src="../../images/anaconda/anaconda17.PNG", height=60>
# </td>
# </tr>
# 
# </table>
# </p>
# 
# 

# ## 스파이더 터미널 창에서 파이썬 코드 실행하기
# 
# 아래와 같이 명령을 바로 실행하여 결과를 확인할 수 있다.

# In[1]:

a = 2


# In[2]:

b = 3


# In[3]:

a + b


# ### 변수는 선언을 먼저 해야 사용할 수 있다.

# In[4]:

a_number * 2


# In[5]:

a_number = 5


# In[6]:

type(a_number)


# In[7]:

print(a_number)


# In[8]:

a_number * 2


# ### 간단한 코드를 작성하여 실행할 수 있다.

# In[9]:

if a_number > 2:
    print('Greater than 2!')
else:
    print('Not greater than 2!')


# ## 스파이더 에디터 창에서 파이썬 코드 작성 요령
# 
# 탭완성 기능과 다양한 단축키 기능을 활용하여 매우 효율적인 코딩을 할 수 있다.

# ### 탭완성 기능
# 
# 탭완성 기능은 편집기 및 터미널 모두에서 사용할 수 있다.

# In[10]:

# 먼저 `a_`까지만 작성한 후에 탭키를 누르면 나머지가 자동으로 완성된다. 

a_number


# ### 주석 활용
# 
# 이미 여러 번 사용했듯이 코드셀에서 샵(#)이 맨 앞에 있는 경우 해당 줄은 주석으로 처리되어 파이썬 해석기에 의해 무시된다. 
# 주석은 코드를 읽는 이들에게 코드에 대한 정보를 주기위해 사용된다.
# 주석은 보통 개발자가 직접 작성한 코드에 대해서 작성한다.
# 
# 스파이더 에디터에서 주석 처리 단축키: 주석처리하고자 하는 부분을 마우스 또는 키보드를 이용하여 설정한 후에 "Ctrl+1"
# 조합을 이용하여 주석 설정 및 해제를 실행할 수 있다.
# 
# 맥에서는 "Command+1" 조합을 사용한다.

# ### 단축키 활용
# 
# 스파이더 메뉴에 있는 항목들 마다 대부분 단축키가 설정되어 있다. 
# 반복해서 사용하는 기능은 단축키를 외워두면 매우 유용하다.
# 특히, Edit 항목에 있는 기능들은 필수적이다.
