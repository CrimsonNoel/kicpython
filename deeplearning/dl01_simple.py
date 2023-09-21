# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:08:54 2023

@author: KITCOOP
"""

# =============================================================================
#     인공신경망(ANN)
#         단위 : 퍼셉트론
#         
#         y = x1w1 + x2w2 +b
#         x1,x2 : 입력값, 입력층
#         y = 결과값
#         w = 가중치
#         b = 편향
# =============================================================================

import numpy as np

def AND(x1,x2) : # 1,0
    x = np.array([x1,x2]) # 입력값
    w = np.array([0.5,0.5]) # 가중치
    b = -0.8                # 편향
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else : 
        return 1
'''
AND
    (0, 0) => 0
    (0, 1) => 0
    (1, 0) => 0
    (1, 1) => 1
'''
'''
OR
    (0, 0) => 0
    (0, 1) => 1
    (1, 0) => 1
    (1, 1) => 1
'''
# 가중치를 변경함에 따라 결과값이 달라진다. 조건을 이용해서 답을 
def OR(x1,x2) : # 1,0
    x = np.array([x1,x2]) # 입력값
    w = np.array([0.5,0.5]) # 가중치
    b = -0.2                # 편향
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else : 
        return 1


for xs in [(0,0),(0,1),(1,0),(1,1)]:
    y = AND(xs[0],xs[1])
    print(xs,"=>",y)
    
for xs in [(0,0),(0,1),(1,0),(1,1)]:
    y = OR(xs[0],xs[1])
    print(xs,"=>",y) 

import tensorflow as tf
import pandas as pd
import numpy as np
    
# tensorflow 이용한 AND/OR 게이트 구현
data = np.array([[0,0],[0,1],[1,0],[1,1]])    
andlabel = np.array([[0],[0],[0],[1]])  # AND 결과데이터
orlabel = np.array([[0],[1],[1],[1]])  # OR 결과데이터
xorlabel = np.array([[0],[1],[1],[0]])  # XOR 결과데이터
    

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import mse

model = Sequential()   # 딥러닝 모델
'''
    Dense : 밀집층
        1 : 출력값의 갯수
        input_shape : 입력값의 갯수
        activation  : 활성화 함수 알고리즘
            linear  : 선형함수
            sigmoid : 0 ~ 1 사이의 값 변형
               relu : 양수인 경우 선형 함수, 음수인 경우 0
'''
model.add(Dense(1,input_shape=(2,),activation='linear'))

'''
    compile : 모델 설정, 모형 설정, 가중치 찾는 방법 설정
        optimizer = SGD() 경사하강법 알고리즘 설정,
        loss = mse : 손실함수, mse : 평균제곱오차.
                    mse 값이 가장 적은 경우의 가중치와 편향 구함
        metrics = ['acc'] : 평가 방법 지정. acc : 정확도
        => 손실함수의 값은 적은값, 정확도는 1에 가까운 가중치와 편향의 값을 찾도록 설정
'''


model.compile(optimizer=SGD(),loss=mse,metrics=['acc'])
    
# 학습하기
'''
    data : 훈련데이터
    label : 정답
    epochs = 300 : 300번 반복학습, 손실함수가 적고, 정확도가 높아지도록
    verbose = 0 : 학습과정 출력 생략
    verbose = 1 : 학습과정 상세 출력(기본값)
    verbose = 2 : 학습과정 간략 출력 
'''

# 할때마다 다른 결과가 나온다    
    
def model1(label)    :
    model.fit(data,label,epochs=300,verbose = 2)
    sol1 = model.predict(data)
    print("추정",sol1) # 추정
    print("답",label.flatten()) # input
    sol1 = [ 0 if x < 0.5 else 1 for x in sol1] # list comprehension
    print("조정값", list(sol1))
    print(model.evaluate(data,label))
    print(model.get_weights())
    
model1(andlabel)    
model1(orlabel)
model1(xorlabel)  # xor은 안된다..? 값이 조정됨

# 활성화 함수( 정규화 )
import numpy as np
# 소프트맥스 함수(Softmax function)는 로지스틱 함수의 다차원 일반화이다
# 다항 로지스틱 회귀에서 쓰이고, 인공신경망에서 확률 분포를 얻게 위한 마지막 활성함수로 많이 쓰인다.

# 코드자체에 큰의미 없다함 , 이런값이 나온다 정도
def softmax(arr):
    m = np.max(arr)
    arr = arr -m
    arr = np.exp(arr)
    return arr/np.sum(arr)
    
# 시그모이드 함수는 S자형 곡선 또는 시그모이드 곡선을 갖는 수학 함수이다.
# 시그모이드 함수의 예시로는 첫 번쨰 그림에 표시된 로지스틱 함수가 있으며 다음 수식으로 정의된다.
def sigmoid(x)    : # 0 < y < 1
    return 1/(1+np.exp(-x))
    
# ReLU 는 sparse activation (희소 활성화)를 생성한다
def relu(arr):
    return[x if x>0 else 0 for x in arr]
    
case1 = np.array([3.1,3.0,2.9])    
case2 = np.array([2.0,1.0,0,0.7])    
case3 = np.array([-2,-3,-1,3,2,0.5])    
    
print("sigmoid:",sigmoid(case1),"softmax:",softmax(case1))    
    
print("sigmoid:",sigmoid(case2),"softmax:",softmax(case2))    

print("relu",relu(case3))    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    