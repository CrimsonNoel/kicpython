# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:45:28 2023

@author: KITCOOP
"""

'''
    pandas : 표형태의 데이터 저장 모듈,
        Series : 1차원형태의 데이터
        DataFrame : 2차원 형태(형,열)의 데이터,
                    Series 데이터의 모임.

pandas 모듈
 - 표형태(행:index,열:columns)의 데이터를 처리하기 위한 모듈
 - Series : 1차원형태의 데이터처리. DataFrame의 한개의 컬럼값들의 자료형
 - DataFrame : 표형태의 데이터처리. Series데이터의 모임.
     - 기술통계함수 : sum,mean,median,max,min,std,var,describe
     - 행의 값 : index
     - 열의 값 : columns
     - rename : index,columns의 값을 변경 함수 inplace=True : 객체자체변경
     - drop   : index,columns의 값을 제거 함수 inplace=True : 객체자체변경
     - 얕은복사 : df2 = df, df,df2객체는 물리적으로 같은 객체 
     - 깊은복사 : df3=df[:], df4=df.copy()
     
     - 한개의 컬럼조회 : df["컬럼명"], df.컬럼명 => Series 객체
     - 여러개의 컬럼조회 : df[["컬럼1","컬럼2"]] => DataFrame 객체
                          df["row1":"rown"] =>  DataFrame 객체. 범위지정
     - 행을 조회 : loc["인덱스명"], iloc[인덱스순서]                     
     - 컬럼 => 인덱스 : set_index
     - 인덱스 => 컬럼 : reset_index
     - csv 파일 읽기 : read_csv                     
     - csv 파일 쓰기 : to_csv                     
     - excel 파일 읽기 : read_excel
     - excel 파일 쓰기 : ExcelWriter > to_excel > save
     - reindex([], fill_value=0) 함수 : 인덱스 재설정. 행의 추가.
     - sort_index(ascending=False)  : 인덱스명으로 정렬
     - sort_values() : 기준컬럼의 값으로 정렬
'''

import pandas as pd 

# dictionary 데이터를 Series 데이터로..
dict_data = {'a':1, 'b':2,'c':3}
sr = pd.Series(dict_data) # Series 객체 생성
print(sr)
print(sr.index)
print(sr.values)

# 튜플 데이터를 Series 데이터로
tuple_data = ("홍길동","1991-01-25","남",True)
sr = pd.Series(tuple_data,index=["이름","생년월일","성별","학생여부"])
print(sr)
print(sr.index)
print(sr.values)

sr = pd.Series(tuple_data) # index값 없으면 0 1 2 3~ 으로들어간다 가독성down
print(sr)
print(sr.index)
print(sr.values)

# list를 Series로 만들기
list_data = ["홍길동","1991-01-25","남",True]
sr = pd.Series(list_data,index=["이름","생년월일","성별","학생여부"])
print(sr)
print(sr.index)
print(sr.values)

# Series 조회(key:index)

# 한개 값만 조회
print(sr[0])    #순서로 조회.
print(sr["이름"])    #인덱스로 조회.
print(sr.이름)    #인덱스로 조회.
print(sr[1])    #순서로 조회.
print(sr["생년월일"])    #인덱스로 조회.
print(sr.생년월일)    #인덱스로 조회.

# 여러개의 값 조회
print(sr[[0,1]])  #순서로 조회
print(sr[['이름','생년월일']]) #인덱스로 조회
#print(sr['이름','생년월일']) #KeyError: 'key of type tuple not found and not a MultiIndex'
print(sr[0:2]) #순서로 조회, 마지막값 앞까지 (끝-1)
print(sr['이름':'성별']) #인덱스 조회 마지막값 까지(끝까지)

# 데이터 프레임 객체 생성하기

# dictionary 이용 (key:columns)
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15],}
df = pd.DataFrame(dict_data)
print(df)
print("컬럼명: ",df.columns) # 열의 이름
print("인덱스명: ",df.index) # 행의 이름

# 한개 조회
df["c0"]
#df["c0"],columns=['000','111']  ?이건뭐지
type(df["c0"])
# 여러개 조회
df[["c0","c1"]]
type(df[["c0","c1"]])

# 리스트를 이용하여 데이터프레임 객체 생성
df = pd.DataFrame([[15,'남','서울중'],[17,'여','서울여고'],[17,'남','서울고']],
                  index=['홍길동','성춘향','이몽룡'],
                  columns=['나이','성별','학교'])
print(df)
print("컬럼명: ",df.columns) # 열의 이름
print("인덱스명: ",df.index) # 행의 이

# 인덱스명 변경하기
df.index=["학생1","학생2","학생3"]
print(df)
# 컬럼명 변경하기
df.columns=["age","gender","school"]
print(df)

# rename :  컬럼명,인덱스명의 일부만 변경하기
# inplace = True : 객체 자체 변경
# rename 에서 변경 자료는 dictionary임
df.rename(columns={"age":" 학생나이"},inplace=True) # default는 inplace=false
print(df)
#inplace=True 사용하지 않으면, df= 대입구문이 대체 효과
df.rename(index={"학생1":"홍길동"}) # inplace=True 효과 > 변경값 적용x
print(df)
df=df.rename(index={"학생1":"홍길동"}) # inplace=True 효과 > 변경값 적용됨.
print(df)


exam_data ={'수학':[90,80,70],'영어':[98,88,95],'음악':[85,95,100],'체육':[100,90,90]}

# 문제 exam_data를 이용하여 인덱스는 홍길동,이몽룡,김삿갓 인
#     DataFrame 객체 생성하기
#1
df = pd.DataFrame(exam_data,index=['홍길동','이몽룡','김삿갓'])
print(df)

#2
df = pd.DataFrame(exam_data)
df.index=['홍길동','이몽룡','김삿갓']
print(df)
 

# mead() : 평균
print(df.mean())
print(type(df.mean()))

# 수학평균
print("수학평균: ",df.mean()["수학"])
print("수학평균: ",df["수학"].mean()) # Series.mean() 함수
print(df["수학"].sum()) # Series 객체

# 과목별 최대점수
print(df.max())

# 수학 최대 점수
print(df.max()["수학"])
print(df["수학"].max())

# 홍길동 데이터 조회하기
df.수학
df["수학"]

# 인덱스명으로 조회하기 => 행을 값 조회. .loc 사용
# loc[인덱스명] : 인덱스에 해당하는 행을 조회
# iloc[순서] : 순서 해당하는 행을 조회
df.loc["홍길동"] # 홍길동 행(index) 조회
df.iloc[0] # 첫번째 행 조회
type(df.loc["홍길동"]) #Series 객체
df.loc["홍길동"].mean()  #평균
df.loc["홍길동"].median()#중간값

# 표준편차 : std() : sqrt((평균값 - 값)** 2 합계)
#                   sqrt(분산)
# 분산 : var()
# 분산 : 편차의 평균여고
# 표준편차는  sqrt(분산

# 기술통계 => 기본적인 수치데이터 조회
df.describe()
type(df.describe())
# 수학 통계정보
df.describe()["수학"]
df["수학"].describe()
# 간략정보
df.info()
df["수학"].info()
# 데이터의 처음 일부(default=5개) 조회
df.head()
# 데이터의 마지막 5개 조회
df.tail()

# 김삿갓의 총점, 평균, 중간값, 표준편차를 조회하기
df.loc["김삿갓"]
print("총점: ",df.loc["김삿갓"].sum())
print("평균: ",df.loc["김삿갓"].mean())
print("평균(?): ",df.loc["김삿갓"].median())
print("표준편차: ",df.loc["김삿갓"].std())
df.loc["김삿갓"].describe()

# 데이터 프레임 복사하기
df2 = df # 얕은 복사, df,df2는 동일한 객체임
df2.info()
df
#df 데이터의 홍길동 인덱스를 홍길순으로 변경하기
df.rename(index={"홍길동":"홍길순"},inplace=True)
df
df2

# 깊은 복사 : 두개 객체가 다른 객체
df3 = df[:] # 깊은 복사. [:] 범위 지정. 전체영역
# df 데이터의 홍길순 인덱스를 홍길홍으로 변경하기
df.rename(index={"홍길순":"홍길동"},inplace=True)
df
df3
# copy() : 깊은복사
df4 = df.copy()
df4
df4.rename(index={"홍길동":"aaaaaaaaaaa"},inplace=True)
df4

# drop() : 행,열 제거하기
# axis = 0 : 행을 의미
# axis = 1 : 열을 의미
# 행 제거하기
df3.drop(["홍길순"],axis=0,inplace=True)
df3

# 열 제거하기
df3.drop(["체육"],axis=1,inplace=True)
df3

# 열 제거하기
del df3["음악"]
df3

# copy() : 깊은 복사
df4 = df.copy()
df4
# df4에서 음삭,체육 제거하기
del df4["음악"],df4["체육"]
df4
df4 = df.copy()
df4
df4.drop(["음악","체육"], axis=1, inplace=True)
df4


# DataFrame 조회하기
# df 데이터의 수학, 영어 컬럼 조회하기
df[["수학","영어"]]
df["수학","영어"] # 에러,KeyError
# df 데이터의 수학 컬럼 조회하기
df["수학"]          #Series 객체
df[["수학"]]        #DataFrame 객체
type(df["수학"])    #Series 객체
type(df[["수학"]])  #DataFrame 객체

# df 데이터의 이몽룡(row, index) 학생 점수 조회하기
df.loc["이몽룡"] #인덱스 이름
df
df.iloc[1] # 순서 조회
# df 데이터의 이몽룡, 김삿갓 학생 점수 조회하기
df.loc[["이몽룡","김삿갓"]] #인덱스 이름
df.iloc[[1,2]] #순서 조회
df.iloc[1:2]   #순서 조회
# 범위로 조회하기
df.loc["이몽룡":"김삿갓"] #이몽룡부터 김삿갓까지
df.loc["이몽룡":] #이몽룡부터 끝까지
df.loc[:"이몽룡"] #처음부터이묭롱까지
df.loc[:] #처음부터 끝까지
df.loc[::2] #처음부터 끝까지 2칸씩 조회
df.loc[::-1] #처음부터 끝까지 역순으로

df.iloc[1:3] #1번부터 2까지
df.iloc[1:] #1번부터 끝까지
df.iloc[:2] #처음부터 1번까지
df.iloc[:] #처음부터 끝까지
df.iloc[::2] #처음부터 끝까지 2칸씩 조회
df.iloc[::-1] #처음부터 끝까지 역순으로

# 이몽룡의 수학,영어 점수 조회하기
# df.loc["문자"] #Series 객체
# df.loc[list #DataFrame 객체
df.loc["이몽룡"][["수학","영어"]] #Series 객체
df.loc["이몽룡",["수학","영어"]]
df.loc[["이몽룡"],["수학","영어"]] #DataFrame 객체
df.loc[["이몽룡"]][["수학","영어"]] #DataFrame 객체

df[:] #컬럼만 조회
df.loc[::-1] #df.loc[행의범위,열의범위]
df.iloc[:1,:1]
df.iloc[:1,:-1]
df.iloc[:-1,:-1]
df.iloc[::-1,:-1]
df.iloc[::-1,::-1]

# read_csv : jeju1.csv 파일 읽어 DataFrame 객체로 생성
df = pd.read_csv("data/jeju1.csv")
type(df)
df.info()   #간략정보
df.head()   #상위 5건 조회
df.tail()   #하위 5건 조회
df
# 장소만 조회하기
df.장소
df["장소"]
df[["장소"]]
type(df.장소)
type(df["장소"])
type(df[["장소"]])

# LON,LAT만 조회하기
df[["LON","LAT"]]
df
df.index
# set_index : "장소" 컬럼을 인덱스로 변경하기
df.set_index("장소",inplace=True)
df
df.info()

# 돔베돈의 경도 위도 조회하기
df.loc["돔베돈"]
df.loc[["돔베돈"]]
df.index

# 인덱스 값을 여행지 컬럼으로 추가하기
# 컬럼추가: DataFrame[새로운컬럼명] = 값
# 컬럼수정: DataFrame[기존컬럼명] = 값
df["여행지"] = df.index
df
df.info()

# 현재의 index 값을 컬럼으로 변경하기
df.reset_index(inplace=True)
df.info()
df
df.index

# 장소 컬럼 제거하기
df.drop("장소",axis=1,inplace=True)
df

# df데이터 내용을 csv 파일로 저장하기
# to_csv("파일이름", index=False)
# index=False : 인덱스는 파일에 저장 안함
#               기본값 True
df.to_csv("data/df_jeju1.csv",index=False) #index 제외
df.to_csv("data/jeju2.csv") #index 포함

# Excel 파일 읽기
'''
    read_excel("파일이름","sheet이름","인덱스컬럼")
    ("data/sales_2015.xlsx","january_2015",index_col=None)
    => data/sales_2015.xlxx 파일에서 january_2015 sheet 데이터의 읽기.
    인덱스컬럼 설정안함
    
    sheet_name = None : sheet 이름 지정안함
                        모든 sheet 읽음
'''


# 한개의 sheet 읽기
df = pd.read_excel("data/sales_2015.xlsx","january_2015",index_col=None)
type(df) # DataFrame 객체
df
df.info()

# 모든 sheet 읽기(마지막 자료만 저장됨)
df = pd.read_excel("data/sales_2015.xlsx",sheet_name=None,index_col=None)
df
type(df) # dictionary
'''
    {"sheet이름": DataFrame 데이터, ...}
'''
i=0
dfall=0
for name,data in df.items():
    print("sheet이름: ",name)
    print("data의 자료형: ",type(data))
    
    if i == 0:
        dfall = data
    else:
        dfall = pd.concat([dfall,data],axis=0)
        #axis = 0 index(row), 1 column 
    i=i+1
    
    print(dfall)
    
# 조건에 의한 조회

# Sale Amount 컬럼의 값이 500보다 큰 레코드만 조회
dfall[dfall["Sale Amount"]>500]
dfall.loc[dfall["Sale Amount"]>500]

dfall["Sale Amount"]>500 #True, False 값들

# Sale Amount 가 500보다 레코드만 df500 데이터에 저장
df500 = data[data["Sale Amount"] > 500]
df500 #DataFrame 객체
# df500 데이터를 pd_sale_2015.xlsx 파일의
# 2015_500 sheet로 저장하기

# df500데이터를 pd_sale_2015.xlsx 파일의
# 2015_500 sheet로 저장하기

# 내용없는 파일
outexcel = pd.ExcelWriter("data/pd_sale_2015.xlsx")

df500.to_excel(outexcel, sheet_name="2015_500",index=False)
dfall.to_excel(outexcel, sheet_name="2015",index=False)
outexcel.save()

# 매입일자가 2015-03-17일 정보만 조회하기
df0317 = dfall[dfall["Purchase Date"] == '2015-03-17'] 
df0317

dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15],}
df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
df

# 인덱스 r0,r1,r2,r3,r4 증가
# df.index=['r0','r1','r2','r3','r4'] # 오류 발생. 행의 갯수틀림
# reindex() 함수 : 인덱스 재설정. 행의추가.
ndf = df.reindex(['r0','r1','r2','r3','r4'])
ndf

# NaN : 결측값 ( 값이 없음)
# fill_value =0 : 추가된 내용에 0 값으로 채움
ndf2 = df.reindex(['r0','r1','r2','r3','r4'],fill_value=0)
ndf2

# sort_index() : 인덱스명으로 정렬
# sort_values() : 기준컬럼의 값으로 정렬
print(df.sort_index()) # 인덱스명으로 오름차순 정렬
print(df.sort_index(ascending=False)) # 인덱스명으로 내림차순 정렬
print(ndf2.sort_index(ascending=False)) # 인덱스명으로 내림차순 정렬
# c1 컬럼의 값을 기준으로 내림차순 정렬
print(df.sort_values(by="c1",ascending=False))

exam_data={"이름":["서준","우현","인아"],
           "수학":[90,80,70],
           "영어":[98,89,95],
           "음악":[85,95,100],
           "체육":[100,90,90]}

df = pd.DataFrame(exam_data)
df
#1. 이름 컬럼을 인덱스로 설정하기
df.set_index("이름",inplace=True) #이름 컬럼을 인덱스로 수정
df
# 이름의 역순으로 정렬하기
df.sort_index(ascending=False,inplace=True)
df
df# 영어 점수의 역순으로 정렬하기
df.info()
df.sort_values(by="영어",ascending=False,inplace=True)
df
df.sort_values(by="음악",ascending=False,inplace=True)
df
# 총점 컬럼 생성하여, 총점의 역순으로 출력하기
df["총점"]=df["수학"]+df["영어"]+df["음악"]+df["체육"]
df
df.sort_values(by="총점",ascending=False,inplace=True)
df


df = pd.DataFrame([[90,75,95],[95,85,70],[80,85,72]],
                  index=['홍길동','김삿갓','이몽룡'],
                  columns=['알고리즘','파이썬','R'])
df
df["파이썬"]
df["파이썬"].median()
df["R"].std()
df.loc["홍길동"].sum()/len(df.loc["홍길동"])

df[1:3].sum()
df.iloc[0:].sum()
df[:].corr()















































