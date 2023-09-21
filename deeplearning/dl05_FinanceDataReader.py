# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:41:17 2023

@author: KITCOOP
"""
'''
1) pip install -U finance-datareader (anaconda prompt))
종목 코드 거래소별 전체 종목코드: 
    KRX (KOSPI, KODAQ, KONEX), 
    NASDAQ, NYSE, AMEX, S&P 500 
    가격 데이터 해외주식 가격 데이터:
  
        
AAPL(애플), AMZN(아마존), GOOG(구글) 
005930(삼성전자), 091990(셀트리온헬스케어) 
KS11(코스피지수), KQ11(코스닥지수), DJI(다우지수), 
IXIC(나스닥 지수), US500(S&P 5000) 
환율 데이터: USD/KRX (원달러 환율), 
USD/EUR(달러당 유로화 환율), 
CNY/KRW: 위엔화 원화 환율 
암호화폐 가격: BTC/USD (비트코인 달러 가격, Bitfinex), 
BTC/KRW (비트코인 원화 가격, 빗썸)

2023-08 

주가 분석 project
1) pip install -U finance-datareader   : ok
    Successfully installed finance-datareader-0.9.50
2) pip install tensorflow
   Successfully installed 
   astunparse-1.6.3 
   cachetools-5.3.1 
   gast-0.4.0 
   google-auth-2.22.0 
   google-auth-oauthlib-1.0.0 
   google-pasta-0.2.0 
   grpcio-1.57.0 keras-2.13.1 
   libclang-16.0.6 oauthlib-3.2.2 
   opt-einsum-3.3.0 requests-oauthlib-1.3.1 
   rsa-4.9 tensorboard-2.13.0 
   tensorboard-data-server-0.7.1 
   tensorflow-2.13.0 tensorflow-estimator-2.13.0 
   tensorflow-intel-2.13.0 
   tensorflow-io-gcs-filesystem-0.31.0 termcolor-2.3.0
'''
import FinanceDataReader as fdr
import numpy as np
import matplotlib.pyplot as plt
import pandas as ad

# from stockmodule import MinMaxScaler
fdr.__version__

# 1. 데이터 수집
# 거래소 상장종목
df_nas = fdr.StockListing('NASDAQ')
df_nas.head()
len(df_nas)

df_krx = fdr.StockListing('KOSPI')
df_krx.head()
len(df_krx)

# df = fdr.DataReader('종목코드','시작일','종료일')
# df = fdr.DataReader('종목코드','시작일') 이후 전체
# df = fdr.DataReader('005930','2022') # 년도별 자료 수집 가능

start = '2022-01-01'
end = '2023-07-31'
df = fdr.DataReader('005930',start,end) # 생성
df.info()
df.head()
df.shape # (390, 6)

'''
    10일간의 데이터를 가지고 종가를 예측한다는 것은 이런 의미입니다.
    6월 1일 ~ 6월 10일까지의 OHLV 데이터로
    6월 11일 종가 예측
    6월 2일 ~ 6월 11일까지의 OHLV 데이터로
    6월 12일 종가 예측
'''

dfx = df[['Open','High','Low','Volume','Close']]
dfx.info()

def MinMaxScaler(data) : 
    # 최솟값과 최대값을 이용하여 0과 1사이의 값으로 변환
    mingap = data - np.min(data,0)
    gap = np.max(data,0) - np.min(data,0)
    # 0 으로 나누기 에러가 발생하지 않도록 ㅂ매우작은 값(1e-7)을 더해서 나눔
    return mingap/(gap + 1e-7)

#minmax 정규화

dmaxclose = np.max(dfx,0)['Close']
dmaxclose
dminclose = np.min(dfx,0)['Close']
dminclose

dfx = MinMaxScaler(dfx) # 전체 자료 정규화

dfy = dfx[['Close']] # y, label
dfy
dfx = dfx[['Open','High','Low','Volume']] # 독립변수 정규화
dfx.describe

# 두 데이터를 리스트 형태로 저장
x = dfx.values.tolist()
y = dfy.values.tolist()

# 시계열 자료 추출
window_size = 10
data_x = []
data_y = []

for i in range(len(y)-window_size):
    # i + window_size 다음날 증가
    _x = x[i : i + window_size] # 다음 날 증가 ( i + windows_size) 는 포함되지 않음
    _y = y[i + window_size]     # 다음 날 증가
    data_x.append(_x)
    data_y.append(_y)
    print(i, i + window_size)

len(data_x)
len(data_x[0]) # ['Open','High','Low','Volume'] 10개
len(data_y) # close 1개
len(data_y[0])

# 훈련 데이터와 테스트 데이터를 분리
print('전체 데이터의 크기 : ',len(data_x), len(data_y))
train_size = int(len(data_y)* 0.7)

train_x = np.array(data_x[0 : train_size])
train_y = np.array(data_y[0 : train_size])

test_size = len(data_y) - train_size
test_x = np.array(data_x[train_size : len(data_x)])
test_y = np.array(data_y[train_size : len(data_y)])

print('훈련 데이터의 크기 : ', train_x.shape,train_y.shape)
print('테스트 데이터의 크기 : ', test_x.shape,test_y.shape)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# model 만들기
model = Sequential()
model.add(LSTM(units=20, activation='relu', return_sequences=True,input_shape=(10,4)))
model.add(Dropout(0.1))
model.add(LSTM(units=20,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(units=1))
model.summary()

model.compile(optimizer='adam',loss='mean_squared_error')
model.fit(train_x, train_y, epochs=70, batch_size=30)

model.evaluate(test_x,test_y,batch_size=30)

pred_y = model.predict(test_x)
pred_y
realvalue = (dmaxclose - dminclose + 1e-7) # dminclose 틀렸단다 나중에확인

# 시각화

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure()
plt.plot(test_y*(dmaxclose - dminclose + 1e-7), color='red',label='real samsung stock price')
plt.plot(pred_y*(dmaxclose - dminclose + 1e-7), color='blue',label='predicted samsung stock price')
plt.title('삼성 stock price 예측')
plt.xlabel('기간')
plt.ylabel('주가')
plt.legend()
plt.show()

# 결과 ?
print((pred_y[-1] * (dmaxclose - dminclose + 1e-7))+dminclose,'->',
      (test_y[-1] * (dmaxclose - dminclose + 1e-7))+dminclose,'KRW')

# 한개의 test자료(10일차) 예측
test_x.shape
test_x[0].shape # (10,4) test_x = 3개 test_x = 2개
onepred = model.predict(np.reshape(test_x[0],(1,10,4)))

# 1회차 예측
print((onepred[-1] * (dmaxclose - dminclose + 1e-7))+dminclose,'->',
      (test_y[0][-1] * (dmaxclose - dminclose + 1e-7))+dminclose,'KRW')

# 저장 
model.save("stock1.h5")
from tensorflow.keras import models
loadmodel = models.load_model("stock1.h5")
loadmodel

# loadmodel 확인
onepred = loadmodel.predict(np.reshape(test_x[0],(1,10,4)))

print((onepred[-1] * (dmaxclose - dminclose + 1e-7))+dminclose,'->',
      (test_y[0][-1] * (dmaxclose - dminclose + 1e-7))+dminclose,'KRW')
























































































