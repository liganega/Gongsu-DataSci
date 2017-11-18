
# coding: utf-8

# # 리스트 활용

# ## 주요 내용

# 파이썬에 내장되어 있는 컬렉션 자료형 중의 하나인 리스트(list)에 대해 알아본다.
# 
# **리스트(lists)**: 파이썬에서 사용할 수 있는 **임의의** 값들을 모아서 
# 하나의 값으로 취급하는 자료형
# 
# * 사용 형태: 대괄호 사용
# ```
# even_numbers_list = [2, 4, 6, 8, 10]
# todays_datatypes_list = ['list', 'tuple', 'dictionary']
# ```
# 
# * 특징: 임의의 자료형 값들을 섞어서 항목으로 사용 가능
# ```
# mixed_list = [1, 'abs', [2.1, 4.5]]
# ```
# 
# * 인덱스 또는 슬라이싱을 이용하여 각각의 항목에 또는 여러 개의 항목에 대한 
#     정보를 활용할 수 있다. 사용법은 문자열의 경우와 동일.
# 
# * 리스트는 수정 가능하다. 즉, 가변 자료형이다. 
# 
# * 리스트와 관련되어 많이 사용되는 메소드는 다음과 같다.
#     * `append()`: 기존의 리스트 끝에 항목 추가
#     * `extend()`: 두 개의 리스트 이어붙이기
#     * `insert()`: 기존의 리스트 중간에 항목 삽입
#     * `pop()`, `remove()`, `del`: 항목 삭제
#     * `count()`: 리스트에 포함된 특정 항목이 몇 번 나타나는지 세어 줌.
#     * `index()`: 특정 항목의 인덱스가 몇 번인지 확인해 줌.

# ## 오늘의 주요 예제
# 
# `Sample_Data/Swim_Records` 디렉토리에 위치한
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
# 
# 목표: 위 파일로부터 1~3등 선수의 기록을 아래와 같이 확인하기
# ```txt
# 1등 20.32 
# 2등 21.09 
# 3등 21.20 
# ```
# 
# **참조:** Head First Programming(한빛미디어) 4장

# ## 리스트 활용

# 저장된 파일에서 데이터를 불러와서 한 줄씩 확인하는 방법은 다음과 같다.
# 
# **주의:** `record_list.txt` 파일을 특정 디렉토리에 저장해야 한다.
# 아래 코드는 현재 파이썬 코드가 저장된 곳의 하위 디렉토리인 
# `Sample_Data/Swim_Records` 디렉토리에 저장되어 있는 경우를 전제로 
# 작성하였다. 
# 하위 디렉토리를 사용하지 않고 동일한 디렉토리에 저장할 경우 디렉토리를 생략해도 된다.
# 또한 다른 디렉토리에 저장하였다면 경로를 잘 명시해줘어야 한다.

# In[1]:

record_f = open("Sample_Data/Swim_Records/record_list.txt")
record = record_f.read().decode('utf-8').split('\n')
record_f.close()

for line in record:
    print(line)


# 위 코드에서 `record`에 저장된 값이 바로 리스트이다. 

# In[2]:

print(record)


# 각각의 항목은 각 줄에 위치한 선수의 이름과 기록이다.
# 예를 들어, 첫째 줄 선수의 이름과 기록은 다음과 같다.
# 
# 확인하는 방법은 인덱스를 이용한다.

# In[3]:

print(record[0])


# 각 인덱스 값의 자료형은 문자열이다.

# In[4]:

print(type(record[0]))


# 인덱스를 활용하여 모든 선수의 기록을 다음과 확인할 수 있다.
# 인덱스 활용은 앞서 문자열의 경우와 동일하다.
# 
# **주의:** 아래 코드에서 `len(record) = 8`임에 주의하라.

# In[5]:

for i in range(len(record)):
    print('---')
    print(record[i])


# ### 1~3등 점수 확인
# 
# 위 코드를 응용하여 가장 빠른 50m 기록을 확인해 보자.
# 
# 힌트: 각 선수의 정보를 담은 문자열을 스페이스 기준으로 쪼갠 후, 
# 둘 째 항목(1번 인덱스 값)의 값들 중에서 최소값을 구해야 한다.

# 견본답안: 

# In[6]:

record_f = open("Sample_Data/Swim_Records/record_list.txt", 'r')
record = record_f.read().decode('utf8').split('\n')

lowest_record = 30

for line in record:
    if float(line.split()[1]) < lowest_record: 
        lowest_record = float(line.split()[1])
record_f.close()

print(lowest_record)


# 위 코드의 5번 줄에 사용된 `line.split()`이 선수이름과 기록을 쪼개는 과정이다.
# 
# 아래 코드는 위 코드를 좀 더 세련되게 구현한 것이다. 
# 아래 코드의 5번 줄 내용은 `split()` 메소드를 이용하여 선수 이름과 기록으로 쪼개진
# 각각의 값을 갖는 변수를 동시에 선언하고 있다.
# (**주의:** `split()`의 결과로 길이가 2인 리스트를 얻는다는 것을 미리 예상하였음에 주의하라.)
# ```
# (player, p_record) = line.split()
# ```
# 위와 같이 하면 다음 처럼 한 것과 동일한 일을 하게 된다.
# ```python
# player = line.split()[0]
# p_record = line.split()[1]
# ```

# In[7]:

record_f = open("Sample_Data/Swim_Records/record_list.txt", 'r')
record = record_f.read().decode('utf8').split('\n')

lowest_record = 30

for line in record:
    (p_name, p_record) = line.split()
    if float(p_record) < lowest_record: 
        lowest_record = float(p_record)
record_f.close()

print(lowest_record)


# ### 예제
# 
# 지금까지 1등 선수의 기록을 확인하였다.
# 그렇다면 2등 선수의 기록은 어떻게 확인하는가?
# 
# 단순하게 생각해서 아래와 같이 2등 선수의 기록도 기억하는 방식으로 처리할 수 있다.

# In[8]:

record_f = open("Sample_Data/Swim_Records/record_list.txt", 'r')
record = record_f.read().decode('utf8').split('\n')

lowest_record = 30
second_lowest_record = 31

for line in record:
    (p_name, p_record) = line.split()
    if float(p_record) < lowest_record: 
        lowest_record = float(p_record)
    elif float(p_record) < second_lowest_record:
        second_lowest_record = float(p_record)
record_f.close()

print(lowest_record)
print(second_lowest_record)


# ### 예제: `append()` 메소드 활용
# 
# 3등, 4등, ... 의 기록을 위와같이 계속해서 `if... else...`문을 반복해서 구해야 하는가?
# 그렇게 할 경우 코드가 얼마나 길어져야 하는가?
# 하지만 이와 같이 하는 일에 따라 코드의 모양과 길이가 심하게 변하는 코드는 피해야 한다.
# 
# **질문:** 그렇다면 점수만 뽑아서 모은 다음에 점수들을 순서대로 나열하는 방법이 있으면 좋지 않을까?
# 
# **답:** 매우 그렇다.
# 
# **방법:** `split()`, `append()` 메소드를 아래와 같이 `for` 문과 함께 활용하면 됨.

# In[9]:

record_f = open("Sample_Data/Swim_Records/record_list.txt", 'r')
record = record_f.read().decode('utf8').split('\n')

time_only = []

for line in record:
    (p_name, p_record) = line.split()
    time_only.append(float(p_record))

record_f.close()

print(time_only)


# 위 코드는 선수이름과 시간기록을 쪼갠 후 시간기록만 따로 새로운 리스트인 `time_only`에 
# 추가하는 방식으로 저장하는 내용이다.
# 
# **주의:** 추가하기 전에 `float()` 함수를 활용하는 것이 좋다.

# 이제 위 리스트를 크기 순으로 정렬할 수 있다.

# In[10]:

time_only.sort()


# 그러면 순서가 오름차순으로 정렬된다.

# In[11]:

print(time_only)


# 이제 1, 2, 3등의 기록을 확인하기는 매우 쉽다.

# In[12]:

from __future__ import print_function

print("1등 기록은", time_only[0], "입니다.")


# In[13]:

print("2등 기록은", time_only[1], "입니다.")


# In[14]:

print("3등 기록은", time_only[2], "입니다.")


# 1~3등의 기록을 한꺼번에 확인할 수 있다.

# In[15]:

for i in range(3):
    print(i+1, "등 기록은", time_only[i], "입니다.")


# ### 예제: 슬라이싱 활용
# 
# 슬라이싱 기술은 문자열의 경우와 동일하다.
# 
# 1~3등의 기록을 다음처럼 슬라이싱을 이용하여 구할 수도 있다.

# In[16]:

first_3 = time_only[:3]

for item in first_3:
    print(item)


# 아래 방식도 가능하다.

# In[17]:

first_3 = time_only[:3]

index = 0
for item in first_3:
    print(index+1, "등 기록은", item, "입니다.")
    index += 1


# **주의:** 슬라이싱은 기존의 리스트를 변경시키지 않는다.

# In[18]:

time_only


# ## 연습문제

# ### 연습
공리스트는 아무 것도 포함하지 않는 리스트를 의미한다.
# In[19]:

empty_list = []


# 공리스트의 길이는 0이다.

# In[20]:

len(empty_list)


# 공리스튼 아무 것도 포함하지 않는다. 
# 따라서 0번 인덱스 값도 없다.

# In[21]:

empty_list[0]


# 반면에 아래 리스트는 공리스트가 아니다.

# In[22]:

a_singleton = [[]]


# 위 리스트는 공리스트를 포함한 리스트이다.
# 따라서 길이가 1이다.

# In[23]:

len(a_singleton)


# 포함된 유일한 항목은 공리스트이다.

# In[24]:

a_singleton[0]


# ### 연습

# 리스트는 중첩을 허용한다.
# 아래 리스튼 3중 리스트이다. 

# In[25]:

a_nested_list = [1, 2, [3, 4], [[5, 6, 7], 8]]


# * 첫째, 둘째 항목은 정수인 1과 2이다.
# * 셋쩨 항목은 3과 4로 이루어진 길이가 2인 리스트 `[3, 4]`이다.
# * 넷째 항목은 리스트 `[5, 6, 7]`과 정수 8로 이루어진 리스트 `[[5, 6, 7], 8]`이다.

# 질문: 위 리스트에서 2를 인덱스로 얻는 방법은?

# 견본답안:

# In[26]:

a_nested_list[1]


# 질문: `[3, 4]`를 인덱스로 얻는 방법은?

# 견본답안:

# In[27]:

a_nested_list[2]


# 질문: `3`을 인덱스로 얻는 방법은?

# 견본답안: 인덱스를 연속해서 적용한다.

# In[28]:

a_nested_list[2][0]


# 질문: `[5, 6, 7]`을 인덱스로 얻는 방법은?

# 견본답안: 역시 인덱스를 연속해서 적용한다.

# In[29]:

a_nested_list[3][0]


# 질문: `7`을 인덱스로 얻는 방법은?

# 견본답안: 역시 인덱스를 연속해서 적용한다.

# In[30]:

a_nested_list[3][0][2]


# ### 연습: 리스트의 중요 메소드 활용

# In[31]:

animals = ['dog', 'cat', 'pig']


# 문자열에 포함된 문자들의 순서가 중요하듯 리스트에 포함된 항목들의 순서도 절대적으로 중요하다.
# 문자열과는 달리 리스트는 수정이 가능하다. 

# 예를 들어, `append()` 메소드는 리스트의 끝에 항목을 하나 추가한다. 

# In[32]:

animals.append('coq')
animals


# 동시에 여러 개의 항목을 추가하고자 할 때는 `append()` 메소드를 아래처럼 이용하면 된다고 생각하면 안된다.

# In[33]:

animals.append(['eagle', 'bair'])
animals


# 위에서는 원래의 리스트에 다른 리스트 **하나**를 마지막 항목으로 추가한 것이다.
# 
# 그게 아니라 `eagle`과 `bair` 두 개의 항목을 원래의 리스트에 추가하고자 한다면 `append()` 메소드를 두 번 적용하거나
# 아니면 `extend()` 메소드를 사용하면 된다. 
# 
# 먼저 앞서 추가한 항목을 제거하자.

# In[34]:

animals.remove(['eagle', 'bair'])
animals


# `extend()` 메소드의 활용은 다음과 같다.

# In[35]:

animals.extend(['eagle', 'bair'])
animals


# 두 개의 리스트를 덧셈 기호를 이용하여 확장할 수도 있다. 하지만 원래의 리스트를 변경하는 게 아니라 새로운 리스트를 생성한다. 

# 항목 추가 및 제거 이외에도 항목 자체를 변경할 수도 있다. 
# 
# `cat`를 `cow`으로 변경해보자.
# 방법은 간단하게 인덱싱을 사용한다. 

# In[36]:

animals[1] = 'cow'
animals


# 리스트에 포함된 항목의 인덱스를 알고자 한다면 `index()` 메소드를 이용한다. 

# In[37]:

animals.index('pig')


# **주의**: 만약에 `'pig'`가 여러 번 포함되어 있으면 `index()` 메소드는 가장 작은 인덱스를 리턴한다. 

# In[38]:

animals.append('pig')
animals


# In[39]:

animals.index('pig')


# `pop()` 메소드는 인자가 없을 경우 맨 끝에 위치한 항목을 삭제하며, 인덱스를 인자로 사용하면 해당 항목을 삭제한다. 

# In[40]:

animals.pop()


# In[41]:

animals.pop(2)


# `animals`에 할당된 리스트가 어떻게 변경되었는지 확인해야 한다.

# In[42]:

animals


# 특정 인덱스 위치에 항목을 추가할 경우 `insert()` 메소드를 사용한다. 

# In[43]:

animals.insert(5, 'leopard')
animals


# **주의**: 각 메소드의 리턴값에 주의해야 한다.
# 
# * `pop()`: 리스트에서 삭제한 항목을 리턴한다.
# * `append()`, `remove()`, `insert()` 등은 기존의 리스트를 변경하지만 리턴값은 `None`, 즉 아무 것도 리턴하지 않는다. 

# **주의**: `pop()` 메소드는 인덱스를 사용하거나 아니면 맨 끝 항목만 삭제한다. 인덱스 번호를 모를 경우에 특정 항목을 삭제하고자 한다면 `remove()` 
# 메소드를 사용한다.

# In[44]:

animals.insert(2, 'hamster')
print(animals)


# In[45]:

removed_pet = animals.remove('hamster')
print(animals)


# **주의**:
# 
# * 특정 항목이 여러 번 포함되어 있을 경우 `remove()` 메소드는 맨 왼쪽에 위치한 항목 하나만 삭제한다. 
#     더 삭제하려면 또 사용해야 한다.
# 
# * `remove()`, `index()` 등은 삭제 또는 찾고자 하는 항목이 없을 경우 오류를 발생시킨다. 

# In[46]:

animals.remove('hamster')
animals


# 이외에 `del` 함수를 이용하여 리스트의 일부 또는 전체를 삭제할 수 있다. 
# 
# **주의**: `del` 함수(메소드 아님)는 매우 주의해서 사용해야 한다. 잘못하면 데이터 자체를 메모리에서 삭제시킬 수 있다. 

# In[47]:

del animals[-1]
animals


# In[48]:

animals_sample = ['dog']


# In[49]:

del animals_sample


# In[50]:

animals_sample


# `reverse()` 메소드는 리스트의 순서를 뒤집는다.

# In[51]:

print('기존 동물 리스트: ', animals)
animals.reverse()
print('뒤집어진 동물 리스트: ', animals)


# `sort()` 메소드를 이용하여 리스트의 항목들을 정렬할 수 있다. 
# 
# * 숫자의 경우는 크기 순서대로.
# * 문자열의 경우는 사전식으로.

# In[52]:

print('기존 동물 리스트', animals)
animals.sort()
print('정렬된 동물 리스트', animals)


# **주의**:
# 
# * `sort()`와 `reverse()` 메소드는 원래의 리스트 자체를 변경한다. 
# * 원래의 리스트를 건드리지 않으면서 정렬된 또는 뒤집어진 리스트를 생성하고자 한다면 `sorted()` 또는 `reversed()` 함수(메소드 아님)를 사용한다.

# In[53]:

animals.append('horse')
print(animals)
print(sorted(animals))
print(animals)


# `reversed()` 함수에 대해서는 자세히 알아보지 않는다.
