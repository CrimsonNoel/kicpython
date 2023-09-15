# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:19:43 2023

@author: KITCOOP
"""
############################
# 함수와 람다
# 함수: def 예약어 사용
############################

def func1():
    print("func1() 함수 호출됨")
    return 10 #함수 종류 후 값을 리턴

def func2(num):
    print("func2() 함수 호출됨",num)
     #리턴 없는 함수
     
a=func1()
print(a)
b=func2(100)
print(b)
func2('abc')

# 전역변수 : 모든 함수에서 접근이 가능한 변수 
# 지역변수 : 함수 내부에서만 접근이 가능한 변수

def func3():
    c=300 #지역변수
    print("func3() 함수 호출: ",a,b,c)
def func4():
    a=110 #지역변수
    b=220 #지역변수
    print("func4() 함수 호출: ",a,b)
    
# 함수 내부에서 전역 변수값 수정하기
def func5() :
    global a,b  #a,b 변수는 전역변수를 사용함
    a=110
    b=220
    print("func5() 함수 호출: ",a,b)

a=1000
b=2000

func3()
#print("main: ",a,b,c) #c 변수는 func3() 함수에서만 사용가능
print("main: ",a,b)
func4()
print("main: ",a,b)
func5()
print("main: ",a,b)


# 매개변수
def add1(v1,v2):
    return v1+v2

def sub1(v1,v2):
    return v1-v2

hap = add1(10,20)
sub = sub1(10,20)
print(hap)
print(sub)

hap = add1(10.5,20.1)
sub = sub1(10.5,20.1)
print(hap)
print(sub)

hap = add1("python","3.9")
print(hap)
#sub = sub1("python","3.9")
#hap = add1("python","3.9","aaaa")

# 가변 매개 변수 : 매개변수의 갯수를 정하지 않을 경우
def multiparam(*p):
    result = 0
    for i in p:
        result += i
    return result    
print(multiparam())    
print(multiparam(10))    
print(multiparam(10,20))    
print(multiparam(10,20,30))    
print(multiparam(1.5,2.5,3))    
print(multiparam("1.5",2.5,3))    # result = error

# 매개변수에 기본값 설정
def hap1(num1=0,num2=1) : #매개변수가 없는 경우 0,1 기본값 설ㅈ어됨
    return num1+num2

print(hap1())       #num1=0, num2=1 기본값 설정
print(hap1(10))     #num1=10, num2=1 기본값 설정
print(hap1(10,20))  #num1=10, num2=20 기본값 설정
print(hap1(0,20))   #num1=0, num2=20 기본값 설정
#print(hap1(10,20,30)) #error

# 리턴값 두개인 경우 : 리스트로 리턴
def multiReturn(v1,v2):
    list1=[]
    list1.append(v1+v2)
    list1.append(v1-v2)
    return list1

list1 = multiReturn(200, 100)
print(list1)

# 계산기호인자 값에 따라서 뒤의 가변인자값을 계산하는 함수 정의
def calChoice(choice, *args):
    if choice == '*':
        res = 1
        for i in range(0, len(args)):
            res *= args[i]
        return print(f'계산결과 = 곱 : {res}')
    elif choice == '+':
        res = 0
        for i in range(0, len(args)):
            res += args[i]
        return print(f'계산결과 = 합 : {res}')
    else:
        return print('계산오류')
    
calChoice('*', 20,30)
calChoice('+', 20,30,50)
calChoice('!', 20,30,50)

# 딕셔너리 가변인자 **kwargs
def dictDefine(**kwargs):
    print('='*30)
    print(kwargs)
    # kwargs.sort() 에러 함수없나?;
    for k in kwargs:
        print(k, ':',kwargs[k])
    print('\n 딕셔너리의 총길이는?',len(kwargs))

# 함수 호출
dictDefine()
dictDefine(a='apple',b='banana',c='carrot')
dictDefine(n='nano',u='umbrella',m='mountain',s='sweet',d='dress')

# 람다식을 이용한 함수
hap2 = lambda num1,num2:num1+num2
print(hap2(10)) #error 기본값이 없어서 에러
print(hap2(10,20))
print(hap2(10.5,20.5))

# 기본값 매개변수
hap3 = lambda num1=0, num2=1:num1+num2
print(hap3(10)) #11
print(hap3(10,20)) #30
print(hap3(10.5,20.5))

# 문제: 리스트의 평균을 구해주는 함수 getMean 구현하기
def getMean(li):
    if len(li)>0:
        return sum(li)/len(li)
    else:
        return 0
list1 = [1,2,3,4,5,6]
list2 = []
print(getMean(list1))
print(getMean([]))

# 람다식 lambda p : 내용
# if가 들어가면 lambda p : 내용 if True면내용으로 else 리턴값
getMean2 = lambda li:sum(li)/len(li) if len(li)>0 else 0
print(getMean2(list1))
print(getMean2(list2))


# 문제: mylist1 보다 각각의 요소가 10이 더 많은 요소를 가진 mylist2 생성
mylist1 = [1,2,3,4,5]
mylist2 = [] #결과값 [11,12,13,14,15]

#1 for문
for n in range(1,6):
    mylist2.append(n+10)
print(mylist2)

#2 comprehension
mylist2 = [n+10 for n in mylist1 ]
print(mylist2)

#3 map
#map(함수,리스트) : 리스트의 각 요소에 함수(add10)적용
def add10(n):
    return n+10
mylist2 = list(map(add10,mylist1))
print(mylist2)

#4 map+lambda
mylist2 = list(map(lambda n:n+10,mylist1))
print(mylist2)

######## filter()
# 일반함수 + filter()

# 숫자 리스트에서 짝수만 추출하여 새로운 리스트로 변환
def evenNumber(dataList):
    resList = []
    for i in dataList:
        if i%2 == 0:
            resList.append(i)
    return resList
print(evenNumber([13,50,47,67,12,34,55,134,85,-41,-85,-36]))
list3 = [13,50,47,67,12,34,55,134,85,-41,-85,-36]

#filter() + 일반 함수 스타일
# 1) 값이 짝수면 True, 아니면 False인 일반 함수 정의

def evenNum(n):
    return n%2 == 0

# 1-1) 람다로 변경
evenNum2 = lambda n:n%2==0

# 2) 호출
print(evenNum(5))
print(evenNum(-3))
print(evenNum(8))

# filter() + 일반 함수 스타일
print(list(filter(evenNum,list3)))

# filter() + lambda식
print(list(filter(lambda n:n%2==0,list3)))


# 문제: filter() 함수를 이용하여 다음 문자열에서 숫자만 리스트로 만들어 출력하여라

message = 'ab4690cfvg342가1나1다0'
    
print(list(filter(lambda n:n.isdigit(),message))) #isdigit() 숫자만~


## map,filter
# map() : 람다식}함수명, 리스트
# 입력 리스트 길이와 출력 리스트 길이가 같다
# 리스트의 제곱을 구해서 새로운 리스트로 만들기
numList2=[1,2,3,4]

# 제곱을 구하는 함수 정의 : 일반 함수 스타일
def power_fn1(myList):
        res = []
        for i in myList:
                res.append(i**2 )
        return res
print(power_fn1(numList2))

# map() 사용
def power_f2(value):
    return value**2

print(power_f2(3))
print(map(power_f2,numList2))
print(list(map(power_f2,numList2)))

# lambda 사용

print(list(map(lambda n:n**2,numList2)))
power_f3 = lambda n:n**2
print(power_f3(5))

# 두 리스트에서인덱스가 같은 값을 서로 곱한 후 리스트로 만들기
list1 = [2,3,7]
list2 = [4,5,9]

# 연산x join의 의미, 여러 리스트를 하나의 리스로 병합
print(list1 + list2)
print()

# 일반 함수
def multyply_n(list1, list2):  #(collection , collection)
    resList=[]
    for i in range(0,len(list1)):
        resList.append(list1[i]*list2[i])
    return resList
print(f'{list1}\n{list2}, \n 일반함수 => {multyply_n(list1,list2)}')

# map 함수 이용
def map_multi(x, y):
    return x*y
# map 함수이용 게산
print(f'{list1}\n{list2}, \n map 함수 =>{list(map(map_multi,list1,list2))}')


# lambda
def map_multi(x, y):
    return x*y

print('map(),lambda 함수',list(map(lambda x,y:x*y,list1,list2)))

###
'''
4개의 리스트 각 아이템 요소가 '-'로 연결되어 출력되도록 하여라
최종 결과는 리스트로 저장되어야 하며 map() 함수를 활용한다
'''

num_list = [100, 200, 300, 400]
name_list = ['길동', '동미', '미영', '영철']
gender_list = ['남','여','여','남']
address_list = ['서울','대전','부산','대구']

# ['100-길동-남-서울', '200-동미-여-대전','300-미영-여-부산','400-영철-남-대구']

# map 적용 함수
def map_pair(a,b,c,d):
    return f'{a}-{b}-{c}-{d}'
print(list(map(map_pair,num_list,name_list,gender_list,address_list)))

# map, lambda
print(list(map(lambda a,b,c,d:f'{a}-{b}-{c}-{d}',num_list,name_list,gender_list,address_list)))



















































































