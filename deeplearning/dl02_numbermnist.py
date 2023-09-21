# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:09:45 2023

@author: KITCOOP
"""

import numpy as np
from tensorflow.keras.datasets.mnist import load_data
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from PIL import Image
from keras.models import load_model
from sklearn.metrics import classification_report,confusion_matrix

(x_train, y_train),(x_test,y_test)=load_data(path='mnist.npz')
x_train.shape # (60000, 28, 28) 훈련데이터
y_train.shape # (60000,)
x_test.shape  # (10000, 28, 28) 테스트데이터
y_test.shape  # (10000,)

# image 저장 (정규화 전 자료 저장!!) 읽어서 예측 자료로 사용

tempimg = x_test[2].reshape(28,28)
tempimg
im = Image.fromarray(tempimg)
im.save("deeplearning/images/num2.jpg","jpeg")

y_test[2] # save된 이미지의 숫자가 나옴..x_test img
# 0~59999 사이의 임의의 수 3개
random_idx = np.random.randint(60000,size=3)
for idx in random_idx:
    img = x_train[idx,:]
    label= y_train[idx]
    plt.figure()
    plt.imshow(img)
    plt.title('%d-th data,label is %d' % (idx,label),fontsize=15)

# 검증데이터 생성 : 학습 중간에 평가를 위한 데이터
x_train,x_val,y_train,y_val = train_test_split(x_train,y_train,test_size=0.3,random_state=777)
x_train.shape # (42000, 28, 28)
x_val.shape   # (18000, 28, 28)

# 데이터 정규화
'''
    MinMax normalization : X = (x-min)/(max-min) color = max 255 min 0  255-0 = 255
    Robust normalization : X = (x-중간값)/(3분위값 - 1분위값)
    Standardization      : X = x-평균값/표준편차
'''
x_train[0]

# MinMax normalization 정규화
# 현재데이터 : min:0, max=255
x_train = (x_train.reshape(42000,28*28))/255
x_val = (x_val.reshape(18000,28*28))/255
x_test = (x_test.reshape(10000,28*28))/255
x_train.shape  # (42000, 784)
x_val.shape    # (18000, 784)
x_test.shape   # (10000, 784)
y_train[:10]

# 레이블 전처리 : one-hot 인코딩하기

y_train = to_categorical(y_train)
y_train[:10]
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

# 모델 구성하기
model = Sequential()  # 모델 생성
model.add(Dense(64,activation="relu",input_shape=(784,)))
model.add(Dense(32,activation="relu"))
model.add(Dense(10,activation="softmax"))
model.summary()

'''
  1층 : 
    64 : 출력노드 갯수   
    input_shape=(784,) : 입력노드의 갯수
    activation="relu" : 활성화 함수. 0이상의 값
  2층 :
    32 : 출력노드 갯수  
    activation="relu" : 활성화 함수. 0이상의 값
    입력노드갯수 : 1층의 출력노드갯수.64개
  3층 :
    10 : 출력노드 갯수. 0~9까지의 수. 다중분류 모델  
    activation="softmax" : 활성화 함수. 
                    다중분류 방식에서 사용되는 활성화 함수
    입력노드갯수 : 2층의 출력노드갯수.32개
'''

model.compile(optimizer="adam",loss='categorical_crossentropy',metrics=['acc'])

'''
    optimizer="adam" : 경사하강법 알고리즘 이름.
                      Adam 클래스로도 가능 => import 해야함
    loss='categorical_crossentropy' : 손실함수 종류,
                                     label(정답), ont-hot 인코딩 되어야함
                        mse : 평균 제곱오차
                        categorical_crossentropy : 다중분류에서 사용되는 손실함수
                                                => 활성화함수 : softmax와 보통 같이 사용됨
                        binary_crossentropy : 이진분류에서 사용되는 손실함수 
                                                => 활성화함수 : sigmoid와 보통 같이 사용됨
                        metrics=['acc'] : 평가지표
'''

# 학습하기
history = model.fit(x_train,y_train,epochs=30,batch_size=127, validation_data=(x_val,y_val))
'''
    epochs=30 : 30번 학습하기.
    batch_size=127 : 데이터를 127개로 분리, 기본값 : 32
                    42000/127=330.70866...
    validation_data=(x_val,y_val) : 검증데이터 설정.
    history : 학습 과정을 저장한 데이터
'''

history.history["loss"] # 훈련데이터 손실함수값
len(history.history["loss"])
history.history["acc"]  # 훈련데이터 정확도
history.history["val_loss"] # 검증데이터 손실함수값
history.history["val_acc"]   # 검증데이터 정확도값
type(history.history)        # dict

#----- 
#그래프

his_dict = history.history
loss = his_dict['loss'] # 훈련데이터 학습시 손실함수값
val_loss = his_dict['val_loss'] # 검증데이터 학습시 손실함수값
epochs = range(1, len(loss) + 1) # 1 ~ 30 까지의 숫자
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(1, 2, 1) # 1행 2열의 1번쨰 그래프 영역
ax1.plot(epochs, loss, color='blue',label='train_loss')
ax1.plot(epochs, val_loss, color='orange',label='val_loss')
ax1.set_title('train and val loss')
ax1.set_xlabel('epochs')
ax1.set_ylabel('loss')
ax1.legend()

# 정확도 그래프

acc = his_dict['acc'] # 훈련데이터 정확도값
val_acc = his_dict['val_acc'] # 검증데이터 정확도값
ax2 = fig.add_subplot(1, 2, 2) # 1행 2열의 2번쨰 그래프 영역 위그래프에 더해진다
ax2.plot(epochs, acc, color='blue',label='train_acc')
ax2.plot(epochs, val_acc, color='orange',label='val_acc')
ax2.set_title('train and val acc')
ax2.set_xlabel('epochs')
ax2.set_ylabel('acc')
ax2.legend()
plt.show()

#--------

x_test.shape # 2차원
x_test[0,:].shape # 1차원
y_test[0]


# 예측하기
results = model.predict(x_test)
results[0] # [7] 99%
np.argmax(results,axis=1)[0] 
y_test[0] # 7
results[1] # [2] 100%
y_test[1] # 2
np.argmax(results,axis=1)[1]

model.evaluate(x_test,y_test)




































