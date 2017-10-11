
# coding: utf-8

# # 연습문제 
# 
# 아래 문제들을 해결하는 코드를 W04-Exc.py 파일에 작성하여 제출하라.

# ### 연습 1
# 
# 양의 정수 `n`을 입력 받아 `0`과 `1` 사이의 값을 균등하게 `n`등분하는 숫자들의 
# 리스트를 리턴하는 함수 `n_divide(n)`을 작성하라. (힌트: `range` 함수 활용)
# 
# 예제: 
# 
#     In [1]: n_divide(10)  
#     out[1]: [0, 0.1, 0.2, ..., 0.9, 1]

# In[7]:

def n_divide(n):
    L = []
    for i in range(n+1):
        L.append(i * 1.0/n)
    return L

n_divide(10)


# ### 연습 2
# 
# 문장을 인자로 받으면 문장에 사용된 단어들을 차례대로 print하는 함수 
# `sen2word()` 함수를 정의하라.
# 
# 예제:
# 
#     In [1]: sen2word("I am learning Python.")    
#             I
#             am
#             learning
#             Python.
# 

# In[2]:

def sen2word(xs):
    for i in xs.split():
        print(i)
        
sen2word("I am learning Python. It's quite interesting.")


# ### 연습 3
# 
# 2보다 큰 양의 정수 `n`을 입력 받아 `n`개의 피보나찌 수열값으로 구성된 리스트를 
# 리턴하는 함수 `fibo()` 함수를 구현하라.
# 
# 피보나찌 수열은 다음과 같이 정의된다. 
# ```
# f(0) = f(1) = 1
# f(n+2) = f(n) + f(n+1)
# ```    
# 예제:
# ```
# In [13]: fibo(5)    
# out[13]: [1, 1, 2, 3, 5]
# ```

# In[8]:

def fibo(n):
    F = [1, 1]
    for i in range(2, n):
        F.append(F[i-1] + F[i-2])
    return F


# In[9]:

fibo(5)


# ### 연습 4
# 
# 이름과 점수로 구성된 길이가 2인 튜플들의 리스트를 입력받으면 점수 순서대로 
# 정렬하여 리턴하는 함수 `sort_notes()`를 작성하라.
# 단, 성적이 가장 좋은 경우가 제일 먼저 오도록 한다.
# 
# 예제:
# 
#     In [30]: sort_notes([("Lee", 45), ("Kim", 30), ("Kang", 70), ("Park", 99), ("Cho", 65)])
#     Out[30]: [("Park", 99), ("Kang", 70), ("Cho", 65), ("Lee", 45), ("Kim", 30)]

# In[5]:

def second(t):
    return t[1]

def sort_notes(xs):
    xs.sort(key=second, reverse=True)
    return xs
    
L = [("Lee", 45), ("Kim", 30), ("Kang", 70), ("Park", 99), ("Cho", 65)]
sort_notes(L)


# ### 연습 5
# 
# 리스트 `xs`를 입력 받아 `xs`의 항목 중에서 정수 또는 실수들만 모두 더하는 함수 
# `num_sum` 를 정의하라. 어떠한 부작용도 발생하지 않도록 함수를 작성해야 한다.
# 
# 예제: 
#     
#     In [19]: L = [5, 'abc', 2, [2,3]]
#              num_sum(L)
#     Out[19]: 7
#     In [20]: L
#     Out[20]: [5, 'abc', 2, [2,3]]

# In[10]:

def num_sum(xs):
    L = []
    for i in xs:
        if isinstance(i, int) or isinstance(i, float):
            L.append(i)
        else:
            pass
    return sum(L)

L = [5, 'abc', 2, [2,3]]
num_sum(L)


# In[11]:

L

