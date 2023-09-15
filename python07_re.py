# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:06:59 2023

@author: KITCOOP
"""
data = \
'''
   park 800915-1234567
   kim 890125-2345678
   choi 850125-a123456
'''
#1. 정규식 없이 주민번호 뒷자리 값추기
print(data)
result = [] #['park 800915-*******','kim 890125-*******','choi 850125-a123456']

#line : choi 850125-a123456
for line in data.split("\n"): #[choi,850125-a123456]
    word_result= []
    #word : 850125-a123456
    for word in line.split(" "): #word[0] : park, word[1] : 800915-1234567
        
        if len(word) == 14 and word[:6].isdigit() and\
                               word[7:].isdigit() : #word[1]
                word = word[:6]+"-"+"*******"
        word_result.append(word) #word[0],word[1] 추가
    result.append(" ".join(word_result))
        
print("\n".join(result))

#2. 정규식을 이용하여 주민번호 뒷자리 감추기

import re #정규식을 위한 모듈
'''
re.compile(정규식패턴) : 패턴 객체 생성 

pat : 패턴객체. 정규식 형태로 정의된 형태를 지정하는 객체 

(\\d{6,7})[-]\\d{7} : 형태 지정. 패턴.
     => 앞의 6또는 7 자리 숫자, -, 7자리 숫자 인 형태 패턴
() : 그룹
\d{6,7} : \d(숫자데이터) {6,7}(6,7개의 자리수) 숫자 6또는7개
[-] : - 문자
\d{7} : 숫자 7개
'''
pat1 = re.compile("(\\d{6,7})[-][a-zA-Z0-9]{7}")
pat = re.compile("(\\d{6,7})[-]\\d{7}")
print(pat1.sub("\g<1>-*******",data))

# 정규식을 이용하여 데이터 찾기
str1 = "The quick brown fox jomps over the laze dog Te Thhhhhhhe,THE"
str_list = str1.split()
print(str_list)
# Th*e : 0개이상.
#       T로 시작하고 e로 종료하는 문자열. 사이값이 h가 0개 이상인 문자열
#       The, Te, Thhhhhe
pattern = re.compile("Th*e") #패턴 객체 설정
count = 0
for word in str_list:
    # pattern.search(word) : word에서 pattern에 맞는 문자열 존재?
    #                       존재 : 객체 리턴
    #                       없으면 : None 리턴
    if pattern.search(word):
        print(word)
        count+=1
print("결과 1=> %s:%d"%("갯수",count)) #3

# re.I : 대소문자 구분없이 검색

pattern = re.compile("Th*e",re.I) #패턴 객체 설정
count = 0
for word in str_list:
    if pattern.search(word):
        print(word)
        count+=1
print("결과 2=> %s:%d"%("갯수",count))

print("결과 3=>",re.findall(pattern,str1))
print("결과 4=>",pattern.sub('aaa',str1))

# 문제 :  str2 문자열에서 온도의 평균 출력하기
str2 = "서울:25도,부산:23도,대구:27도,광주:26도,대전:25도,세종:27도"
pattern = re.compile("\\d{2}")
tlist = re.findall(pattern, str2)
tlist = list(map(int,tlist))
print(tlist)
print(sum(tlist)/len(tlist))

'''
  정규식에서 사용되는 기호
  1. () : 그룹
  2. \g<n> : n번째 그룹
  3. [] : 문자
     [a] : a 문자
     [a-z] : 소문자
     [A-Za-z] : 영문자(대소문자)
     [0-9A-Za-z] : 영문자+숫자
  4. {n} :n개 갯수
     ca{2}t : a 문자가 2개
      caat : true
      ct   : false
      cat  : false
     {n,m} :n개이상 m개이하 갯수
     ca{2,5}t : a 문자가 2개이상 5개 이하
      ct   : false
      cat  : false
      caat : true
      caaaaaaaaat : false
  5. \d : 숫자. [0-9]동일
  6. ?  : 0개또는 1개.
    ca?t : a문자는 없거나 1개    
    ct : true
    cat : true
    caat : false
  7. * : 0개이상  
    ca*t : a문자는 0개 이상
    ct : true
    cat : true
    caat : true
  8. + : 1개이상  
    ca+t : a문자는 1개 이상
    ct : false
    cat : true
    caat : true
  9. \s : 공백
     \s* : 공백문자 0개이상  
     \s+ : 공백문자 1개이상  
'''





















