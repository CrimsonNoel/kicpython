# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:37:24 2023

@author: KITCOOP
"""
'''
numpy 기본 함수
  np.arange(15) : 0 ~ 14까지의 숫자를 1차원 배열로 생성
  arr.reshape(3,5) : 3행5열의 2차원배열로 생성.  배열 갯수가 맞아야 함.
  arr.dtype : 배열 요소의 자료형
  arr.shape :배열 구조 행열값
  arr.ndim  : 배열의 차수
  arr.itemsize : 요소의 바이트 크기
  arr.size : 요소의 갯수
  np.zeros((행,열)) : 요소의 값이 0인 배열 생성
  np.ones((행,열)) : 요소의 값이 1인 배열 생성
                 np.ones(10,dtype=int)
  np.eye(10,10) #10행10열 단위 행렬
  np.linspace(시작값,종료값,갯수) : 시작값부터 종료값까지 갯수만큼 균등분할하는 수치
  np.pi : 원주율 상수

난수 관련 함수
   np.random.random() : 난수 발생
   np.random.default_rng(1) : seed 값 설정
   np.random.randint: 정수형 난수 리턴. 
   np.random.normal(평균,표준편차,데이터갯수) : 정규 분포 난수 생성
   np.random.choice(값의범위,선택갯수,재선택여부)
   np.random.choice(값의범위,선택갯수,확률)

통계 관련 함수
   sum,min,max,mean,std
   max(axis=1) : 행중 최대값
   max(axis=0) : 열중 최대값
   cumsum(axis=1) : 행의 누적 합계
   cumsum(axis=0) : 열의 누적 합계
   argmax(axis=1) : 행 중 최대값의 인덱스
   argmax(axis=0) : 열 중 최대값의 인덱스
   argmin(axis=1) : 행 중 최소값의 인덱스
   argmin(axis=0) : 열 중 최소값의 인덱스
   
 np.fromfunction() : 함수를 이용하여 요소의 값 설정
 arr.flat:배열의 요소들만 리턴
 np.floor: 작은 근사정수
 np.ceil : 큰 근사정수
 
 arr.ravel() #1차원배열로 변경
 arr.resize() : 배열 객체 자체를 변경

'''


## numpy : 행렬, 통계관련기본함수, 배열 기능제공하는 모듈
import numpy as np
# 배열 생성
# np.arange(15) : 0 ~ 14까지의 숫자를 1차원 배열로 생성
# reshape(3,5) : 3행 5열의 2차원 배열로 생성, 배열 갯수가 맞아야함.

np.arange(15)
a = np.arange(15).reshape(3,5)
a # 0 ~ 14 까지의 숫자를 3행 5열의 2차원 배열로 생성
type(a)

# 배열 요소의 자료형
a.dtype # int32 => 32비트, 4바이트

# 배열 형태
a.shape #(3,5) : 3행 5열 2차원 배열

np.arange(15).shape  #(15,) 1차원 배열
np.arange(15).reshape(15,1) #(15,1) 2차원 배열

# 배열의 차수
x = np.arange(15)
a.ndim #2차원
x.ndim
np.arange(15 ).ndim#1

# 리스트로 배열 생성하기
b = np.array([6,7,8])
b
type(b)

# 튜플로 배열 생성하기
c = np.array(6,7,8) #오류
c = np.array((6,7,8))
c
type(c)

# 리스트로 2차원 배열 생성하기
d = np.array([[6,7,8],[1,2,3]])
d
type(d)

# 0으로 초기화된 3행 4열 배열 e 생성하기
e = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
e
e.shape

# zero값 setting
e = np.zeros((3,4))
e
e.shape

# 모든 요소의 값이 0인 배열 100개를 1차원으로 생성하기
f = np.zeros(100)
f.shape

#1 값 setting
# 모든 요소의 값이 1인 배열100개를 1차원으로 생성하기
g = np.ones(100)
g.shape

# 1으로 초기화된 10행 10열 배열 h 생성하기
h = np.ones((10,10))
h
h.shape

# 0~9999 까지의 값을 가진 배열을 100행 100열 배열 1생성하기
i = np.arange(10000).reshape(100, 100)
i.shape
i

# 0~2까지의 숫자를 9개로 균등분할하여 배열 생성
j = np.linspace(0,2,9)
j
j.size

# 0~9까지의 숫자를 20개로 균등 분할한 배열 생성
k = np.linspace(0,9,20)
k
k.size

# wjdtngud l의 값으로 10개를 가진 배열 l
l = np.ones(10,dtype = int)
l
l.dtype

#상수값
np.pi

# 1차원 배열의 연산
a = np.array([20,30,40,50])
b = np.arange(4) # (0,1,2,3)
c = a-b # 각각의 요소들의 연산
c # array([20,29,38,47])

c = a+b #각각의 요소들을 연산
c # array([20, 31, 42, 53])

c = a*b
c # array([0, 30, 80, 150])

c = b**2 # b요소들 각각의 제곱
c

c = a < 35 # a배열의 요소를 35와 비교하여 작으면 True, 크면 False
c

# @: 행렬의 곱. dot

c = a @ b
c

'''
    a   @   b   =   c
행 [1,1]  [2,0]    [1*2+1*3][1*0+1*4]  [5,4]
행 [0,1]  [3,4]    [0*2+1*3][0*3+1*4]  [5,4]
'''
c = a.dot(b)
c

# 난수를 이용한 배열 생성
rg = np.random.default_rng(1) #seed값 설정
rg
a = rg.random((2,3)) #2행 3열배열
a

b=np.ones((2,3),dtype=int)
b
a.dtype
b.dtype

c = a+b # 실수형 = 실수형 + 정수형
c = b+a # 실수형 = 실수형 + 정수형
c

a+=b # 실수형 = 실수형 + 정수형
a
a.dtype

b+=a # 오류, 정수형 = 정수형+실수형

# a배열의 전체 요소들의 합
a.sum()
# a배열의 전체 요소들 중 최소값
a.min()
# a배열의 전체 요소들 중 최대값
a.max()
# a배열의 전체 요소들 중 평균값
a.mean()
# a배열의 전체 요소들 중 중간값
#a.median()
# a배열의 전체 요소들 중 표준편차값
a.std()
a

a = np.array([[1,2],[3,4]])
a
# a배열의 행 중 최대값
a.max(axis=1)
# a배열의 열 중 최대값
a.max(axis=0)
# a배열의 행 중 최소값
a.min(axis=1)
# a배열의 열 중 최소값
a.min(axis=0)
# a배열의 행별 합계
a.sum(axis=1) #행별 합
a.sum(axis=0) #열별 합
# a배열의 행별/열별 누적 합계
a.cumsum(axis=1)
a.cumsum(axis=0)

# 10부터 49까지의 c배열을 생성하기
c = np.arange(10,50)
c
# c 첫번째 값 출력
c[0]
# 첫번째~4번째 값 출력
c[:4] #[0]~[3]
c[0:4] #[0]~[3]
# 4번째 인덱스값을 100으로 변경
c[4] = 100
c[:5]
# 처음부터 3씩 증가하여 10인덱스까지 조회
c[:11:3]
c[:11]

# 0부터  11까지의 숫자를 3행4열 2차원 배열로 d로생성하기
d = np.arange(12).reshape(3,4)
d
# 1행 1열의 값을 조회하기
d[1,1]
d[0:2,0:2] # [0,0]~[1,1]
d[:2,:2] # [0,0]~[1,1]
d[::2,::2] # 끝까지 2씩 증가하며

# 1값으로 채워진 10행 10열 배열e생성하기
e = np.ones((10,10))
e
# e배열의 가장자리는 1로 내부는 0으로 채워진 배열로 수정하기
e[1:9,1:9] = 0
e
e = np.ones((10,10))
e[1:-1,1:-1]=0
e

# e배열과 같은 모양의 배열 f 생성하기
f = np.zeros((8,8))
f

f = np.pad(f,pad_width=1,constant_values=1)
f
f.shape

# np.fromfunction() : 함수를 이용하여 요소의 값 설정
# np.fromfunction(함수명,행렬,요소자료형)
def f(x,y) : # x:행의 인덱스, y:열의 인덱스
    return 10*x+y
'''
    f(0행,0열) : 0
    f(0행,1열) : 1
    f(0행,2열) : 2
    f(0행,3열) : 3
    f(1행,0열) : 10
    ..
    f(2행,0열) : 20
    
    g[0,1,2,3]
     [10,11,12,13]
     [20,21,22,23]
     ...

'''
g = np. fromfunction(f,(5,4),dtype=int)
g

# g배열의 0행 출력
g[0]
# g배열의 0열 출력
g[:,0] # : 모든행/ 0 0열
# g배열의 2열 출력
g[:,2]
# g배열의 0~1행 0~1열출력
g[:2,:2]

# g.flat: 배열의 요소들만 리턴
for i in g.flat:
    print(1)

# 난수를 이용하여 0~9사이의 정수값을 가진 임의의 수를 3행 4열
# 배열 생성
# np.floor : 작은 근사정수
# np.ceil : 큰 근사 정수
np.random.random((3,4))
np.random.random((3,4))*10
h=np.floor(np.random.random((3,4))*10)
h
h.ndim #x차원
h.shape# 땡행,떙열

# h배열을 1차원배열 h1 변경하기
h1 = h.ravel()  #h배열이 변경되지 않음
h1.ndim
h1.shape

# h배열을 6행2열 배열 h2변경하기
h2 = h.reshape(6,2) #h배열이 변경되지 않음
h2.shape
h.shape

# h배열 자체를 6행2열의 배열로 변경하기
h.resize(6,2)
h.shape

# h배열을 3행5열로 변경
h.reshape(3,5) # 에러 h행의 요소보다 많다 3x5 =15
h.reshape(3,4)
h.shape
h
### resize > 원본,h값이 바뀐다. 
### reshape > 원본 변경이없음

# 3행을 지정, 열을 자동 맞춤
h.reshape(3,-1) # -1을 지정하면 자동으로 맞춤***
h.reshape(4,-1).shape # -1 자동. 4x3으로 만듬
h.reshape(-1,4).shape
h

'''
    2개의 배열을 합하기
   np.vstack((i,j)) #행기준 합. 열의 갯수가 같아야 함
   np.hstack((i,j)) #열기준 합. 행의 갯수가 같아야 함.

    배열 나누기
   np.hsplit(k,3) #3개로 열을 분리. 
   np.vsplit(k,2) #2개로 행을 분리.
'''




# 0 ~ 9 사이의 정수형 난수값을 가진 2행 2열 배열 생성
# randint : 정수형 난수 리턴
i = np.random.randint(10,size=(2,2))
i
j = np.random.randint(10,size=(2,2))
j
# 2개의 배열을 합하기
np.vstack((i,j)) # 행기준 합, 열의 갯수가 같아야 함
np.hstack((i,j)) # 열기준 합, 행의 갯수가 같아야 함
# 배열 나누기
k  = np.random.randint(10,size=(2,12))
k                       
np.hsplit(k,3) # 3개로 열을 분리.
np.vsplit(k,2) # 2개로 행을 분리,
k.shape
# k 배열의 모든 요소값을 100으로 변경하기
# k=100, k 변수에 100 정수값을 저장. k값은 배열이 아님
k.shape
k[0,0] = 100
k[0,:] = 100
k[:] = 100
k[:,:] = 200
k

# 0 ~ 19사이의 임의의 정수를 가진 5행 4열 배열 1을 생성하기
l = np.random.randint(20,size=(5,4))
l
l.max()
# 각 행의 최대값들을 조회하기
l.max(axis=1)
# 각 열의 최대값들을 조회하기
l.max(axis=0)

# 각 행의 최대값의 인덱스 조회하기
l.argmax(axis=1)
# 각 열의 최대값의 인덱스 조회하기
l.argmax(axis=0)

# 각 행의 최소값의 인덱스 조회하기
l.argmin(axis=1)
# 각 열의 최소값의 인덱스 조회하기
l.argmin(axis=0)

# 단위 행렬 : 대각선(행==열) 셀의 값이 1인 배열
m = np.eye(10,10) # 10행 10열 단위 행렬
m

np.nonzero(m)
n=[1,2,0,4,0] # 리스트
type(n)
np.nonzero(n) # 요소의 값이 0이 아닌 요소의 인덱스 리턴

# 정규 분포값을 가진 임의의 수 10000개를 가진 배열
# np.random.normal : 정규분포에 맞는 난수 발생 함수
# (0,1,10000) => (평균, 표준편차, 데이터갯수) 평균이0, 표준편차가 1인 난수들
o = np.random.normal(0,1,10000)
o
o.shape

o.mean()
o.std()

# 정규분포 확인 :  히스토그램을 이용하여 확인
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus']=False #음수표시 - 설정
plt.hist(o,bins=100)

# 평균:2 표준편차:2 인 난수 10000개를 생성
p = np.random.normal(2,2,10000)
p
p.mean()
p.std()
plt.hist(p,bins=100)

# choice 함수 : 값을 선택.
#       choice(값의 범위, 선택 갯수, 재선택여부)
# (10,5,replace=False)
# 10 : 0~9사이의 값
# 5 : 5개 선택
#  replace=True | False ,  중복가능 | 중복불가
q = np.random.choice(10,5,replace=False)
q

# 1~45 사이의 수를 중복없이 6개를 선택한 r배열 생성
r = np.random.choice(45,6,replace=False)+1
r
# 정렬
r.sort()
r

# 확률 적용 선택
# choice(값의 범위, 선택갯수, 확률)
# p = [0.1,0.2,0.3,0.2,0.1,0.1]
# p의 전체 합: 1
'''
  선택수  확률    100개 선택시 추정갯수
    0     0.1     10  
    1     0.2     20  
    2     0.3     30
    3     0.2     20
    4     0.1     10
    5     0.1     10
'''
t = np.random.choice(6,100,p=[0.1,0.2,0.3,0.2,0.1,0.1]) # 0~5까지 100개 찍는데 확률이 p
                       # p = [ 0,  1,  2,  3,  4,  5] 확률
t
listt=list(t)  # 리스트 <- 배열
listt.count(0) #  어느정도 확률 따라서 숫자 갯수가 조절된다. 
listt.count(1) #  생성할때마다 배열,갯수가 달라짐.
listt.count(2) #  p확률+총갯수에 대한 비율을 어느정도 따라가지만
listt.count(3) #  매번 같진 않다.
listt.count(4) # 
listt.count(5) # 

# 0~3사이의 수를 중복없이 5개 선택
# 오류. 중복되어야 생성가능함
s = np.random.choice(4,5,replace=False) # 오류 불가능 선택
s = np.random.choice(4,5,replace=True)  # 생성
s

fruits = ["apple","banana","cherries","durian","grapes"]
u = np.random.choice(fruits,100,p=[0.1,0.2,0.3,0.2,0.2])
u
listu = list(u)
for d in fruits:
    print(d,"=",listu.count(d))

import pandas as pd
sr = pd.Series(u)
sr.value_counts()







































