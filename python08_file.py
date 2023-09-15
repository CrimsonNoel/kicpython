# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:17:40 2023

@author: KITCOOP
"""

### 파일 읽기
'''
    open("파일명",파일모드,[인코딩])
    인코딩: 파일의 저장방식. 기본값:cp949형식
    파일코드
        r : 읽기
        w : 쓰기, 기존의 파일의 내용을 무시, 새로운 내용으로 추가
        a : 쓰기, 기존의 파일의 내용에 추가
        t : text 모드, 기본값
        b : 이진모드, binary모드, 이미지, 동영상...
        
    파일 : open(파일명,모드,[encoding])
         os.getcwd() : 작업폴더 조회
         os.chdir()  : 작업폴더 변경
         os.path.isfile(file) : 파일?
         os.path.isdir(file)  : 폴더?
         os.listdir()  : 폴더의 하위 파일 목록 조회 
'''

infp = open("c:\\Users\\KITCOOP\\kicpython\\python07_re.py","rt",encoding="UTF-8")
while True:
    instr = infp.readline() # 한줄씩 읽기
    if instr == None or instr == '' :  #python07_re.py을 console창에 읽어온다
        break
    print(instr,end="")
infp.close() 

# 파일 쓰기 : 콘솔에 내용을 입력 받아 파일로 저장 하기
# 현재 폴더에 data/data.txt에 저장한다

outfp = open("data/data.txt","w",encoding="UTF-8")
while True:
    outstr = input("내용 입력 : ")
    if outstr == '':
        break
    outfp.writelines(outstr+"\n")
outfp.close()

'''
    readline() : 한줄씩 읽기
    read()     : 버퍼의 크기만큼 한번 읽기
    readlines(): 한줄씩 한번에 읽어서 줄별로 리스트로 리턴
'''

#data.txt 파일을 읽어서 화면에 출력하기
infp = open("data/data.txt","r",encoding="UTF-8")
while True:
    instr = infp.readline() # 한줄씩 읽기
    if instr == None or instr == '' :
        break
    print(instr,end="")
infp.close() 

infp = open("data/data.txt","r",encoding="UTF-8")
print(infp.read())
infp.close()

infp = open("data/data.txt","r",encoding="UTF-8")
print(infp.readlines())
infp.close()

# 이미지 파일 읽어 복사하기
# apple.gif 파일을 읽어서 apple2.gif로 복사하기
infp = open("data/apple.gif","rb")
outfp = open("data/apple2.gif","wb")

while True:
    indate = infp.read()
    if not indate : # 파일의 끝 EDF(End of file)
        break
    outfp.write(indate)
infp.close()
outfp.close()

# 문제: score.txt 파일을 읽어서 점수의 총합과 평균 구하기
#
# score.txt 내용
# 홍길동,100
# 김삿갓,50
# 이몽룡,90
# 임꺽정,80

import re

infp = open("data/score.txt","r",encoding="UTF-8")
data = infp.read()
print(data)
# \\d+  : 숫자 1개이상
# \\d{1,3} : 숫자 1개이상 3개이하
pattern = re.compile("\\d+") # 숫자 1개이상
# pattern = re.compile("\\d{1,3}") #숫자1개이상 3개이하
# data 에서 숫자를 찾아서 라스트리턴
scorelist = re.findall(pattern,data)
print(scorelist)
scorelist = list(map(int,scorelist))
print(scorelist)
print("총합: ",sum(scorelist), "평균",sum(scorelist)/len(scorelist))

###
import os
# 현재 작업 폴더 위치 조회
print(os.getcwd())
# 폴더 위치 변경
os.chdir("c:/Users/KITCOOP")
print(os.getcwd())

os.chdir("c:/Users/KITCOOP/kicpython")
print(os.getcwd())

# 파일의 정보 조회
import os.path
file = os.getcwd()
file

if os.path.isfile(file) :
    print(file,"은 파일입니다.")
elif os.path.isdir(file) :
    print(file,"은 폴더입니다.")

if os.path.exists(file) :
    print(file,"은 존재합니다.")
else :
    print(file,"은 없습니다.")    

# 문제 : 작업파일의 하위파일목록
# 파일인 경우 : 파일의 크기 os.path.getsize(파일명)
# 폴더인 경우 : 하위파일의 갯수
# 작업 폴더의 하위파일갯수

print(os.listdir())
file = "data/data.txt"
os.path.exists(file) # true 존재한다

len(os.listdir()) # 갯수
os.listdir()      # 폴더 아래에 있는 파일을 (폴더 포함) 보여준다
# 현재 작업 폴더
cwd = os.getcwd()
cwd
for f in os.listdir():
    if os.path.isfile(f):
        print(f,":파일,크기: ", os.path.getsize(f))
    elif os.path.isdir(f):
        os.chdir(f)
        print(f,":폴더,하위파일의 갯수: ",len(os.listdir()))
        os.chdir(cwd)

# 폴더 생성
os.mkdir("temp")  #temp 폴더 생성
# 폴더 제거
os.rmdir("temp")  #temp 폴더 제거

###### 엑셀 파일 읽기
'''
    xlsx : openpyxl 모듈사용
    xls  : xlrd 모듈로 읽기
           xlwd 모듈로 쓰기
'''
import openpyxl

filename = "data/sales_2015.xlsx"
# 엑셀파일 전체
book = openpyxl.load_workbook(filename)
# 첫번째 sheet
sheet = book.worksheets[0]

data=[]
for row in sheet.rows:
    line = []
    print(row)
    # enumerate(row) : 목록에서
    #               l : 인덱스
    #               d : 데이터,셀의값
    for l,d in enumerate(row):
        line.append(d.value) # 셀의 내용을 line 추가
  # print(line) #한 줄의 셀의 리스트
    data.append(line)  
print(data)     

# xls 형식의 엑셀파일 읽기
# import 안되면(모듈이 없을시)
# anaconda prompt 들어가서 
# pip install (모듈명) xlrd 입력시 설치
import xlrd
infile = "data/ssec1804.xls"
# workbook : 엑셀파일 전체 데이터
workbook = xlrd.open_workbook(infile)
# workbook.nsheets : sheet의 갯수
print("sheet 의 갯수", workbook.nsheets)

for worksheet in workbook.sheets():
    #worksheet : 한개의 sheet 데이터
    print("worksheet 이름: ",worksheet.name)
    print("행의 수: ",worksheet.nrows)
    print("컬럼의 수: ",worksheet.ncols)
    # worksheet.nrows : 행의 수
    # worksheet.ncols : 컬럼의 수
    for row_index in range(worksheet.nrows) :
        for column_index in range(worksheet.ncols) :
            print(worksheet.cell_value(row_index,column_index),",",end="")
        print()







































