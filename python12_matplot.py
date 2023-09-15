# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:44:27 2023

@author: KITCOOP
"""

# matplot 시각화 모듈
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# 한글이 가능한 폰트로 설정 :  맑은 고딕, 기본폰트는 한글불가
plt.rc("font",family="Malgun Gothic")

# plot1 -start-------------------------------
# x축 데이터의 내용
subject = ["Oracle","Python","Sklearn","Tensorflow"]
# y축 데이터값
score = [65,90,85,95]
# 그래프가 그려지는 영역
fig = plt.figure()

# 그래프 영역을 분할
# ax1 : 그래프 작성 영역
#ax1 = fig.add_subplot(1,1,1) # 1행 1열 1번째 영역
ax1 = fig.add_subplot(2,1,1) # 2행 1열 1번째 영역
ax2 = fig.add_subplot(2,1,2) # 2행 1열 2번째 영역 #==> 그래프가 총 두개 생긴다
# bar(x축의값, y축의값, 가운데막대, 막대그래프색상) : 막대그래프
# x축의값 : range(len(subject)) : 0~3까지
# y축의값 : score :[65,90,85,95]
# align = "edge"/"center"
ax1.bar(range(len(subject)),score,align="center",color="darkblue")
ax2.plot(range(len(subject)),score)
# x축의 값을 숫자에서 subject의 내용으로 변경
# rotation = 45 : x축의 값 출력각도
plt.xticks(range(len(subject)),subject,rotation=0,fontsize="small")
plt.xlabel("Subject") # x축값 설명
plt.ylabel("Score")   # y축값 설명
plt.title("Class Score")
plt.show()
# --- 단일 실행말고 담을 내용 전부를 실행해야 한다
##ax1 = fig.add_subplot(2,1,1)
##ax1.bar(range(len(subject)),score,align="center",color="darkblue")
##ax1.plot(range(len(subject)),score)
##-> 막대 그래프랑 선그래프가 공존하는 plot이 그려진다(?연합그래프가 이건가?)
# plot1 -end-------------------------------

# plot2 - start--------------------------------
## 연합 그래프 그리기
df = pd.read_excel("data/남북한발전전력량.xlsx")
df.info()
df
# 북한지역 발전량만 조회.
df = df.loc[5:]
df
df.info
# 전력량(억㎾h) 컬럼 제거
# df.drop("전력량 (억㎾h)", axis=1, inplace=True)
del df["전력량 (억㎾h)"]
df.info()
df["발전 전력별"]
# 발전 전력별 컬럼을 index로 설정
df.set_index("발전 전력별",inplace=True)
df.info()
df.index
df
# 전치행렬 :  행과 열을 바꿈(.T)
df = df.T
df.info()
df
# 합계 컬럼을 총발전량 컬럼으로 변경하기
df = df.rename(columns={"합계":"총발전량"})
df.info()
df
# 총발전량 - 1년 추가: 전년도 발전량
df.head()
# shift(1) : 총발전량의 앞의 인덱스 데이터
df["전년도발전량"] = df["총발전량"].shift(1) #.fill_value=0 하면추가된 값에 0으로들어간다 ~한번해봄
df.head()
# 증감율 컬럼 추가하기
# 증감율 : (현재 - 전년도)/전년도 *100
#         (현재/전년도-1) *100
df["증감율"]=((df["총발전량"]/df["전년도발전량"])-1)*100
df.head()
df
df.loc["1990","증감율"] = '0' # nan 값을 0으로 바꿨다. 한번해봄
df.loc["1990","전년도발전량"] = '0'
##
plt.style.available # 사용 가능한 style 목록
plt.style.use("ggplot") # 그래프 스타일 선택
plt.rc("font",family="Malgun Gothic") # 한글폰트 설정 (기본은 출력안됨)
plt.rcParams['axes.unicode_minus']=False # 음수표시 설정
df[['수력','화력']] # 원자력 데이터 제외
# DataFrame.plot 함수 사용
# figsize : 그래프 영역의 크기
# width=0.7 : 막대그래프 넓이
# stacked = False : 막대그래프를 수력, 화력 따로표시
# ax1 : 막대그래프 영역
# x축값 : df.index
# y축값 : df[['수력','화력']]. 막대그래프 2개
ax1 = df[['수력','화력']].plot(kind='bar',figsize=(20,10), width=0.7, stacked=False)

# ax1 영역을 ax2와 같은 영역 설정,
# ax1, ax2 영역은 같은 영역
ax2 = ax1.twinx()

# ax2: 증감율 선 그래프 작성
# df.index : 년도 데이터를 x축값
# df.증감율 :  증감율 컬럼을 y축값
# ls = '--' : 선의 종료(--:댓쉬선, -:실선)
# marker='o' : 선의 마커 표시
# markersize=10 : 마커 크기
# label = '전년대비 증감율(%)' : 범례표시
ax2.plot(df.index, df.증감율, ls='--',marker='o',markersize=10, color='green',label='전년대비 증감율(%)')
ax1.set_ylim(0,200) # 막대그래프 y축 값의 범위
ax2.set_ylim(-50,50) # 선그래프 y축 값의 범위

ax1.set_xlabel('연도',size=20) # x축값의 설명
ax1.set_ylabel('발전량(역 KWh)') # 막대그래프 y축값의 설명
ax2.set_ylabel('전년 대비 증감율(%)') # 선그래프 y축값의 설명
plt.title('북한 전력 발전량(1990 ~ 2016)', size=30) # 전체 그래프 제목
ax1.legend(loc='upper left') #범례 : 왼쪽 위 위치
ax2.legend(loc='upper right') #범례 : 오른쪽 위 위치

# 그래프를 이미지파일로 저장.
# savefig(저장파일명, 해상도,이미지크기설정)
# plt.savefig("img/북한전력량.png",dpi=400,bbox_inches="tight") 
plt.savefig("img/북한전력량.png", bbox_inches="tight")
plt.show()
# plot2 - end--------------------------------
# plot3 - start ------------------------------

# 자동차 연비데이터의 mpg 값을 히스토그램으로 출력하기
df = sns.load_dataset("mpg")
df.info()
# 히스토그램 출력
df["mpg"].plot(kind="hist")
# 간격을 20개로 분리한 히스토그램 출력
# linewidth=1 : 막대사이간격
df["mpg"].plot(kind="hist",bins=20,color='coral',figsize=(10,5), histtype='bar',linewidth=1)
plt.title("MPG 히스토그램")
plt.xlabel("mpg(연비)")

df["mpg"].min() # 9.0
df["mpg"].max() # 46.6

# weight,mpg 데이터의 산점도 출력하기
# DataFrame.plot(kind="scatter") : 그래프 종류
# x = 'mpg' : x축의 사용될 컬럼명
# y = 'weight' : y축의 사용될 컬럼명
# s = 50 : 점의 크기 지정
df.plot(kind="scatter",x='mpg',y='weight', c='coral',s=50,figsize=(10,5))

#-----------------------
# matplot 모듈을 이용하여 산점도 출력
plt.figure(figsize=(10,5)) # 새로운 그래프창
# scatter(x축데이터,y축데이터) : 그래프종류
# df["mpg"] : x축데이터
# df["weight"] : y축 데이터
plt.scatter(df["mpg"], df["weight"], c='coral',s=20)

df[["mpg","weight"]].corr() #correlation 상관계수
df[["mpg","cylinders"]].corr()

#-----------------------
# bubble 그래프: 산점도, 점의 크기를 데이터의 값으로 결정
# 3개의 컬럼 지정: x축:weight, y:mpg 점의 크기:cylinders
# cylinders의 데이터의 값의 종류와 갯수 조회
df["cylinders"].unique()
df["cylinders"].value_counts()
# cylinders 값을 최대값의 비율로 계산하여 데이터 생성
cylinders_size = (df["cylinders"]/df["cylinders"].max()*100)
cylinders_size.value_counts()
# alpha = 0.7 : 점의 색을 반투명(70%)
df.plot(kind='scatter',x='weight',y='mpg',c='coral',s=cylinders_size,figsize=(10,5),alpha=0.7)

#-----------------------
# 색상으로 데이터 값을 설정.
# marker="+" : 산점도 점의 모임
# cmap = 'magma' : matplot 모듈에서 숫자에 해당하는 색의 목록
#                 viridis, inferno,magma,cividis...
# c=df["cylinders"] : cylinders의 값에 해당하는 색을 cmap에서 선택
df.plot(kind="scatter", x="weight", y="mpg",marker="+",figsize=(10,5), cmap='magma', c=df["cylinders"],s=50,alpha=0.7)
plt.title("산점도:mpg-weight-cylinders")
# transparent=True : 투명그림으로 저장
plt.savefig("img/scatter_transparent3.png", transparent=True)

# 파이그래프
# origin 컬럼 : 제조국[usa,japan,europe]
    
df_origin = df.origin.value_counts()
df_origin
type(df_origin)
df_origin.plot(kind="pie") #파이그래프
'''
    autopct = "%.1f%%" : 파이그래프에 비율표시
                %.1f   : 소수점이하 1자리로 표시
                %%     : % 문자
                
    startangle=90 : 기본설정 위치에서 90도로 시작위치 변경
'''
df_origin.plot(kind="pie", figsize=(7,5),autopct="%.1f%%", startangle=90,colors=['chocolate','bisque','cadetblue']) #파이그래프
plt.title("자동차 생산국",size=20)
plt.legend(labels=df_origin.index,loc="upper left") #labels다 s가붙어야함

#----------------------------------------------------------
## 박스그래프 두개의 그래프 출력하기
fig = plt.figure(figsize=(15,5)) # 그래프 출력영역, 크기 지정

# 그래프 출력 영역을 분리
ax1 = fig.add_subplot(1,2,1) #1행2열 1번째 그래프
ax2 = fig.add_subplot(1,2,2) #1행2열 2번째 그래프

'''
  labels=['USA','JAPAN','EU'] : x축의 값. 3개의 그룹명
  
  vert=False : 가로형태의 박스그래프.
  
  sym 속성  : "r*"  : 이상치 표현기호 및 색상
            r:red. b:blue .....
            *:별, s:정사각형, +:십자가, .:작은점
            o:큰점(기본값), d:다이아몬드
            
'''

box1 = ax1.boxplot(x=[df[df['origin']=='usa']['mpg'],
                      df[df['origin']=='japan']['mpg'],
                      df[df['origin']=='europe']['mpg']],
                      labels=['USA','JAPAN','EU'],sym="ro") # r 빨간 o 점 
box2 = ax2.boxplot(x=[df[df['origin']=='usa']['mpg'],
                      df[df['origin']=='japan']['mpg'],
                      df[df['origin']=='europe']['mpg']],
                      labels=['USA','JAPAN','EU'],vert=False)
ax1.set_title("제조국자별 연비분포(수직박스플롯)")
ax2.set_title("제조국자별 연비분포(수평박스플롯)")

usadf = df[df['origin']=='usa'][['mpg']]
usadf.max()
usadf.min()
usadf.mean()

# df 데이터를 origin 컬럼으로 그룹화하여 그룹별 합계 출력하기
df.groupby("origin").sum()
# df 데이터를 origin 컬럼으로 그룹화하여 그룹별 건수 출력하기
df.groupby("origin").count()
df.origin.value_counts()
# df 데이터를 origin 컬럼으로 그룹화하여 그룹별 평균 출력하기
df.groupby("origin").mean()
# df 데이터를 origin 컬럼으로 그룹화하여 그룹별 건수 출력하기
df.groupby("origin").median()


# seaborn 모듈 : 시각화 모듈, 데이터셋 mayplot 모듈 확장. 고급시각화
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
titanic.info()
titanic[["age","fare"]].corr()
'''
    선형회귀그래프 : 산점도+회귀선 표시
    회귀선 : 모든점에서 가장 가까운 점들을 선으로 표시.
    fit_reg=False : 회귀선 표시안됨
'''

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='age', y='fare', data=titanic, ax=ax1)
sns.regplot(x='age', y='fare', data=titanic, ax=ax2,fit_reg=False)
plt.show()

# 히스토그램 작성하기
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1) #1행3열1번째
ax2 = fig.add_subplot(1,3,2) #1행3열2번째
ax3 = fig.add_subplot(1,3,3) #1행3열3번째
'''
    sns.distplot : 밀도,빈도수 함께 출력.    
                  kde = False 지정하면 빈도수만 출력
    sns.kdeplot : 밀도를 출력 그래프
    sns.histplot : 빈도수 출력그래프
'''
sns.distplot (titanic['fare'], ax=ax1)
sns.kdeplot(x='fare',data=titanic,ax=ax2)
sns.histplot(x='fare',data=titanic,ax=ax3)
ax1.set_title('titanic fare - distplot') 
ax2.set_title('titanic fare - kdeplot')
ax3.set_title('titanic fare - histplot')
plt.show()

# 히트맵 그래프 : 범주형 데이터의수치를 색상과 값으로 표시
# pivot_table : 2개의 범주형 데이터를 행열로 분리
# aggfunc = 'size' : 데이터갯수 mean,sum....
table = titanic.pivot_table(index=['sex'],columns=['class'], aggfunc='size')
table

a1=titanic[['sex','class']].value_counts()
'''
    table: 표시할 데이터
    annot=True: 데이터값 표시여부
    fmt='d': 10진 정수로 표시
    linewidth=.5: 여백,간격
    cbar=False:  컬러바 표시여부
    cmap='YlGnBu': 컬러맵, Grays
https://matplotlib.org/3.2.1/tutorials/colors/colormaps.html
'''
sns.heatmap(table,annot=True,fmt='d',cmap='YlGnBu',linewidths=.5,cbar=True)
plt.show()

### boxplot 그래프
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(2,2,1) 
ax2 = fig.add_subplot(2,2,2) 
ax3 = fig.add_subplot(2,2,3) 
ax4 = fig.add_subplot(2,2,4) 
'''
    data=titanic : 데이터변수명.
    x='alive', y="age" : titanic 의 컬럼명.
    hue="sex" : 성별로 분리.
    violinplot : 값의범주+분포도를 표시. 가로길이 넓은 부분은 분포가 많은 수치의미
'''
sns.boxplot(x='alive',y='age',data=titanic,ax=ax1)
sns.boxplot(x='alive',y='age', hue="sex",data=titanic,ax=ax2)
sns.violinplot(x='alive',y='age',data=titanic,ax=ax3)
sns.violinplot(x='alive',y='age', hue="sex",data=titanic,ax=ax4)
ax2.legend(loc="upper center")
ax4.legend(loc="upper center")
plt.show()

# pairplot : 각각의 컬럼들의 산점도출력, 대각선위치는 히스토그램으로 표시 값의 분포, 컬럼간의 관계.
titanic_pair = titanic[["age","pclass","fare"]]
titanic_pair
sns.pairplot(titanic_pair)

# FacetGrid : 조건(컬럼의 값)에 다라 그리드 나누기.
#             컬럼의 값(범주형데이터)에 따라서 여러개의 그래프출력.
g = sns.FacetGrid(data=titanic, col='who', row='survived')
g = g.map(plt.hist,'age') #age컬럼의 히스토그램 출력

##########
# 지도 시각화
import folium # pip install folium
# location = [37.55,126.98] : 지도의 중앙 GPS값
# zoom_start=12 : 지도 확대값
seoul_map = folium.Map(location=[37.55,126.98],zoom_start=12)
seoul_map.save("TMap/seoul.html") # html파일생성

seoul_map2 = folium.Map(location=[37.55,126.98],zoom_start=12,title="stamenwatercolor")
seoul_map2.save("TMap/seoul2.html") # html파일생성

'''
tiles : 지도 표시되는 형식 설정.
     openstreetmap : 기본값
     cartodbdark_matter
     cartodbpositron
     cartodbpositrononlylabels
     stamentonerbackground
     stamentonerlabels
     stamenterrain, Stamen Terrain
     stamenwatercolor 
     stamentoner, Stamen Toner
'''

#############################
# index_col=0 : 첫번쨰 컬럼을 index로 설정
df = pd.read_excel("data/서울지역 대학교 위치.xlsx",index_col=0)
df.info()

seoul_map = folium.Map(location=[37.55,126.98],zoom_start=12)
'''
folium.Marker : 지도에 마커 표시객체.
  [lat,lng] : 위도 경도. 마커가 표시될 위치
  popup=name : 마커 클릭시 표시되는 내용
  tooltip=name : 마커ㅓ 내부에 마우스커서가 들어온 경우 표시되는 내용
  
add_to(seoul_map) : seoul_map 지도에 추가  

zip : 목록을 하나씩 연결하여 튜플객체의 리스트로 생성 
'''
df.head()
for name,lat,lng in zip(df.index, df.위도,df.경도):
    # name : 대학교명
    # lat  : 위도
    # lng  : 경도
    folium.Marker([lat,lng],popup=name,tooltip=name).add_to(seoul_map)
seoul_map.save("TMap/seoul13.html")

for z in zip(df.index,df.위도,df.경도):
    print(z)

seoul_map = folium.Map(location=[37.55,126.98],zoom_start=12)

for name,lat,lng in zip(df.index, df.위도,df.경도):
    folium.CircleMarker([lat,lng],
                        popup=name,tooltip=name,
                        radius=10, #반지름 크기
                        color='brown', #원 테두리 색상
                        fill=True, #원내부 채움
                        fill_color='coral', #원 내부색상
                        fill_opacity=0.7, #원 내부 투명도
                        ).add_to(seoul_map)
seoul_map.save("TMap/seoul13.html")

#마커 내부의 아이콘 설정하기
#icon=['home','flag','bookmark','star']
seoul_map = folium.Map(location=[37.55,126.98],zoom_start=12)
for name,lat,lng in zip(df.index,df.위도,df.경도) :
   folium.Marker\
       ([lat,lng],popup=name,tooltip=name,
       icon=folium.Icon(color='red',icon='home')
       ).add_to(seoul_map)
seoul_map.save("TMap/seoul5.html")

# Library.csv 파일을 읽어서 도서관 정보를 지도에 표시하기
df = pd.read_csv("data/Library.csv")
df
# 도서관명
df.시설명.head()
library_map = folium.Map(location=[37.55,126.98],zoom_start=12)

for name,lat,lng in zip(df.index,df.위도,df.경도) :
   folium.Marker\
       ([lat,lng],popup=name,tooltip=name,
       icon=folium.Icon(color='blue',icon='bookmark')
       ).add_to(library_map)
library_map.save("TMap/library.html")

df.시설구분.unique()
'''
    #시설구분별로 색상 설정하기
     시설구분 컬럼의 값에 따라
      구립,국립: green
      사립 : red
      그외 : blue
'''
library_map = folium.Map(location=[37.55,126.98],zoom_start=12)
for name,lat,lng,kbn in zip(df.index,df.위도,df.경도,df.시설구분) :
   if kbn == '구립도서관' or kbn == '국립도서관':
       color = 'green'
   elif kbn == '사립도서관':
       color = 'red'
   else :
       color = 'blue'
    
   folium.Marker\
       ([lat,lng],popup=name,tooltip=name,
       icon=folium.Icon(color=color,icon='bookmark')
       ).add_to(library_map)
library_map.save("TMap/library_color.html")

# MarkerCluster 기능: 지도 확대 정도에 따라 마커 표시방법을 달리해줌. 그룹화 기능

from folium.plugins import MarkerCluster

library_map = folium.Map(location=[37.55,126.98],zoom_start=12)

mc = MarkerCluster() # MarkerCluster() 객체 생성

'''
    DataFrame.iterrows() : 반복문에서 한계레코드의 인덱스와 레코드값을 리턴
                    _    : 변수명, 반복문에서 사용되지 않으므로 상징적인 변수로 설정
                            인덱스값
                    row  : 한개의 레코드
'''

for t in df.iterrows():
    print(t)
    
for _,row in df.iterrows():
    mc.add_child(
        folium.Marker(location = [row['위도'],row['경도']],
                      popup=row['시설구분'],
                      tooltip=row['시설명']
                      )        )
library_map.add_child(mc) # 클러스터를 지도에 추가
library_map.save("TMap/library_dongsan.html")

# 경기도의 인구 데이터와 위치 정보를 이용하여 연구를 지도에 표시하기
import pandas as pd
import folium
import json
df=pd.read_excel("data/경기도인구데이터.xlsx",index_col='구분')
df.info()
df.columns #컬럼명의 자료형이 정수형
#컬럼의 자료형을 문자열형으로 변경하기
df.columns = df.columns.map(str) 
df.columns #컬럼명의 자료형이 문자열형
#2. 위치 정보를 가지고 있는 경기도행정구역경계.json 파일 읽기
# 경기도행정구역경계.json 
# 파일의 내용을 읽어서 json 형식의 객체(dict 객체)로 load
# json 형식 : {"키":"값","키2":"값2",.....}
geo_data=json.load\
    (open("data/경기도행정구역경계.json",encoding="utf-8"))
type(geo_data)
# 3. 지도 표시하기
g_map = folium.Map(location=[37.5502,126.982],zoom_start=9)
year = '2017'  
#데이터와 위치값 매칭.
folium.Choropleth(geo_data=geo_data, #위치 정보를 가진 딕셔너리 객체
     data = df[year],  #표시하고자하는 데이터값
     columns = [df.index, df[year]], #지역명,데이터
     fill_color='YlOrRd',  #채워질 색상 맵. 데이터에 따라 다른 색상 설정
     fill_opacity=0.7,    #내부 투명도
     line_opacity=0.3,    #경계선 투명도
     #데이터와 색상 표시시 사용되는 범위 지정
     threshold_scale=\
         [10000,100000,200000,300000,400000,500000,600000,700000],               
     key_on='feature.properties.name', #데이터와 지역부분 연결 값 
   ).add_to(g_map)
g_map.save('data/gyonggido_' + year + '.html')

df.index
df[year]
df.loc["남양주시"]
df.loc["화성시"]
df.loc["과천시"]


####################

state_geo = "data/us-states.json"
state_unemployment = "data/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)
state_data.info()
m = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(
    state_geo, #문자열. 파일의 위치인식
    data=state_data,  #표시할 데이터.
    columns=["State", "Unemployment"],# 지역명,데이터 컬럼
    key_on="feature.id", #데이터값, 지도의 위치 연결 컬럼
    fill_color="YlGn",  #컬러맵
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",  #범례명
).add_to(m)
m.save('TMap/usa.html')

state_data.head(10)









































































