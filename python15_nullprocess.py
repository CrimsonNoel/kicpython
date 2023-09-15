# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:05:40 2023

@author: KITCOOP
"""

####################################
# 데이터 전처리 :  원본데이터를 원하는 형태로 변경하는 과정(결측치 처리)

import seaborn as sns
import pandas as pd
df = sns.load_dataset("titanic")
df.info()
df.deck.unique()
#deck 컬럼의 값별 건수 출력하기
df.deck.value_counts() # 결측값을 제외한 값의 건수(dropna=True)->default
df.deck.value_counts(dropna=False)# 결측값을 포함한 값의 건수
df.deck.head()
# isnull() : 결측값? 결측값인 경우 True, 일반값 : False
df.deck.head().isnull()
# notnull() : 결측값이 아니냐? 결측값인 경우 False, 일반값 : True
df.deck.head().notnull()

# 결측값의 갯수 조회
df.isnull().sum()       #컬럼별 결측값 갯수
df.isnull().sum(axis=0) #컬럼별 결측값 갯수
df.isnull().sum(axis=1) #행별 결측값 갯수

# 결측값이 아닌 갯수 조회
df.notnull().sum()
df.notnull().sum(axis=0)
df.notnull().sum(axis=1)

####################################
# dropna : 결측값 제거
#         inplace = True 있어야 자체 변경가능
# 결측값이 500개 이상인 컬럼 제거하기
# thresh = 500 : 결측값의 갯수가 500이상
df_tresh = df.dropna(axis=1,thresh=500)
df_tresh.info() # 11.deck 가 삭제되엇다.

df.info()
# 결측값을 가진 행을 제거
# subset = ["age"] : 컬럼설정.
# how = 'any'  |  'all' =  한개만결측값  |  모든값이 결측값
# axis =0 : 행
df_age = df.dropna(subset=["age"],how='any',axis=0)
df_age.info

#####################################
# fillna :  결측값을 다른값으로 치환, 
#           inplace =True 가 있어야 자체 객체 변경
# fillna(치환할값,옵션)
# 1. age 컬럼의 값이 결측값인 경우 평균 나이로 변경하기
# 1. age 컬럼의 평균나이 조회하기
age_mean = df["age"].mean()
age_mean
age_mean = df.mean()["age"]
age_mean
# 치환하기
df["age"].fillna(age_mean,inplace=True)
df.info()

# 2. embark_town 컬럼의 결측값은 빈도수가 가장 많은 데이터로 치환하기
# embark_town 중 가장 건수가 많은 값을 조회하기
# value_counts() 함수 결과의 첫번쨰 인덱스값. 가장큰수
df["embark_town"].value_counts()
most_freq = df["embark_town"].value_counts().index[0]
most_freq
# value.counts() 함수 결과의 가장 큰 값의 인덱스값
most_freq = df["embark_town"].value_counts().idxmax()
most_freq

# embark_town 컬럼의 결측값에 most_freq 값을 치환하기
# 결측값의 인덱스 조회
df[df["embark_town"].isnull()]
df.iloc[[61,829]]["embark_town"] # 결측값 확인
df["embark_town"].fillna(most_freq,inplace=True) # 결측값 수정
df.iloc[[61,829]]["embark_town"] # 결측값 변경 확인
df.info()

# embarked 컬럼을 앞의 값으로 치환하기
# 1.embarked 컬럼의 값이 결측값인 레코드 조회하기
df[df["embarked"].isnull()]
df.iloc[[61,829]]["embarked"]
df["embarked"][58:65] # 61:NAN > C
df["embarked"][825:831] # 829:NAN > Q

# 앞의 데이터로 치환하기
# method = "ffill" : 앞의 데이터로 치환
# method = "bfill" : 뒤의 데이터로 치환
# method = "backfi11" : 뒤의 데이터로 치환
df["embarked"].fillna(method="ffill",inplace=True)
df["embarked"][58:65] #61:C
df["embarked"][825:831] #829:Q

###########################################
# 중복데이터 처리
df = pd.DataFrame({"c1":['a','a','b','a','b'],
                   "c2":[1,1,1,2,2],
                   "c3":[1,1,2,2,2]})
df
# duplicated() : 중복데이터 찾기.
#                중복된 경우 중복된 두번째 데이터 부터 True리턴
#                전체 행을 비교하여 중복 검색
df_dup = df.duplicated()
df_dup
df[df_dup]  # 중복된 데이터만 조회

# c1 컬럼을 기준으로 중복 검색
col_dup = df["c1"].duplicated()
df
col_dup
df[col_dup]

# 중복된 데이터 제거하기
df
# df 데이터의 중복없는 데이터 생성하기
# df 객체, 원본이 변경되지않음 ( = new 객체 생성할 필요없다)
df2 = df.drop_duplicates()
df2
# c1,c3 컬럼을 기준으로 검색
col_dup = df[["c1","c3"]].duplicated()
col_dup
df[col_dup]
# c1,c3 컬럼을 기준으로 중복 제거하기
df3 = df.drop_duplicates(subset=["c1","c3"])
df3

# auto_mpg.csv 파일 읽기
mpg = pd.read_csv("data/auto-mpg.csv")
df = pd.read_csv("data/auto-mpg.csv")
mpg.info()
# 컬럼추가하기
# kpl : kilometer per liter mpg * 0.425
mpg["kpl"] = mpg["mpg"]*0.425
mpg.info()
mpg.kpl.head()
# kpl 컬럼의 데이터를 소숫점 1자리로 변경하기.
# 반올림하기
# round(1) : 소숫점 한자리로 반올림
mpg["kpl"] = mpg["kpl"].round(1)
mpg.kpl.head()
mpg.info()

# horsepower 컬럼의 값을 조회하기
mpg.horsepower.unique()

# 오류데이터 : ? => 처리
#           horsepower 컬럼은 숫자형
# replace 함수  : 값을 변경
# ? => 결측값 변경
# np.nan : 결측값
mpg["horsepower"].replace("?",np.nan,inplace=True)
mpg.info()

# horsepower 값이 결측값인 행 조회하기
mpg[mpg["horsepower"].isnull()]
mpg.info()
# horsepower 값이 결측값인 행 삭제하기
mpg.dropna(subset=["horsepower"],axis=0,inplace=True)
mpg.info()
# 자료형을 실수형 변환하기
# astype(자료형) : 모든 요소들은 자료형으로 변환.
mpg["horsepower"] = mpg["horsepower"].astype("float")
mpg.info()

mpg["horsepower"].describe()
mpg.describe()

################################################
# 범주형 데이터:
# origin 컬럼 : 1:USA, 2:EU 3:JAPAN
mpg["origin"].unique()
mpg["origin"].describe()
# 정수형 컬럼을 문자열 범주형 데이터로 변환
# 범주형 : category형
# 1. 정수형 데이터를 문자열형으로 변환
mpg["origin"].replace({1:"USA",2:"EU",3:"JAPAN"},inplace=True)
mpg["origin"].unique()
mpg.info()
# 2. 문자열형을 범주형으로 변환
mpg["origin"] = mpg["origin"].astype("category")
mpg.info()
# 3. 범주형을 문자열형으로 변환
mpg["origin"] = mpg["origin"].astype("str")
mpg.info()

































