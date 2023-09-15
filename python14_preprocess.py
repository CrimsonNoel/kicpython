# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:34:09 2023

@author: KITCOOP
"""

'''
 -- 행정안전부 홈페이지 : www.mois.go.kr
   -> 정책자료 -> 주민등록인구통계 -> 연령별인구현황
   -> 계:선택, 남여구분:선택안함
   -> 연령 구분 단위 : 1세
   -> 만 연령구분 : 0세 ~ 100세이상->검색버튼클릭
   -> 전체읍면동현황 선택
   -> csv파일로 다운받기 (age.csv 파일로 이름 변경)
 -- age.csv 파일 data폴더에 저장하기
'''

import numpy as np
import csv
import re

f = open("data/age.csv")
data = csv.reader(f) #csv 형태의 파일을 읽어 저장
type(data)  #csv형태 파일  #stream 처리한다(반복자)
data
import matplotlib.pyplot as plt 
name="목포"

for row in data:  # data를 반복문으로 읽으면,
    if row[0].find(name) >= 0: # 행정구역의 내용이 존재할때
        print(row)

#             name = row[0]
# \( : 그룹 괄호가 아니고 ( 개별 문자이다
# \\d* : 숫자 0개이상
# \) : )문자
# re.sub(패턴문자,변경문자,대상문자열)
        name = (re.sub('\(\\d*\)','',row[0])) # 조건에 맞는 동 선택?.. 전체가아닌 한번만 찍힌다
        # 숫자자리수 나타내는 , 제거?
        row = list(map((lambda x:x.replace(",","")),row))
        print(row)
        # 0세 컬럼 이후의 셸들을 배열 생성
        home = np.array(row[3:],dtype=int)
        print(home)

# home : 해당동의 나이별 인구수를 배열로 저장
plt.style.use('ggplot') # 스타일 설정
plt.figure(figsize=(10,5),dpi=100)
plt.rc('font',family='Malgun Gothic') #한글설정
plt.title(name+' 지역의 인구 구조')
plt.plot(home)

f = open("data/age.csv") #f : IOStream
data = csv.reader(f) #csv 형태의 파일을 읽어 저장
next(data)  # 1줄씩 읽기
data = list(data) # 파일스트림데이터를 리스트객체로 변경
                  # 파일 내용을 리스트로 저장

data
name="역삼"  # 기준이될 변수?
homelist=[] # 신사이름을 가진 행정동의 연구 데이터 목록
namelist=[] # 동이름 목록
for row in data:
    # row :  동별 인구데이터 한개.
    if(row[0].find(name) >= 0 ) * (row[0].find('동') >= 0):
        # 숫자의 ,를 제거
        row = list(map((lambda x:x.replace(",","")),row))
        # row[3:] : 0세 이후 인구목록
        homelist.append(np.array(row[3:],dtype = int))
        # 동의 이름의 '(' 이전부분만 이름 목록에 추가
        # row[0] = 서울특별시종로구 (1111000000)
        # row[0].find('(') : row[0] 문자열에서 '(' 문자의 인덱스
        #[0:'c'] 이전까지
        namelist.append(row[0][:row[0].find('(')])

namelist
homelist

# 시각화
plt.style.use('ggplot') # 스타일 설정
plt.figure(figsize=(10,5),dpi=100)
plt.rc('font',family='Malgun Gothic') #한글설정
plt.title(name+' 지역의 인구 구조')
for h,n in zip(homelist,namelist):
    # h : 그래프로 출력할 데이터
    # n : 동의 이름
    plt.plot(h,label=n) # 하나의그래프에서 여러개 선그래프 작성
plt.legend()    

###
# age.csv 파일을 이용하여 선택한 지역의 인구구조와 가장 비슷한 인구구조를 
# 가진 지역의 그래프와 그 지역 출력하기
# 가장 비슷한 지역 한개만 그래프로 출력
# data : 리스트 객체
data
name="역삼1동" #동명을 정확하게 # 기준이될 변수? 
for row in data:
    if name in row[0]: # row[0] 문자열에 name 포함?
        # 숫자의 ,를 제거
        row = list(map((lambda x:x.replace(",","")),row))
        # np.array(row[3:],dtype=int) : 0세이후 데이터를 배열 생성 요소는 int형으로
        # int(row[2]) : 정수형 총인구수
        # home : 0세이후 인구수를 정수형배열/총인구수 
        #        총인구수 대비 각각의 나이의 비율목록
        #        name 에 해당하는 동의 나이별 인구 비율 목록
        home = np.array(row[3:],dtype=int) / int(row[2])
        home_name = re.sub('\(\\d*\)','',row[0])

###
mn = 1
for row in data:
    row = list(map((lambda x:x.replace(",","")),row)) # , 제거
    # 현재 레코드의 인구 비율 정보
    away = np.array(row[3:],dtype=int)/int(row[2])
    # name의 동과 다른지역의 데이터의 차의 제곱의 합.
    # s값이 가장 작은 지역이 name 동과 가장 비슷한 인구구조 지역
    s = np.sum((home - away)**2)
    # s < mn : 다른지역의 오차합이 더 작은지역
    # name not in row[0] : name의 지역이 아님
    if s < mn and name not in row[0]:
        mn = s
        # result_name : 현재까지 가장 오차가 적은 지역의 이름
        result_name = re.sub('\(\\d*\)','',row[0])
        # result : 현재까지 가장 오차가 적은 지역 데이터
        result = away

# 시각화
# home : name 동의 데이터,
# home_name : name 동의 행정구역 이름
# result : data 데이터 중 가장 오차합이 가장 적은 지역 데이터
# result_name : 오차합이 작은 지역의 이름

plt.style.use('ggplot') # 스타일 설정
plt.figure(figsize=(10,5),dpi=100)
plt.rc('font',family='Malgun Gothic') #한글설정
plt.title(home_name+' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=home_name)
plt.plot(result, label = result_name)
plt.legend()    
plt.show()

import pandas as pd
# pandas로 해보기
'''

    age.csv 파일 cp949 형태의 파일임. ANSI형태 , EUC-KR, KSC5601, csv모듈, open함수를 이용한 경우 기본인코딩 cp949임,
    MAC은 기본 인코딩방식이 UTF-8임.
    
    pandas 모듈에서는 기본 인코딩 방식이 UTF-8임.
    
    thousands = "," : 숫자에 자리수 나타내는 , 를 제거함. 숫자만 나오도록
    
    index_col=0 : 0번 컬럼을 인덱스로 설정. 
                 행정구역 컬럼이 인덱스로 설정됨
                 
'''
df = pd.read_csv("data/age.csv",encoding="cp949",thousands=",",index_col=0)
df.head()
df.info()
df.columns

################################
# 자료축소
df = df.iloc[0:10] # row를 10개만 저장
df
################################

# 컬럼명을 변경
col_name = ['총인구수','연령구간인구수']
for i in range(0,101) : #0~100
    col_name.append(str(i)+'세') # ? 내가 원하는컬럼으로 정리가능할듯
col_name
df.columns = col_name
df.columns
# df의 모든 컬럼들을 총인구수로 나누기.(비율로만든다) 비율로 저장하기
df = df.div(df["총인구수"],axis=0)
df.head()
# 총인구수, 연령구간인구수 컬럼제거
del df["총인구수"],df["연령구간인구수"]
df.info()
df.count() # 컬럼의 결측갑싱 아닌 데이터의 건수
df
# 결측값을 0으로 치환
# fillna : 결측값을 다른값으로 치환
df.fillna(0,inplace=True) # 결측값을 0으로 치환
# 지정한 지역과 가장 비슷한 인구구조를 갖는 지역을 찾아 그래프로 출력하기
name = "무악"
# df.index: 행정구역명
# df.index.str : 인덱스의 이름을 문자열로 변경
# df.index.str.contains() : 선택된 이름을 포함? 지정한 이름을 가진 레코드만 True
a = df.index.str.contains(name)
a

df2 = df[a]
df2 # 지정지역데이터. a가 False기 떄문에 자료가없다. = 0 rows

names = list(df2.index)
names
names[0] = names[0][:names[0].find('(')] # :names[0].find('(') 괄호 앞까지 찾는다 그게 names[0]다 
df2.index = names
df2

# df3 : a값을 제외한 다른 데이터만 저장
b = list(map(lambda x : not x,a))
b
df3 = df[b]

### DataFrame graph(df.plot)

df3.index
names2 = list(df3.index)
names2
for index in range(0,len(names2)):
    names2[index] = names2[index][:names2[index].find('(')]
df3.index = names2
df3.index

df3.plot()  #row: index : 지역, column: 101개 (나이)
df3.T.plot()#row: 나이  column: 지역

#### 비슷한 동 찾기
mn = 1
# index : label,  content 0~100까지
for label,content in df3.T.items():
    # label : 행정돔여
    # content : 행정동 데이터
    # s : 지정된 지역과 현재데이터의 오차 합
    s = sum((content - df2.iloc[0])**2)
    if s < mn:
        mn = s;
        result = content
        name = result.name
        result.name = name[:name.find('(')]
df2.T.plot() #지정된 데이터
result.plot()
plt.legend()        



























