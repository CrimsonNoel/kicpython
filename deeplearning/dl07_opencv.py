# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:06:54 2023

@author: KITCOOP
"""
'''
     opencv 예제 : 이미지 처리를 위한 툴
         pip install opencv-python : anaconda prompt
        
    빅데이터 조건(3v):
            1. Volumn : 대용량
            2. Velocity : 속도, 처리속도가 빠르다.
            3. Variety : 데이터의 다양성
                    - 정형데이터   : dbms, csv, excel => pandas,numpy...
                    - 반정형데이터 : xml, html, json => BeatifulSoup, selenium, json
                    - 비정형데이터 : 이미지, 동영상 => opencv
'''

import cv2
title1, title2, title3 = "gray2gray", "gray2color","gray2colors"
# cv2.imread : 이미지 파일을 읽기, 행렬 데이터로 변환
# cv2.IMREAD_GRAYSCALE : 흑백이미지로 처리
# cv2.IMREAD_COLOR : 컬러이미지로 처리
# cv2.IMREAD_UNCHANGED : 원래이미지로 처리

gray2gray = cv2.imread("images/read_gray.jpg",cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread("images/read_gray.jpg",cv2.IMREAD_COLOR )
gray2colors = cv2.imread("images/read_gray.jpg",cv2.IMREAD_UNCHANGED)

color2gray = cv2.imread("images/read_color.jpg",cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("images/read_color.jpg",cv2.IMREAD_COLOR )
color2colors = cv2.imread("images/read_color.jpg",cv2.IMREAD_UNCHANGED)

type(gray2gray)
gray2gray.shape # (300, 400)
gray2gray.ndim  # 2
gray2gray[0]    
gray2color.shape # (300, 400, 3)
gray2colors.shape # (300, 400)
gray2colors.ndim # 2

# imshow : 행렬데이터를 이미지로 출력
cv2.imshow(title1,gray2gray)
cv2.imshow(title2,gray2color)
cv2.imshow(title3,gray2colors)
cv2.waitKey(0)

cv2.destroyAllWindows()

# 이미지 저장하기
image = cv2.imread("images/read_color.jpg",cv2.IMREAD_COLOR)
# cv2.IMWRITE_JPEG_QUALITY,10 : 화질설정
#                 0 ~ 100(95) : 훟자가 높으면 화질이 좋음
param_jpg = (cv2.IMWRITE_JPEG_QUALITY,10) # 튜플, 리스트가능
# cv2.IMWRITE_PNG_COMPRESSION,9 : png 파일의 압축레벨 설정
#                       0 ~ 9(3) : 압축레벨이 높으면 이미지 용량이 작다
params_png = [cv2.IMWRITE_PNG_COMPRESSION,9]
# imwrite : 배열데이터를 이미지파일로 저장

import matplotlib.pyplot as plt

cv2.imwrite("images/write_test0.png",image)
test0 = cv2.imread("images/write_test0.png")
plt.imshow(test0)

cv2.imwrite("images/write_test1.jpg",image)
test1 = cv2.imread("images/write_test1.jpg")
plt.imshow(test1)

# cv2.IMWRITE_JPEG_QUALITY,10 : 화질설정
#                 0 ~ 100(95) : 훟자가 높으면 화질이 좋음
params_jpg = (cv2.IMWRITE_JPEG_QUALITY,95) # 튜플 리스트가능
cv2.imwrite("images/write_test2.jpg",image,params_jpg)
test2 = cv2.imread("images/write_test2.jpg")
plt.imshow(test2)

cv2.imwrite("images/write_test3.png",image)
test3 = cv2.imread("images/write_test3.png")
plt.imshow(test3)

cv2.imwrite("images/write_test4.bmp",image)
test4 = cv2.imread("images/write_test4.bmp")
plt.imshow(test4)

cv2.imwrite("images/write_test5.jpg",image,(cv2.IMWRITE_JPEG_QUALITY,100))
test5 = cv2.imread("images/write_test5.jpg")
plt.imshow(test5)

# 이미지 형태 분석

def print_matInfo(name, image):
    # image : 이미지를 읽은 배열값, 이미지데이터
    # image, dtype : 배열요소의 자료형
    if image.dtype == 'uint8' :    mat_type = "CV_8U" # 부호없는 8비트(0~255)
    elif image.dtype == 'int8' :    mat_type = "CV_8S" # 부호있는 8비트(-128~127)
    elif image.dtype == 'uint16' :    mat_type = "CV_16U" # 부호없는 16비트
    elif image.dtype == 'int16' :    mat_type = "CV_16S" # 부호있는 16비트
    elif image.dtype == 'float32' :    mat_type = "CV_32F" # 부호있는 32비트 실수형
    elif image.dtype == 'float64' :    mat_type = "CV_64F" # 부호있는 64비트 실수형
    # image.ndim : 배열의 치수
    nchannel = 3 if image.ndim == 3 else 1
    print("%12s: dtype(%s),channels(%s) -> mat_type(%sC%d)" % (name,image.dtype,nchannel,mat_type,nchannel))
    
# imread : 이미지파일을 배열 저장
gray2gray = cv2.imread("images/read_gray.jpg",cv2.IMREAD_GRAYSCALE)
gray2color = cv2.imread("images/read_gray.jpg",cv2.IMREAD_COLOR )
gray2colors = cv2.imread("images/read_gray.jpg",cv2.IMREAD_UNCHANGED)

color2gray = cv2.imread("images/read_color.jpg",cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("images/read_color.jpg",cv2.IMREAD_COLOR )
color2colors = cv2.imread("images/read_color.jpg",cv2.IMREAD_UNCHANGED)

png2gray = cv2.imread("images/write_test0.png",cv2.IMREAD_GRAYSCALE)
png2color = cv2.imread("images/write_test0.png",cv2.IMREAD_COLOR )
png2colors = cv2.imread("images/write_test0.png",cv2.IMREAD_UNCHANGED)

bmp2gray = cv2.imread("images/write_test4.bmp",cv2.IMREAD_GRAYSCALE)
bmp2color = cv2.imread("images/write_test4.bmp",cv2.IMREAD_COLOR )
bmp2colors = cv2.imread("images/write_test4.bmp",cv2.IMREAD_UNCHANGED)

print_matInfo("gray2gray", gray2gray)
print_matInfo("gray2color", gray2color)
print_matInfo("gray2colors", gray2colors)

print_matInfo("color2gray", color2gray)
print_matInfo("color2color", color2color)
print_matInfo("color2colors", color2colors)

print_matInfo("png2gray", png2gray)
print_matInfo("png2color", png2color)
print_matInfo("png2colors", png2colors)

print_matInfo("bmp2gray", bmp2gray)
print_matInfo("bmp2color", bmp2color)
print_matInfo("bmp2colors", bmp2colors)


color1 = cv2.imread("images/read_16.tif", cv2.IMREAD_UNCHANGED)
color2 = cv2.imread("images/read_32.tif", cv2.IMREAD_UNCHANGED) # 손상된건가?
color1.shape
color2.shape
color1[10,10]
color2[10,10]
cv2.imshow("read_16.tif",color1)
cv2.imshow("read_32.tif",color2)
cv2.waitKey(0)
cv2.destroyAllWindows() 
print_matInfo("color1", color1)
print_matInfo("color2", color2)

import numpy as np
# image resize
img = cv2.imread('images/read_color.jpg')
height,width=img.shape[:2]

# 원하는 크기로 이미지 조절 (180 x 180 으로 만들기)
hr = 180/height
wr = 180/width

reset_size = np.float32([[hr,0,0],[0,wr,0]])

reset_dst = cv2.warpAffine(img,reset_size,(int(width*wr),int(height*hr)))
reset_dst.shape

cv2.imshow("reset_dst",reset_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 비율로 조절
# --0.5배 축소 변환 행렬
m_small = np.float32([[0.5,0,0],[0,0.5,0]])

# --2배 확대 변환 행렬
m_big = np.float32([[2,0,0],[0,2,0]])

# 보간법 적용 없이 확대 축소
dst1 = cv2.warpAffine(img,m_small,(int(width*0.5),int(height*0.5)))
dst1.shape
dst2 = cv2.warpAffine(img,m_big,(int(width*2),int(height*2)))
dst2.shape

# 보간법 
'''
 cv2.INTER_NEAREST - 최근방 이웃 보간법 : 
     퀄리티 나쁘다 : 잘사용 않함
 cv2.INTER_LINEAR - 양선형 보간법(2x2 이웃 픽셀 참조)
     4개의 픽셀 사용 (효율성 좋음) : 속도 빠르고 퀄리티 좋음
 cv2.INTER_CUBIC - 3차회선 보간법(4x4 이웃 픽셀 참조)
     16개의 픽셀을 사용  cv2.INTER_LINEAR 보다 퀄리티 좋음
 cv2.INTER_LANCZOS4 - Lanczos 보간법 (8x8 이웃 픽셀 참조)
     64개의 픽셀을 사용 복잡해서 오래 걸리지만 퀄리티 좋음
 cv2.INTER_AREA - 영상 축소시 효과적
 
 '''

reset_dst = cv2.warpAffine(img,reset_size,(int(width*wr),int(height*hr),None,cv2.INTER_AREA))
reset_dst.shape

cv2.imshow("reset_dst",reset_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

































