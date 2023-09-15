# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:04:01 2023

@author: KITCOOP
"""

# seaborn 모듈 : 시각화 모듈, 데이터셋
#               mapplot 모듈 데이터 확장

'''
    빅데이터 특징
    3V
    1. Volume(규모) : 데이터의 양이 대용량
    2. Velocity(속도) : 데이터의 처리 속도가 빨라야 한다.
    3. Variety(다양성) : 데이터의 형태가 다양함.
                        정형데이터 : 데이터베이스, csv
                        반정형데이터 : json,xml,html
                        비정형데이터 : 이미지,음성
'''

#---------------------------------------------------------#
# titanic 데이터셋 연습 ( 데이터 전처리 )
# seaborn 모듈에 저장된 데이터

'''
survived   생존여부
pclass   좌석등급 (숫자)
sex   성별 (male, female)
age   나이
sibsp   형제자매 + 배우자 인원수
parch:    부모 + 자식 인원수
fare:    요금
embarked   탑승 항구
class   좌석등급 (영문)
who   성별 (man, woman)
adult_male 성인남자여부 
deck   선실 고유 번호 가장 앞자리 알파벳
embark_town   탑승 항구 (영문)
alive   생존여부 (영문)
alone   혼자인지 여부
'''

import pandas as pd
import seaborn as sns # 시각화 모듈

# seaborn 모듈에 저장된 데이터셋 목록
print(sns.get_dataset_names())

# titanic 데이터 로드.
titanic = sns.load_dataset("titanic")
titanic.info()
#
titanic.head(10)
titanic
# pclass,class 데이터만 조회하기
titanic[["pclass","class"]].head()

# 컬럼별 건수 조회하기
titanic.count() # 결측값을 제외한 데이터
# 건수 중 가장 작은 값 조회하기
titanic.count().min()
# 건수 중 가장 작은 값의 인덱스 조회하기
titanic.count().idxmin()
type(titanic.count())

# titanic의 age,fare 컬럼만을 df 데이터셋에 저장하기
df = titanic[["age","fare"]]
df.info()
# df 데이터의 평균 데이터 조회
df.mean()
# df데이터의 최대나이와 최소나이 조회
df.age.max()
df.age.min()
# 나이별 인원수를 조회. 최대 인원수를 가진 5개의 나이 조회
# 값의 갯수, 내림차순 정렬하여 조회
df.age.value_counts().head()
# 인원수가 많은 나이 10개 조회
df.age.value_counts().head(10)

# 승객 중 최고령자의 정보 조회하기
df[df["age"]==df["age"].max()]
#1
titanic[titanic["age"]==titanic["age"].max()]
#2
titanic["age"].idxmax()
titanic.iloc[titanic["age"].idxmax()]

# 데이터에서 생존건수(342), 사망건수(549) 조회하기
titanic.columns
titanic["survived"].value_counts()
titanic["alive"].value_counts()

# 성별로 인원수 조회하기
titanic["sex"].value_counts()
titanic["who"].value_counts()

# 성별로 생존건수 조회하기
cnt = titanic[["sex","survived"]].value_counts()
cnt
type(cnt)
cnt.index

# 컬럼 : 변수, 피처 용어사용.
# 상관 계수 : -1 ~ 1 사이의 값, 변수의 상관관계 수치로 표현
titanic.corr()
titanic[["survived","age"]].corr()

'''
mpg : 연비
cylinders : 실린더 수
displacement : 배기량
horsepower : 출력
weight : 차량무게
acceleration : 가속능력
model_year : 출시년도
origin : 제조국
name : 모델명
'''

#1. seaborn 데이터에서 mpg 데이터 로드하기
import seaborn as sns
mpg = sns.load_dataset("mpg")
mpg.info()

#2. 제조국별 자동차 건수 조회하기
mpg[["origin"]].value_counts()
mpg.origin.value_counts()
type(mpg)

#3. 제조국 컬럼의 값의 종류를 조회하기
# unique() : 중복을 제거하여 조회
mpg.origin.unique() #array(['usa', 'japan', 'europe'], dtype=object)
mpg.origin  #(1...398)

#4. 출시년도의 데이터 조회하기
mpg.model_year #(1...398)
mpg.model_year.unique() #array([70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], dtype=int64)

#5. mpg 데이터의 통계정보 조회하기
mpg.describe() # 숫자형태의 데이터만 조회
mpg.describe(include="all") # 모든데이터 조회
type(mpg)

# mpg 데이터의 행의값,열의값 조회
mpg.shape #(398,9) 튜플데이터 : 398행 9열
# 행의값 조회
mpg.shape[0]
# 열의값 조회
mpg.shape[1]

# 모든 컬럼의 자료형을 조회하기
mpg.dtypes

# mpg 컬럼의 자료형을 조회하기
mpg["mpg"].dtypes

#6. mpg. 데이터의 mpg.weight 컬럼의 최대값 조회하기
mpg.mpg.max()
mpg.weight.max()
mpg[["mpg","weight"]].max()

#7. mpg. 데이터의 mpg.weight 컬럼의 기술통계 정보 조회하기
mpg[["mpg","weight"]].describe(include="all")

#8. 최대 연비를 가진 자동차의 정보 조회하기
mpg[mpg["mpg"]==mpg["mpg"].max()]
mpg.loc[mpg["mpg"]==mpg["mpg"].max()]
mpg.iloc[mpg["mpg"].idxmax()] 
mpg.iloc[mpg["mpg"].idxmax()][["origin"]+["name"]+["mpg"]+["horsepower"]]
                                #[[]] dataframe 멀티인덱스?형으로 보고싶은것 +로 입력하면 따라온다

# mpg 데이터의 컬럼간의 상관계수 조회하기
mpg.corr()
# mpg.mpg, weight 데이터의 컬럼간의 상관계수 조회하기
mpg[["mpg","weight"]].corr()                                

####시각화하기
# 연비와 차량의 무게의 관계를 시각화하기
'''
    산점도: 두개의 컬럼의 각각의 값들을 x,y축에 점으로 표현
          값의 분포를 알수 있다.
          컬럼사이의 관계를 시각화 한다.
          kind = "scatter" : 산점도
'''

mpg.plot(x="mpg",y="weight",kind="scatter")
# 히스토그램 : 데이터의 반도수 시각화
#            kind = "hist"
mpg.mpg.plot(kind="hist")

# 남북한 발전전력량.xlsx 파일을 읽어 df에 저장하기
# 첫번째 sheet. sheet 가 한개만 있음.
df = pd.read_excel("data/남북한발전전력량.xlsx")
df
df.info()
df.head()
df.tail()
# 0,5 행 데이터의 2열 이후의 정보만 ndf에 저장하기
ndf = df.iloc[[0,5]]
ndf.info()
ndf.head()
ndf = df.iloc[[0,5],2:]
ndf.info()
# 선그래프 출력하기
ndf.plot() # 컬럼별 선 그래프작성
ndf.info()

# 남한,북한별로 그래프 작성필요 : 남한,북한 컬럼으로
# 행열을 바꿔야함. 행=>열, 열=>행
# 전치행렬 : 행과 열이 바뀌는 행렬. ndf.T
ndf
ndf2 = ndf.T
ndf2
ndf2.info()

# 컬럼명 변경하기
ndf2.columns=["South","North"]
ndf2.info()
ndf2

# 선그래프로 출력하기
ndf2.plot() # 범례: 컬럼명
# 막대그래프로 출력하기
ndf2.plot(kind="bar")
ndf2.info()
# 데이터 값을 정수형(숫자형)변환 - hist 그래프는 실수안된다
ndf2 = ndf2.astype(int)
ndf2.info()
ndf2
ndf = ndf.astype(int) # 컬럼이 연도별이라 컬러풀하다
# 히스토그램
ndf2.plot(kind="hist")
ndf.plot(kind="hist") # 컬럼이 연도별이라 컬러풀하다











































