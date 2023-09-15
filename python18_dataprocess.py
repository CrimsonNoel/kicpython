# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:36:48 2023

@author: KITCOOP
"""

'''
데이터 속성 설명
order_id : 주문번호
quantity : 아이템의 주문수량
item_name : 주문한 아이템의 이름
choice_description : 주문한 아이템의 상세 선택 옵션
item_price : 주문 아이템의 가격 정보
'''

# 파일 읽기
import pandas as pd
chipo = pd.read_csv("data/chipotle.tsv",sep="\t")
chipo.info()

# chipo 데이터의 행열의 갯수 출력하기
chipo.shape
chipo.columns # 컬럼명
chipo.index # 인덱스명 
# order_id 주문번호이므로, 숫자형 분석의 의미가 없다.
# order_id 컬럼의 자료형을 문자열로 변경하기
chipo["order_id"] = chipo["order_id"].astype(str)
chipo.info()
# 판매상품명과 상품의 갯수 출력하기
chipo["item_name"].unique()
len(chipo["item_name"].unique())
# item_price 컬럼을 실수형 변경

#1
chipo["item_pirce"] = chipo["item_price"].str.replace("$","").astype(float)
chipo.info()
# 주문 금액 합계
hap = chipo["item_price"].sum()
hap

#2
# apply 함수 : 요소들에 적용되는 함수
# apply(함수명||람다식)
chipo["item_price"] = chipo["item_price"].apply(lambda x : float(x[1:]))
chipo["item_price"].sum()

# 주문건수
len(chipo["order_id"].unique())
cnt=len(chipo.groupby("order_id"))
cnt

# 주문당 평균 금액
hap/cnt
chipo.groupby("order_id")["item_price"].sum().mean()

# 50달러이상 주문건수의 주문번호
# 주문 번호가 같은 item_price의 합계를 찾아야한다.
chipo.groupby("order_id")["item_price"].sum()
order_id_tot = chipo.groupby("order_id").sum()
order_id_tot
result = order_id_tot[order_id_tot["item_price"]>=50]
len(result)
type(result)
result
list(result.index)

# 50달러이상 주문한 건수의 주문 정보
chipo_50 = chipo[chipo["order_id"].isin(result.index)]
chipo_50.info()
# or
chipo_51 = chipo.groupby("order_id").filter(lambda x : sum(x['item_price']) >= 50)
chipo_51.info()

# item_name 별 단가 조회하기
price_one = chipo.groupby("item_name")["item_price"].unique()
price_one
price_two =chipo.groupby("item_name")["item_price"]
price_two

len(price_one)
len(price_two)

for key,item in price_two:
    print(key,"=",len(item))
    print(item)

price_min = chipo.groupby("item_name").min()["item_price"]
price_min

# 히스토그램으로 출력하기
import matplotlib.pyplot as plt
import pandas as pd
plt.rc("font",family= "Malgun Gothic")
plt.hist(price_min)
plt.xlabel("상품이름")
plt.ylabel("상품갯수")
plt.title("상품단가 분포")
# or
price_min.plot(kind="line")
plt.xlabel("상품이름")
plt.ylabel("상품갯수")
plt.title("상품단가 분포")

# 주문당 금액이 가장 높은 5건의 주문 총수량을 조회하기
pricetop5 = chipo.groupby("order_id").sum().sort_values(by="item_price",ascending=False)[:5]
pricetop5

# 주문당 금액이 가장 높은 5건의 주문 정보 조회하기
chipotop5 = chipo[chipo["order_id"].isin(pricetop5.index)][["order_id","item_name","quantity","item_price"]]
chipotop5.set_index("order_id",inplace=True)
chipotop5

# Chicken Bowl의 주문 건수 출력하기
chipo_chicken = chipo[chipo["item_name"]=="Chicken Bowl"]
len(chipo_chicken) # 치킨볼이 나간 총 갯수 
len(chipo_chicken.groupby("order_id")) # 치킨볼의 주문 건수
#or
chipo_chicken = chipo_chicken.drop_duplicates(['item_name','order_id'])
len(chipo_chicken)

##########################
# 전세계 음주 데이터 분석하기 : drinks.csv
import pandas as pd
import matplotlib.pyplot as plt
drinks = pd.read_csv("data/drinks.csv")
drinks.info()

'''
  country : 국가명
  beer_servings : 맥주소비량
  spirit_servings : 음료소비량
  wine_servings : 와인소비량   
  total_litres_of_pure_alcohol : 순수 알콜량
  continent : 대륙명
'''
drinks.head()

# 변수  = 컬럼 = 피처?
# 상관계수 :  두 연속적인 데이터의 상관관계 수치
# 피어슨 상관계수 : 기본
beer_wine_corr = drinks[["beer_servings","wine_servings"]].corr()
beer_wine_corr

beer_wine_corr = drinks[["beer_servings","wine_servings"]].corr(method="pearson")
beer_wine_corr

# 켄달 상관계수 :  샘플 사이즈가 작은경우. 동률데이터의 확률이 높은 경우
beer_wine_corr = drinks[["beer_servings","wine_servings"]].corr(method="kendall")
beer_wine_corr

# 스피어만 상관계수 :  정규화가 되지 않는 데이터에 많이 사용
beer_wine_corr = drinks[["beer_servings","wine_servings"]].corr(method="spearman")
beer_wine_corr

drinks.columns
cols = drinks.columns[1:-1]
cols
corr = drinks[cols].corr()
corr
corr.values

# 상관계수 시각화하기
# 히트맵을 이용하여 시가고하 하기
import seaborn as sns
cols_view=["beer","spirit","wine","alcohol"]
sns.set(font_scale=1.5) # 글자크기
hm = sns.heatmap(corr.values, # 데이터
                 cbar = True, # 색상맵
                 annot= True, # 데이터 값 표시
                 square = True,# 히트맵을 사각형으로 출력
                 yticklabels = cols_view, # y축 라벨 표시
                 xticklabels = cols_view  # x축 라벨 표시
                 )



# seaborn 모듈의 산점도를 이용하여 시각화 하기
sns.pairplot(drinks[cols])
plt.show()

# 회귀그래프 작성하기
sns.regplot(x="beer_servings",y="total_litres_of_pure_alcohol",data=drinks)

# 각 변수의 결측값 갯수 조회하기
drinks.isnull().sum()

# 대륙별 국가수 조회하기
drinks["continent"].value_counts()
drinks["continent"].value_counts(dropna=False)
drinks.groupby("continent").count()["country"]

# continent 컬럼의 결측값을 OT로 변경하기
# fillna : 결측값을 다른 값으로 치환함수
drinks["continent"] = drinks["continent"].fillna("OT")
drinks.info()

import numpy as np
plt.rc("font",family="Malgun Gothic")
# 대륙별 국가이ㅡ 갯수를 파이그래프로 출력하기
sns.set(font_scale=1)
# tolist() : 리스트로 형변환
labels = drinks["continent"].value_counts().index.tolist()
labels

# 'AF','EU','AS','OT','OC','SA'
explode = (0,0,0,0.1,0,0)
plt.pie(drinks['continent'].value_counts(), # 데이터값
        labels = labels, # 라벨명, 대륙명
        autopct = '%.0f%%', # 비율표시. #.0f : 소수점이하 없음. %%:%문자
        explode = explode, # 파이의 위치지정, 0.1 : 1/10만큼 밖으로 표시
        shadow = True
        )
plt.title('null data to\'OT\'')

# 대륙별 total_litres_of_pure_alcohol 섭취량 평균
drinks.groupby("continent")["total_litres_of_pure_alcohol"].mean() # 됬나?
drinks.groupby("continent").total_litres_of_pure_alcohol.mean() # 됬다

# 답
cont_mean = drinks.groupby("continent")["total_litres_of_pure_alcohol"].mean()
cont_mean
# 전체평균도 구해놓자
total_mean = drinks["total_litres_of_pure_alcohol"].mean()
total_mean

# 대륙명 : x축의 라벨
xl=list(drinks["continent"].unique())
xl

# 답
continents = cont_mean.index.tolist()
continents
# 추가작업
continents.append("Mean")
continents
x_pos = np.arange(len(continents)) 

# y축 데이터 : 대륙별 평균값
yl = list(drinks.groupby("continent")["total_litres_of_pure_alcohol"].mean())
yl # hm... 내가한거 두개다 순서가..? 그래프로 확인해야함

alcohol = cont_mean.tolist() # list()말고 tolist 좀 써봐야할듯 
alcohol.append(total_mean)
alcohol

# 시각,그래프화
# plt.bar : 막대그래프
# bar_list : 막대그래프 막대 목록
# 그래프를 먼저 그리고 매칭시킨다. 내가 그린건 틀렷다.
bar_list = plt.bar(x_pos,alcohol,align='center',alpha=0.5)
bar_list

# bar_list[len(continents)-1] : bar_list[6] ㅎ막대
# set_color('r') : 색상 설정. r:red
bar_list[len(continents)-1].set_color('r') # 7번째(마지막순번) 막대색 red로 설정

plt.xticks(x_pos,continents) # 각각의 값에 매칭되게 붙는다
plt.ylabel('total_litres_of_pure_alcohol') # y축 전체를 가리키도록 붙는다
plt.title('대륙별 평균 알콜섭취량') # title
plt.show()
bar_list

## bar_list2 = plt.bar(xl,yl,align='center',alpha=0.5) 리스트 맞추는거 tolist() 로 써라 
## 내가그린건 값은 구했는데 매칭이 안된다. 하나로 통일

'''
    대륙별 beer_servings의 평균를 막대그래프로 시각화
    가장 많은 맥주를 소비하는 대륙(EU)의 막대의 색상을 빨강색("r")으로 변경하기 
    전체 맥주 소비량 평균을 구해서 막대그래프에 추가
    평균선을 출력하기. 평균 막대 색상은 노랑색 ("y")
    평균선은 검정색("k--")
'''
#######################내가함
ybeer1 = drinks.groupby("continent")['beer_servings'].sum()
ybeer1.tolist()
ybeer1total = sum(ybeer1.tolist())
ybeer1total

Beercon = ybeer1.index.tolist()
Beercon.append("Mean")
Beercon
x_pos1 = np.arange(len(continents)) 
y_pos1 = ybeer1.tolist().append(ybeer1total)

bar_list10 = plt.bar(x_pos,alcohol,align='center',alpha=0.5)
bar_list10


# bar_list[len(continents)-1] : bar_list[6] ㅎ막대
# set_color('r') : 색상 설정. r:red
bar_list10[ybeer1.tolist().index(max(ybeer1))].set_color('g') # 젤 큰 값의 막대색 red로 설정
    
plt.xticks(x_pos1,continents) # 각각의 값에 매칭되게 붙는다
plt.ylabel('beer_servings') # y축 전체를 가리키도록 붙는다
plt.title('대륙별 평균 알콜 소모량') # title
plt.show()
bar_list10
#########################
# 평균선못그엇고 y축 라벨값 맘에안듬?ㄴㄴ 평균인데 총소비량만구햇네 씁..
###################### 해답

beer_mean = drinks.groupby("continent")["beer_servings"].mean()
beer_mean
total_beer = drinks["beer_servings"].mean()
total_beer

# 대륙명 : x축의 라벨
continents = beer_mean.index.tolist()
continents
continents.append("Mean")
continents
x_pos = np.arange(len(continents)) 

# y축 데이터 : 대륙별 평균값
alcohol = beer_mean.tolist()  
alcohol.append(total_beer)
alcohol

# 시각,그래프화
# plt.bar : 막대그래프
# bar_list : 막대그래프 막대 목록
# 그래프를 먼저 그리고 매칭시킨다. 내가 그린건 틀렷다.
beer_list = plt.bar(x_pos,alcohol,align='center',alpha=0.5)
beer_list
# set_color('r') : 색상 설정. r:red
beer_list[len(continents)-1].set_color('y')
beer_list[beer_mean.index.get_loc(beer_mean.idxmax())].set_color('r')
plt.plot([0,6],[total_beer,total_beer],'k--')
plt.xticks(x_pos,continents) # 각각의 값에 매칭되게 붙는다
plt.ylabel('평균 맥주 소비량') # y축 전체를 가리키도록 붙는다
plt.title('대륙별 맥주 섭취량') # title
plt.show()
beer_list
######################

# 대한민국은 얼마나 술을 독하게 마시는 나라인가?
# total_servings : 전체 주류 소비량 컬럼 추가
drinks["total_servings"] = drinks["beer_servings"]+drinks["spirit_servings"]+drinks["wine_servings"]

# alcohol_rate : 알콜비율(알콜섭취량/전체주류보시량) 추가
drinks["alcohol_rate"] = drinks["total_litres_of_pure_alcohol"]/drinks["total_servings"]

drinks.info()
# alcohol_rate 컬럼에 결측값 존재
# 전체주류소비량이 0인 경우 불능 = > 결측값
# alcohol_rate 컬럼의 값이 결측값인 레코드 조회하기

# alcohol_rate null인 index 구하기
drinks["alcohol_rate"].isnull()
alcoholnull = drinks[drinks["alcohol_rate"].isnull()]
alcoholnull
'''
    기본 사용법
    df.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
    value : 결측값을 대체할 값입니다. dict형태로도 가능합니다.
    method : 결측값을 변경할 방식입니다. bfill로 할경우 결측값을 바로 아래 값과 동일하게 변경합니다.
    ffill로 할 경우 결측값을 바로 위 값과 동일하게 변경합니다.
    axis : {0 : index / 1 : columns} fillna 메서드를 적용할 레이블입니다.
    inplace : 원본을 변경할지 여부입니다. True일 경우 원본을 변경하게 됩니다.
    limit : 결측값을 변경할 횟수입니다. 위에서부터 limit로 지정된 갯수만큼만 변경합니다.
    downcast : 다운캐스트할지 여부입니다. downcast='infer'일 경우 float64를 int64로 변경합니다.
'''
# alcohol_rate 컬럼의 결측값을 0으로 치환하기
alcoholnull.fillna(value=0, axis=0, inplace=True)
alcoholnull
# 우씨 다0으로되네

# 답
drinks["alcohol_rate"]=drinks["alcohol_rate"].fillna(0)
drinks.info()
# alcohol_rate의 값으로 내림차순 정렬하기. alcohol_rate_rank 저장
alcohol_rate_rank = drinks.sort_values(by="alcohol_rate",ascending=False)[["country","alcohol_rate"]]
alcohol_rate_rank.fillna(0,inplace=True)
alcohol_rate_rank

alcohol_rate_rank.head()
alcohol_rate_rank.shape

KR = alcohol_rate_rank.country.tolist().index("South Korea")
alcohol_rate_rank.head(15)
total_servings_rank =  alcohol_rate_rank

# 국가명 목록
country_list = alcohol_rate_rank.country.tolist()

# x축값
x_pos2 = np.arange(len(country_list))

# y축값
rank = alcohol_rate_rank.alcohol_rate.tolist()
rank

# 막대그래프
plt.rc("font",family="Malgun Gothic")
bar_list = plt.bar(x_pos2,rank,align='center',alpha=0.5)

plt.ylabel('alcohol rate') # y축 전체를 가리키도록 붙는다
plt.title('liquor drink ') # title
plt.axis([0,200,0,0.3])
#** axis([x,x,y,y]) xy축 범위:[x축 값의 시작,x축 값의 종료,y축 값의 시작,y축 값의 종료]
# 대한민국 막대색을 red로 변경
bar_list[KR].set_color('r')
KR = alcohol_rate_rank.country.tolist().index("South Korea")
korea_alcohol_rate = alcohol_rate_rank[alcohol_rate_rank['country']=="South Korea"]\
                                                                    ['alcohol_rate'].values[0]
korea_alcohol_rate
KR
## annotaion?
plt.annotate("South Korea : "+str(KR + 1)+'번째',
             xy = (KR, korea_alcohol_rate),
             xytext = (KR+10,korea_alcohol_rate+0.05),
             arrowprops=dict(facecolor = 'red',shrink=0.2) )
plt.show()

import pandas as pd
import numpy as np

# 서울 구별 CCTV 정보 데이터 읽기
CCTV_Seoul = pd.read_csv("data/01. CCTV_in_Seoul.csv")
CCTV_Seoul.info()

# 서울 경찰서별 범죄
crime_Seoul = pd.read_csv("data/02. crime_in_Seoul.csv",thousands=',',encoding='cp949')
crime_Seoul.info()

# 전국 경찰서 위치 데이터 읽기
police_state = pd.read_csv("data/경찰관서 위치.csv",thousands=',',encoding='cp949')
police_state.info()

# 서울지역 경찰서 위치 데이터만 저장
police_state.head()
police_Seoul = police_state[police_state["지방청"]=='서울청'] # 조건문걸어서 찍어내기
police_Seoul

# police_Seoul 데이터의 경찰서 컬럼의 내용을 XX서로 이름변경하여 관서명으로 컬럼생성
# ex ) 서울중부 -- > 중부서
police_Seoul["관서명"] = police_Seoul["경찰서"].str[2:]+"서"
police_Seoul

# police_Seoul 지방청, 경찰서 구분 컬럼 제거하기
del police_Seoul["지방청"],police_Seoul["경찰서"],police_Seoul["구분"]
police_Seoul
police_Seoul.info()

# police_Seoul["관서명"] 중복행 제거
police_Seoul
police_Seoul = police_Seoul.drop_duplicates(subset=["관서명"])
police_Seoul
police_Seoul.info()

# police_Seoul 데이터의 주소 컬럼을 이용하여 구별 컬럼을 생성하기
police_Seoul["구별"] = police_Seoul["주소"].str.split().str[1] # 0: xx시 1: xx구 2: xx로~/xx길~ ...
police_Seoul["구별"].tolist()

# police_Seoul 데이터의 주소 컬럼 제거하기
del police_Seoul["주소"]
police_Seoul.info()
police_Seoul

# 관서명 컬럼을 연결컬럼으로 crime_Seoul 데이터와 police_Seoul 데이터를 병합하기
# data_result 데이터에 저장하기
crime_Seoul
data_result = pd.merge(police_Seoul, crime_Seoul,on="관서명")
data_result

# 구별 범죄의 합계 출력하기
crime_sum = data_result.groupby("구별").sum()
crime_sum

# 범죄 종류(강간,강도,살인,절도,폭력) 별 검거율 컬럼 추가하기
# 검거율 = 검거/발생 * 100
col_list = ['강간','강도','살인','절도','폭력']
for col in col_list:
    crime_sum[col+" 검거율"] = crime_sum[col+" 검거"]/crime_sum[col+" 발생"] * 100
crime_sum.info()
crime_sum

# 검거율 데이터 중 100보다 큰값은 100으로 변경하기
for col in col_list:
    crime_sum.loc[crime_sum[col+" 검거율"] >=100, col+" 검거율"] = 100 # loc 쓰는게 참 난해하네;
    
for col in col_list:
    print(crime_sum.loc[crime_sum[col+" 검거율"] <100, col+" 검거율"])
crime_sum

### 구별 검거율과, CCTV 갯수를 산점도와 회귀선으로 출력하기
# 오차가 큰 10개 구 이름을 그래프로 출력하기
crime_sum.info()
crime_sum.index # 강남구~ 중랑구~
crime_sum = crime_sum.reset_index() # 리셋, 뭐야 간단허네
crime_sum.index # 0 1 2 ~
crime_sum

# 구별 컬럼으로 CCTV_Seoul, crime_sum 데이터를 병합하여 data_result에 저장하기
CCTV_Seoul.info()

# 기관명 > 구별컬럼으로 변경 (merge 기준or교집합이 되는부분) 및 병합
CCTV_Seoul.rename(columns={"기관명":"구별"},inplace=True)
CCTV_Seoul.info()
CCTV_Seoul.drop(["2013년도 이전","2014년","2015년","2016년"],axis=1,inplace=True)
CCTV_Seoul.info()

data_result = pd.merge(crime_sum,CCTV_Seoul,on="구별")
data_result
data_result.info()

# 절도 검거율과 cctv 회귀선과 산점도 출력하기
fp1 = np.polyfit(data_result['소계'],data_result['절도 검거율'],2)
f1 = np.poly1d(fp1) # 회귀선을 위한 함수
fx = np.linspace(500,4000,100)

# data_result 데이터에 오차 컬럼을 추가하기
# 실제 검거율과 기대 검거율의 차이를 절대값 저장
data_result['오차'] = np.abs(data_result["절도 검거율"]-f1(data_result['소계']))
# 오차 내림차순으로 정렬하여 df_sort 데이터 저장
df_sort = data_result.sort_values(by='오차',ascending=False)
df_sort

import matplotlib.pyplot as plt
plt.rc("font",family="Malgun Gothic")
plt.figure(figsize=(14,10))
plt.scatter(df_sort['소계'],df_sort["절도 검거율"],c = df_sort['오차'], s =50)
plt.plot(fx,f1(fx), ls='dashed',lw=3, color="r")

for n in range(len(data_result)):
    plt.text(df_sort.iloc[n,]["소계"]*1.001,  # x축값
             df_sort.iloc[n,]["절도 검거율"]*0.999, # y축값
             df_sort.iloc[n,]["구별"], fontsize=10    )
plt.xlabel('CCTV 갯수')
plt.ylabel('절도범죄 검거율')
plt.title('CCTV와 절도 검거율 분석')
plt.colorbar()
plt.grid()
plt.show()






































































