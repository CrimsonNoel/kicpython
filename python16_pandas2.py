# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:39:55 2023

@author: KITCOOP
"""
'''
  데이터 전처리 : 원본데이터를 원하는 형태로 변경 과정. 
    1. 결측값 처리 : 값이 없는 경우.
        - isnull() : 결측값인 경우 True, 일반값인 경우 False
        - notnull() : 결측값인 경우 False, 일반값인 경우 True
        - dropna() : 결측값 제거 함수
              dropna(axis=1,thresh=500) : 결측값이 500개 이상인 컬럼 제거
              dropna(subset=[컬럼명],how=any/all, axis=0) :결측값을 가지고 있는 행 제거
                                              any:한개라도 결측값.
                                              all:모두 결측값
        - fillna() :결측값 치환
           fillna(치환값,inplace=True)
           fillna(방법,inplace=True) : method="ffill"/"bfill" :앞의값/뒤의값
           
    2. 중복데이터 처리 
       - duplicated() : 중복데이터 찾기. 첫번째 데이터는 False, 
                        같은 데이터인 경우 두번째 True       
       - drop_duplicates() : 중복데이터를 제거. 중복된 데이터 중 한개는 남김.

    3. 새로운 컬럼 생성
       - df[컬럼명] : 컬럼명이 없는 경우 생성, 있으면 수정.
       - round(자리수) : 반올림.    

    4. 오류데이터 존재.
       - 결측값 치환 : 결측값(np.nan) 
                 replace(오류문자열, np.nan, inplace=True)
''' 
'''
    groupby관련해서
    https://teddylee777.github.io/pandas/pandas-groupby/
    여기 읽어보기 
'''
import pandas as pd

# 범주형 : 값의 범위 가지고 있는 자료형.
#         값의 크기와 상관 없는 단수한 범위를 의미. 통계데이터 필요없음
age = pd.Series([26,42, 27, 25, 20,  20, 21, 22, 23, 25]) 
stu_class = pd.Categorical([1,1,2,2,2,3,3,4,4,4]) #정수형 범주 데이터
gender=pd.Categorical(['F','M','M','M','M','F','F','F','M','M'])
c_df = pd.DataFrame({'age':age,'class':stu_class,'gender':gender})
c_df.info()
c_df.describe()
c_df
# class 컬럼을 범주형 => 정수형
c_df["class"] = c_df["class"].astype("int") # 타입변경
c_df.info() # category>int
c_df.describe()
    
# 날짜 데이터.
# 20220101 부터 이후 6까지일 날짜를 데이터
# date_range : 날짜의 범위를 지정
# 단위 설정 
# freq = "D " : 일자기준 기본값
# freq = "M " : 월의 종료일 기준
# freq = "MS " : 월의 시작일 기준
# freq = "3M " : 3개월의 종료일 기준

dates = pd.date_range('20220101',periods=6,freq="D")
dates
dates = pd.date_range('20220101',periods=6,freq="M")
dates
dates = pd.date_range('20220101',periods=6,freq="MS")
dates
dates = pd.date_range('20220101',periods=6,freq="3M")
dates
dates = pd.date_range('20220101',periods=6,freq="6M")
dates

# 주식 데이터 읽기
df = pd.read_csv("data/stock-data.csv")
df.info()
df
# 문자열 데이터를 Date 형으로 새로운 컬럼 생성하기
df["new_date"] = pd.to_datetime(df["Date"])
df
df.info()

# new_Date 컬럼에서 년,월,일 정보 각각 컬럼으로 생성하기
df["Year"] = df["new_date"].dt.year
df["Month"] = df["new_date"].dt.month
df["Day"] = df["new_date"].dt.day
df.info()
df

# 월별 평균값 조회하기
df.groupby("Month").mean()[["Close","Start","Volume"]]

# new_date 컬럼을 문자열형으로 변경한 연월일 컬럼 생성하기
df["연월일"] = df["new_date"].astype("str")
df.info()
df.head()

# 연월일 에서 년,월,일 컬럼을 생성하기
df["연월일"].str.split("-").str.get(0)
df["년"] = df["연월일"].str.split("-").str.get(0)
df["월"] = df["연월일"].str.split("-").str.get(1)
df["일"] = df["연월일"].str.split("-").str.get(2)
df.head()
df.info()

##############################
# groupby 함수 : 컬럼으로 데이터 분리
import seaborn as sns
titanic = sns.load_dataset("titanic")

# class 컬럼으로 데이터 분할하기
# class 컬럼의 값으로 데이터를 분리
grouped = titanic.groupby("class")
grouped

for key,group in grouped : 
    print("====key",key,end=",") # class 컬럼의 값
    print("====cnt",len(group),type(group)) # DataFrame 객체
    print(group)
    
titanic["class"].value_counts()

grouped.mean()
titanic.groupby("class").mean()

# 3등석 데이터만 조회하기
group3 = grouped.get_group("Third")
type(group3)
group3.info()

# class,sex 컬럼으로 데이터 분할하기
grouped2 = titanic.groupby(["class","sex"])

for key,group in grouped2 : 
    print("====key",key,end=",") 
    print("====cnt",len(group),type(group)) 

# 3등석 여성 정보만 group3f 데이터에 저장하기
group3f = grouped2.get_group(('Third','female'))
group3f.info()
group3f[['class','sex']]

# class,sex 평균 구하기
grouped2.mean()
titanic.groupby(["class","sex"]).mean()

# class, sex 나이 평균 구하기
grouped2.age.mean()
titanic.groupby(["class","sex"]).age.mean()
grouped2.mean()["age"]
titanic.groupby(["class","sex"]).mean()["age"]

# 클래스별 나이가 가장 많은 나이와. 가장 적은 나이를 추렭하기
titanic.groupby("class").max()["age"]
titanic.groupby("class").age.max()
titanic.groupby("class").min()["age"]
titanic.groupby("class").age.min()
grouped.max()["age"]
grouped.min()["age"]


# 클래스별 성별 나이가 가장 많은 나이와, 가장 적은 나이를 출력하기
titanic.groupby(["class","sex"]).max()["age"]
grouped2.max()["age"]
titanic.groupby(["class","sex"]).min()["age"]
grouped2.min()["age"]

# agg(함수이름) 함수 : 여러개의 함수를 여러개의 컬럼에 적용할 수 있는 함수, 사용자 정의함수 적용
# x는 전체컬럼
def max_min(x):
    return x.max() - x.min()

agg_maxmin = grouped.agg(max_min)
agg_maxmin
grouped.max()
grouped.min()

# 요금(fare) : 평균, 최대값, 나이(age) ; 평균값
# class별 요금 나이 정보 조회하기
grouped.agg({'fare':['mean','max'],'age':'mean'})
titanic.groupby("class").agg({'fare':['mean','max'],'age':'mean'})

# filter(조건) 함수 : 그룹화된 데이터 
# grouped 데이터의 갯수가 20개 이상인 그룸만 조회하기
grouped.count()
# x : group 화된 DataFrame객체
# filter1 : First.third class 데이터만 저장
filter1 = grouped.filter(lambda x:len(x)>=200)
filter1
titanic['class'].value_counts

'''
    Third 491
    First 216
    Second 184
'''
filter1['class'].value_counts
'''
    Third 491
    First 216
    Second xxxxx 지워짐
'''


filter1.info() 
titanic.info()

filter2 = grouped.filter(lambda x:x.age.mean() < 30)
filter2['class'].value_counts()

# 두개의 DataFrame 연결하기
import pandas as pd
# stockprice.xlsx, stockvaluation.xlsx 데이터를 읽기
df1 = pd.read_excel("data/stockprice.xlsx")
df2 = pd.read_excel("data/stockvaluation.xlsx")
df1
df2

# concat(): 물리적 두개의 데이터를 연결
# df1, df2 열기준으로 연결하기
result1 = pd.concat([df1,df2],axis=1)
result1
result1.info()

#df1,df2 행기준으로 연결하기
result2 = pd.concat([df1,df2],axis=0)
result2
result2.info()

# 인덱스 숫자대신 id로 해봤다...
result10 = pd.concat([df1,df2],axis=0)
result10
result10.set_index(keys=["id"],inplace=False)
type(result10) # DataFrame 인덱스 수정

# merge : 컬럼을 기준으로 컬럼값이 같은 값인 경우 레코드를 병합,
#         sql문장의 inner join과 같은 의미
result3 = pd.merge(df1,df2) # 조인컬럼 : id의 값이 같은때
result3
result3.info()  # df1.id == df2.id 인것이 5개임
type(result3)
df1
df2

result3 = pd.merge(df1,df2,on="id")
result3.info()
result3

# outer merge
# how = "left" : 왼쪽 데이터는 조인되는 값이 없어도 선택. left outer join
# df1은 모든 데이터 조회, df2는 df1과 id값이 같은 데이터만 조회
# df1, df2 모두 존재하는 데이터 병합
# df1(왼쪽데이터) 만 있는 데이터는 df2(d오른쪽)의 컬럼값은 NaN임

result4 = pd.merge(df1,df2,on="id",how="left")
result4
df1

# df1(왼쪽데이터),df2(오른쪽데이터) id 컬럼이 같은 경우 데이터 병합하기
# 단 df2의 모든 데이터는 조회되도록 하기
# how="right" : 오른쪽데이터는 모두 조회.right outer join
result5 = pd.merge(df1,df2,on="id",how="right")
result5.set_index(keys=["id"],inplace=False)
result5
type(result5)

# how="outer" full outer join
result6 = pd.merge(df1,df2,on="id",how="outer")
result6

# 다른컬럼으로 병합하기
'''
    left_on="stock_name" : 왼쪽데이터(df1)의 컬럼 중 stock_name 컬럼을 조인컬럼으로 설정
    right_on="name"      : 오른쪽테이터(df2)의 컬럼 중 name 컬럼을 조인컬럼으로 설정
'''
result7 = pd.merge(df1,df2,left_on="stock_name",right_on="name"  )
result7
df1
df2
result7.info()
result7[["stock_name","name"]]

result8 = pd.merge(df1,df2,left_on="stock_name",right_on="name" ,how="left")
result8
result8.info()

import sqlite3
conn = sqlite3.connect("mydb")
# read_sql(sql문자, 연결객체)
query_result = pd.read_sql("select * from member",conn)
type(query_result)
query_result.info()
query_result
conn.close()

import cx_Oracle as co
# 오라클과 연동하기
conn = co.connect("kic","1111","localhost/xe")
query_result = pd.read_sql("select * from board",conn)
conn.close()
query_result
query_result.info()




















































