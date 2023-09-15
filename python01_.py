# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:40:59 2023

@author: KITCOOP
"""

### -  한줄 주석

'''

여러줄 주석

F9 선택영역 or 한줄 실행

'''

"""

여러줄 주석

"""


print('hello')
print("hello")
# 여러개의 데이터 화면에 출력
print(10,20,30,40,50)
# 문자열을 여러번 출력
print("abc"*3)
print('abc'*3)


# 문자열 + 숫자 안됨.
print("학번: "+ 100) #오류발생
print("학번: ", 100)
print("학번: "+ '100')
print("학번: "+ str(100)) #str() : 문자열로 변환
print("'안녕하세요' 라고 말했습니다.")
print('"안녕하세요" 라고 말했습니다.')


# \"
print("\"안녕하세요\" 라고 말했습니다.")
print('\'안녕하세요\' 라고 말했습니다.')

# \n : new line
print("동해물과 백두산이 마르고 닳도록 \n 하느님이 보우하사")

# \ : 라인 연결, 다음라인도 연결된 문장.
print("동해물과 백두산이 마르고 닳도록 \
      하느님이 보우하사")


"""
\ 라인 연결 대신
여러줄 주석 이용하기

"""
print(""" 동해물과 백두산이 마르고 닳도록
      하느님이 보우하사 우리나라 만세
      무궁화 삼천리 화려강산""")
      

    
# 10 20 30 출력
print(10,end="\t")      
print(20,end="\t")
print(30,end="\n") #end 속성값의 기본값 : \n

# 10,20,30 출력      
print(10,end=",")     
print(20,end=",")
print(30)
     
      print("문장의 처음에 공백이 있으면 오류") #오류
      # 공백+컴파일에러 있어도 한줄실행은 잘되네? 다른영역하고 묶으면 에러
      
      
# 문자열 : 문자들의 모임, 문자여러개, 문자의 배열로 인식
print("안녕하세요"[0]) #안
print("안녕하세요"[2]) #하
      
# 문자열의 범위를 지정하여 출력하기
# 문자열[첫번째인덱스 : 마지막인덱스+1 : 증강값]
print("안녕하세요"[0:2]) #안녕, 0번 인덱스부터 1번 인덱스까지(마지막인덱스+1이므로)
print("안녕하세요"[:2])  #안녕, 처음부터 1번 인덱스까지
print("안녕하세요"[:5:2])#안하요, 처음부터 4번인덱스까지 2칸씩증가   
print("안녕하세요"[2:])  #하세요, 2번 인덱스부터 끝까지
print("안녕하세요"[::2]) #안하요, 처음부터 끝가지 2칸씩
print("안녕하세요"[::-1])#요세하녕안 끝에서 처음까지 역순

"""
len=9
함수를 변수로 잡으면 top&down 실행이기 때문에 함수 사용이 안된다.
변수에 숫자 붙이면 실수를 줄일수 있다.
Variable Explorer에서 변수 삭제가능
"""
# len() :문자열의 길이 (자바의 .length)
print(len("안녕하세요"))
len("안녕하세요")

#### 자료형 : 변수선언하지 않고 사용
# 변수의 자료형은 값으로 결정됨.
# 변수명이 같으면 마지막 선언한 변수의 타입으로 저장됨
n = 10
type(n)
n = 10.5
type(n)
n = "안녕"
type(n)

#### 연산자
# 산술 연산자 : +, -, *, /, %, //, **
5+7
5*7
5/7
11%5  #나머지
11//5 #정수형 몫의 값
5**2  #5*5 제곱
5^2   #비트연산자

# 문제 " 3741초가 몇시간 몇분 몇초인지 출력하기(1시간 2분 21초)
print(3741//3600,'시간',((3741%3600)//60),'분',3741%60,'초')

# 키보드에서 초를 입력받아 몇시간 몇분 몇초인지 출력하기
# input 함수: 키보드에서 입력받기.
#             문자열형태로 입력받음.

second = int(input("초를 입력하세요: "))
print(second//3600,'시간',((second%3600)//60),'분',second%60,'초')


# 대입연산자 : =, +=, -= *=,....
a = 10
a += 10
a
a -= 5
a
a *= 2
a

# 문자열에서 사용가능한 대입연산자 : =, +=, *=
s = "abc"
s += "d"
s
s *= 3
s

# 자연수를 입력받아 +100을 한 값을 출력하기

int1 = int(input("자연수를 입력하세요: "))
#print(int1, +100)
int1 += 100
print(int1)


# 형변환 함수
# int() : 정수형으로 변환
# float() : 실수형으로 변환
# str() : 문자열형으로 변환
print("int1+100"+str(int1))
print("int1+100",int1)


# 2, 8, 16 진수를 10진수로 변환
print(int("11",2))
print(int("11",8))
print(int("11",16))

# 10진수를 2, 8, 16진수로 변환
print(10,"의 2진수: ",bin(10))
print(10,"의 8진수: ",oct(10))
print(10,"의 16진수: ",hex(10))

# 형식문자를 이용하여 출력하기 :
# %d (10진수정수)
# %f (실수)
# %s (문자열)
print("%d * %d = %d" %(2.0,3,6))
print("%f * %f = %f" %(2,3,6))
print("%.2f * %.2f = %.2f" %(2.0,3,6))

# %x, %X : 16진수 표현
print("%X" %(255))
print("%x" %(255))
print("안녕 %s!, 나도 %s"%("홍길동",'김삿갓'))

# format 함수를 이용한 출력
# {0:5d} : 첫번째 값을 정수형 5자리로 출력
# {1:5d} : 두번째 값을 정수형 5자리로 출력
# {2:5d} : 세번째 값을 정수형 5자리로 출력
print("{0:5d}{1:5d}{2:5d}".format(100,200,300))
print("{1:5d}{2:5d}{0:5d}".format(100,200,300))

# 직접 변수이름으로 출력
# print(name) 가능해보인다
a = 100
b = 200 
print(f"{a},{b}")
print(a,b)

### 조건문 : if문
# 들여쓰기 해야함
# 들여쓰기로 if else 괄호 맞춘다 생각해야된다.
score = 65

if score >= 90 :
    print("A학점")
    print("합격입니다")
else :
    if score >= 80 :
        print("B학점")
        print("합격입니다")
    else :
        if score >= 70 :
            print("C학점")
            print("합격입니다")
        else : 
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")

# if elif 구문
# 문장 내에서 들여쓰기만 맞추면된다
# if-elif-else 맞추고
# 사이에 print끼리 맞춰야한다

if score >= 90 :
    print("A학점")
    print("합격입니다")
elif score >= 80 :
    print("B학점")
    print("합격입니다")
elif score >= 70 :
    print("C학점")
    print("합격입니다")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")

score = 70
if(score >= 60) :
    print("합격입니다.")
    print("자격증을 받으러 오세요")

# 점수가 60이상이면 PASS 600미만이면 FAIL을 출력하기
score = 65
if score >= 60 :
    print("PASS")
else : 
    print("FAIL")
    
if score >= 60 :
    print("PASS")
elif score < 60 : 
    print("FAIL")

# 간단한 조건식
# TRUE IF 조건식 else FALSE
score = 65
#                    TRUE   IF   조건식  else FALSE
print(score,"점수는",'PASS' if score>=60 else'FAIL')

# 반복문
# 1부터 100까지의 합 구하기
num = 100
hap = 0
# range(1, num+1, 증강값) : 1 ~ num까지의 숫자들
for i in range(1,num+1) :
    hap += i
    print("1부터 %d까지의 합: %d" %(num,hap))

#1 ~ 100까지 짝수의 합 구하기

num = 100
hap = 0
for i in range(0,num+1,2) :
    hap += i
    print("%d부터 %d까지의 합: %d"%(0,num,hap))


hap=0
for i in range(1,num+1) :
    if i % 2 == 0 :
        hap += i
    print("%d부터 %d까지의 합: %d"%(1,num,hap))

# 12345
print(12345)

for i in range(1,6):
    print(i,end="")

# while 조건문 : 조건문의 결과가 참인 동안 반복함
num = 1
while num <= 5:
    print(num,end="")
    num +=1

# break : 반복문 종료
# continue : 반복문의 처음으로 제어 이동

hap = 0
for i in range(1,11) : #1~10
    if i == 5 :
        break;
    hap +=i
print('hap=',hap) #10

hap = 0
for i in range(1,11) : #1~10
    if i == 5 :
        continue;
    hap +=i
print('hap=',hap) #50

# 1 ~ 45 사이의 숫자 6개 출력하기
import random  #모듈
rnum = random.randrange(1,46) # 1~46까지 임의의 수
print(rnum)

for i in range(1,7):
    rnum = random.randrange(1,46)
    print(rnum,end=",")

"""
컴퓨터가 1부터 99사이의 임의의 수를 저장하고,
숫자를 입력받아서 컴퓨터가 저장한 수를 맞추기
컴퓨터는 입력한 숫ㅈ가ㅏ 정답과 비교하여 큰수, 작은수 인지 출력
정답 입력시 입력한 횟수를 출력하기.
1. 난수 생성
2. 정답을 맞추는 동안 계속 입력 받기. => while True:
    정답이 입력되는 break
"""
rnum = random.randrange(1,100) #1~9 까지 임의의 수
cnt = 0

while True :
    a = int(input("숫자를 입력하세요: "))
    cnt += 1
    if a > rnum:
        print(a, "보다 작은수 입니다.")
    elif a < rnum:
        print(a, "보다 큰수 입니다.")    
    else :
        print("정답입니다.")
        print("%d 만에 정답을 맞췄습니다."%(cnt))
        break
    
# 중첩 반복문
i,j=0 #초기화방식
for i in range(2,10)    : #2~9
    print("%5d단 "%i)
    for j in range(2,10) : #2~9
        print("%2d X%2d = %3d"%(i,j,(i*j)))
    print()    

    
'''
*
**
***
****
*****
직각 삼각형 출력하기
'''
i=0
j=0 #초기화방식
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end="")
    print()

# or
i=0
j=0
h=5
for i in range(1,6) :
    print('*'*i)

'''
*****
****
***
**
*
직각 삼각형 뒤집어서
'''

i=0
j=0
h=5
for i in range(1,h+1):
    for j in range(h,j,-1):
        print("*",end="")
    print()
    
# or
i=0
j=0
h=5
for i in range(h,0,-1):
    print("*"*i)


'''
*****
 ****
  ***
   **
    *
    찍기
'''

i=0
j=0
h=5
for i in range(i,h+1):
    print(" "*i,end="")
    for j in range(h,j,-1):
        print("*",end="")
    print()

# or 
i=0
j=0
h=5
for i in range(h,0,-1):
    print(" "*(h-i),end="")
    print("*"*i)

'''
    *
   **
  ***
 ****
*****
찍기
'''
i=0
j=0
h=5
for i in range(i,h+1):
    print(" "*(h-i),end="")
    print("*"*i)
    for j in range(j,h+1):
     print("",end="")

#or

i=0
j=0
h=5
for i in range(i,h+1):
    print(" "*(h-i),end="")
    for j in range(j,i+j,1):
        print("*",end="")
    print()

#or

i=0
j=0
h=5
for i in range(i,h+1,1):
    print(" "*(h-i),end="")
    print("*"*i)

#### 문자열 함수
'''
len(문자열) : 문자열의 길이
문자열.count(문자) : 문자열에서 문자의 갯수 리턴
문자열.fine(문자) : 문자열에서 문자의 위치 리턴
                    없는 경우 -1 리턴
문자열.index(문자) : 문자열에서 문자의 위치 리턴
                    없는 경우 오류 발생
'''
a = "hello"
#a 문자열에서 1문자의 갯수 출력하기
cnt = 0;
# len(a) : a문자열의 길이 5
for i in range(len(a)) : #0 ~4까지값
    if a[i] == 'l' :
        cnt += 1
print(a,"에서 l 문자의 갯수:",cnt)
        

print(a,"에서 l 문자의 갯수:",a.count('l'))
print(a,"에서 a 문자의 갯수:",a.count('a'))

# a 문자열에서 l 문자의 위치 (인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l'))
print(a,"에서 l 문자의 위치:",a.index('l'))

# a 문자열에서 3번 인덱스 부터 l 문자의 위치(인덱스) 출력하기
print(a,"에서 l 문자의 위치:",a.find('l',3))
print(a,"에서 l 문자의 위치:",a.index('l',3))


# a 문자열에서 3번 인덱스 부터 o문자의 위치(인덱스) 출력하기
print(a,"에서 o 문자의 위치:",a.find('o',3))
print(a,"에서 o 문자의 위치:",a.index('o',3))

# a 문자열에서 a문자의 위치(인덱스) 출력하기
print(a,"에서 o 문자의 위치:",a.find('a')) # -1
print(a,"에서 o 문자의 위치:",a.index('a')) # 오류, 에러처리필요

# 문자열의 종류 알려주는 함수
ss = '123'
ss = 'Aa123'
ss = 'Aa'
ss = 'AA'
ss = 'a'
ss = '        '
ss = '   aa   '
ss = '   Aa   '

if ss.isdigit():
    print(ss,": 숫자")
if ss.isalpha():
    print(ss,": 문자")
if ss.isalnum():
    print(ss,": 문자 또는 숫자")
if ss.isupper():
    print(ss,": 대문자")
if ss.islower():
    print(ss,": 소문자")
if ss.isspace():
    print(ss,": 공백")

'''
   print(값) : 화면에 출력하기
   print(값1,값2) : 값을 여러개 출력
   print("{0:d}{1:2d}...".format(값1,값2,...))  형식문자 이용하여 출력
   print("%2d,%3d" % (값1,값2)) : 형식문자 이용하여 값을 여러개 출력
   print(f"{변수1} {변수2}") : 변수에 해당하는 값을 출력
   print(""" 문자열 """) : 여러줄 문자열
   
   문자열 : 문자들의 모임. 인덱스(첨자)를 사용가능
   "문자열"[시작인덱스:종료인덱스+1:증감값]
      시작인덱스 생략시 : 0번부터시작
      종료인덱스 생략시 : 마지막문자까지
      증감값 생략시 : 1씩 증가 
      
   조건문 : if else, if elif else , True if 조건식 else False   

   반복문 : for 변수 in 범위 , while 조건식  
           범위 : range(초기값,종료값+1,증감식)
           break,continue
   조건문,반복문 : 들여쓰기에 주의.         
   
   문자열 함수
     len(문자열) : 문자열의 길이
     문자열.count(문자) : 문자열에서 문자의 갯수 리턴
     문자열.find(문자) : 문자열에서 문자의 위치 리턴  문자가 없는 경우 -1 리턴
     문자열.index(문자) : 문자열에서 문자의 위치 리턴 문자가 없는 경우 오류 발생
     문자열.isdigit() : 숫자?
     문자열.isalpha() : 문자?
     문자열.isalnum() : 숫자또는문자?
     문자열.isupper() : 대문자?
     문자열.islower() : 소문자?
     문자열.isspace() : 공백 ?
'''
'''
튜플(tuple)
튜플의 모양은 아래와 같습니다.
t1 = ()
t2 = (5, )
t3 = (5, 6, 4, 5)
이런식으로 튜플을 만들 수 있습니다.
리스트에서는 대괄호 "[, ]"를 이용해서 리스트를 만들었다면
튜플에서는 소괄호 "(, )"를 이용해서 튜플을 만들 수 있습니다.

비어있는 튜플을 만들려면 t1 = () 처럼 비어있는 소괄호를 넣으면 됩니다.

눈치가 빠르신 분들은 이미 눈치를 채셨겠지만,
값이 1개만 들어있는 튜플을 만들때에는 t2 = (1, ) 처럼 값을 하나 넣고 콤마(,)를 넣어주어야 합니다. 튜플의 규칙이죠.

또 튜플은 set자료형이랑 달리 중복된 값을 넣을 수 있습니다. t3을 보면 5가 두번 있는것을 볼 수 있죠. 튜플은 내부의 값이 중복되도 상관없습니다.

튜플에서 가장 중요한 특징은 "값이 변하지 않는다" 라는 특징인데요.
리스트에서는 값을 변경할수 있지만, 튜플은 내부의 값을 변경하거나 삭제 할 수 없습니다.

특징1) 소괄호 이용해서 생성 "(, )"
특징2) 비어있는 튜플은 ()
특징3) 값이 하나만 있는 튜플은 (5, ) 콤마 하나 꼭 붙여야함
특징4) 값이 중복될 수 있다.
특징5) 튜플의 요소 값은 변경하거나 삭제할 수 없다.
    
    https://blockdmask.tistory.com/447
'''













