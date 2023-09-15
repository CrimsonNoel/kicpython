# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:23:59 2023

@author: KITCOOP
"""

import sqlite3
dbpath = "test.sqlite"  # database 파일 이름...
conn = sqlite3.Connection(dbpath) # 데이터 베이스 접속.
cur = conn.cursor() # sql 구문을 실행할 수 있는 객체

# executescript : 여러개의 sql 문장을 실행.
#                 각각의 문장들은 ;으로 구분됨      
'''
  drop table if exists items; => items 테이블이 존재하면 테이블 삭제.
  => items 테이블 생성
  item_id integer primary key : 
               item_id 컬럼이 숫자형 기본키. 값이 자동증가됨
  name text unique : 문자형 데이터. 중복불가

  create table items (item_id integer primary key,
        name text unique, price integer);
=> insert 구문 실행. 
=> item_id 컬럼을 제외 : 값이 자동 증가됨  
  insert into items (name,price) values ('Apple',800);                  
  insert into items (name,price) values ('Orange',500);
  insert into items (name,price) values ('Banana',300);  

'''

cur.executescript("""
     drop table if exists items;
     create table items(
         item_id integer primary key,
         name text unique,
         price integer);
     insert into items (name,price) values ('Apple',800);                  
     insert into items (name,price) values ('Orange',500);
     insert into items (name,price) values ('Banana',300);  
""")
conn.commit()

# execute : sql 명령문 실행
cur.execute("select * from items")
# fetchall() : select 결과 전부를 리스트 전달
item_list = cur.fetchall()
print(item_list) # [(컬럼값1,컬럼값2,...),(...) 
                 # => [(1, 'Apple', 800), (2, 'Orange', 500), (3, 'Banana', 300)]
# 반복문으로 조회
for id,name,price in item_list :
    print(id,name,price)


'''
    문제: mydb sqlite 데이터 베이스 생성
         mydb member 테이블 생성하기
         id char(4) primary key,name char(15), email char(20) 인
         컬럼을 가진다
'''

cur.executescript("""
            drop table if exists member;
            create table member(
                id char(4) primary key,
                name char(15),
                email char(20)
                );
          insert into member (id,name,email) values ('kimsk','김삿갓','kim@aaa.bbb')  
                  """)
conn.commit()

cur.execute("select * from member")
member_list = cur.fetchall()
print(member_list)
for id,name,email in member_list :
    print(id,name,email)

# 화면에서 id, 이름, 이메일을 입력받아 db에 등록하기
while True:
    d1 = input("사용자Id: ") #사용자 id
    if d1 == '':
        break
    d2 = input("사용자name: ") #사용자 name
    d3 = input("사용자email: ") #사용자 email
    sql = "insert into member (id,name,email) values ('"+d1+"','"+d2+"','"+d3+"')"
    
    print(sql)
    cur.execute(sql)
    conn.commit

# db닫히면 다시열어줘야함
conn = sqlite3.connect("mydb")
cur = conn.cursor()


## mapping에 의한 insert sql
param = []
sql = "insert into member (id,name,email) values (?,?,?)"
param.append("kic")         #첫번째 등록. 첫 ?값
param.append("dddd")        #두번째 등록. 
param.append("ccc@mmm.com") #세전뺴
cur.execute(sql,param)
conn.commit()

cur.execute("select * from member")
# fetchall() : select 결과 전부를 리스트 전달
item_list = cur.fetchall()
print(member_list) # [(컬럼값1,컬럼값2,...),(...) 

## mapping 을 이용한 update
param = []
param.append("hongkd@aaa.bbb")
param.append("kic")
sql = "update member set email = ? where id =?",param
conn.commit()
conn.close()

# 이름이 테스트10 회원 정보 삭제하기
param = []
param.append("dddd")
cur.execute("delete from member where name=?",param)
conn.commit()
conn.close()


'''
=========================================================================
'''

# 데이터 없어서 anaconda prompt에서
# pip install cx_Oracle 입력후 데이터 받아야함
# 오라클 데이터 베이스에 접속하기
# 오라클 모듈을 설정해야함

import cx_Oracle
# connect("사용자 아이디","비밀번호","서버 IP/SID")
conn = cx_Oracle.connect('kic','1111','localhost/xe')
cur = conn.cursor() # sql 명령객체

cur.execute("select * from board")
st_list = cur.fetchall()
for st in st_list:
    print(st)

'''
 문제 : 학생테이블에
     학번(studno) : 5555, 이름(name):파이썬, 학년(grade):5,
     id : test1, jumin:9001011234567
     데이터 추가하기
'''


cur.execute("select * from student1")
st_list = cur.fetchall()
for st in st_list:
    print(st)

# dictionary 
sql = "insert into student1(studno,name,grade,id,jumin) values(:studno,:name,:grade,:id,:jumin)"
cur.execute(sql, studno=5555,name='파이썬',grade=5,id='test1',jumin='9001011234567')
conn.commit()

param={"studno":5557,"name":"파이썬","grade":5,"id":"test3","jumin":"9001011234567"}
cur.execute(sql,param)
conn.commit()

# print 방식
cur.execute("select * from student1 where grade=%d" %(5))
st_list = cur.fetchall()
for st in st_list:
    print(st)












































