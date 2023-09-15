# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:01:22 2023

@author: KITCOOP
"""

'''
모듈
함수(변수+명령어) < 클래스(변수+명령어+함수) < 모듈(파일) < 패키지(폴더)
표준모듈, 외장모듈, 사용자정의모듈
모듈이란?
함수, 변수, 클래스의 집합. 함수, 변수, 클래스들을 모아놓은 파일 여러 변수, 함수, 클래스(다수의 변수+함수)를 저장해둔 파이썬 소스코드 파일.
*.py 확장자를 이용하여 직접 만들 수 있다.
다른 사람들에 의해서 만들어진 파이썬 라이브러리들을 모듈이라고 한다.
모듈을 불러오는 방법 : import 명령을 통해서 모듈을 불러와 사용할 수 있다.
모듈의 종류
표준 모듈 : 파이썬이 기본적으로 제공해주는 모듈
외부 모듈 : 파이썬이 기본적으로 제공해주지 않는 모듈
사용자정의 모듈 : 직접 만들어 사용하는 모듈
** 플러그인 같은 개념
'''

# 모듈을 사용하기 위해서는 다음과 같은 문법을 이용하여 모듈을 임포트 해야한다.

'''
1) import <모듈이름>
2) import <모듈이름> as <모듈변수(별칭; alias)>
3) from 모듈이름 import <모듈함수>,<모듈함수>
    from 모듈이름 import 함수명1, 함수명2, ....
    from ~ import ~ 문을 이용하면 모듈이름을 붙이지 않고 바로 해당 모듈 함수 사용 가능
    (콤마)를 사용하지 않고 여러 함수를 불러올 수 있는 방법
    from 모듈이름 import * => 잘 안 씀!
'''

# math 모듈(표준모듈)
# 수학 함수를 사용할 수 있는 math 모듈
# 모듈명.속성, 모듈명.함수() 로 사용

# import tensorflow as tf - error 세팅안해서 에러
import math as m


# help(m) # 개요/가이드/함수 소개
# print(dir(m)) # dir(모듈명) : 제공 함수나 속성을 리스트로 제공

m.__doc__

print(m.sin(90))
print(m.factorial(3))
print(m.tan(90))
print(m.cos(90))
print(m.sin(90)*m.cos(90)*m.tan(90))
print(m.pi)

# sqrt() 함수 사용
m.sqrt(1) # shift + tab 입력하면 어떻게 쓰는지 알려줌
#print(random.sqrt())
print(m.sqrt(9)) # 루트(*)
print(int(m.sqrt(100)))

# random 모듈
# 난수 발생

import random as r

print([r.randint(0,1) for i in range(10)])  # 0, 1 을 무작위로 10개생성
print([r.randrange(11) for i in range(10)]) # 0~10 사이 무작위 10개생성
print([r.random() for i in range(3)])
print([round(r.random(),2) for i in range(3)]) # 0~1 사이 실수
# (random.uniform(x,y), n) => x~y 사이의 수를 n자리까지
print([(r.uniform(-5,5), 1)for i in range(10)])

lottoNum = []
for i in range(0,6):
    lottoNum.append(r.randint(1, 46))
#       if == 6:
#           lottoLost[6]= f'+{r.randint(1,46)}'
print(lottoNum)






































