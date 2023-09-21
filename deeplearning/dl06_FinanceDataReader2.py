# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:26:15 2023

@author: KITCOOP
"""

import FinanceDataReader as fdr
import numpy as np
import matplotlib.pyplot as plt
import pandas as ad
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# import 하는법 찾아야한다.
def MinMaxScaler(data) : 
    # 최솟값과 최대값을 이용하여 0과 1사이의 값으로 변환
    mingap = data - np.min(data,0)
    gap = np.max(data,0) - np.min(data,0)
    # 0 으로 나누기 에러가 발생하지 않도록 ㅂ매우작은 값(1e-7)을 더해서 나눔
    return mingap/(gap + 1e-7)

# 예측 10일차 자료로 다음 주가를 예측한다
model = models.load_model("stock1.h5")
start='2023-07-10'
df = fdr.DataReader('005930',start)[:11] # 11개의 자료
df.info()

# 정규화의 구간정함
dmaxclose = np.max(df,0)['Close']
dmaxclose
dminclose = np.min(df,0)['Close']
dminclose

onedf_x = df[['Open','High','Low','Volume']][:10] # 독립변수
onedf_y = df[['Close']][-1:] # y, label

onedf_x = MinMaxScale(onedf_x)
onedf_y.Close[0]

xone = np.array(onedf_x) # dataframe --> numpy
xone.shape

onepred_y = model.predict(np.reshape(xone, (1,10,4))) # shape(1,10,4) 정함

print((onepred_y[0] * (dmaxclose - dminclose + 1e-7))+dminclose,'->',
      onedf_y.iloc[0],'KRW')
























