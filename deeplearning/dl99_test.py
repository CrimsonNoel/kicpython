# -*- coding: utf-8 -*-

import numpy as np
from tensorflow.keras.datasets.mnist import load_data
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from PIL import Image
from keras.models import load_model
from sklearn.metrics import classification_report,confusion_matrix
import os,re,glob
import cv2

groups_folder_path = 'hansik/kfood_new/learning/'
categories = ["000", "001", "002"]
 
num_classes = len(categories)
num_classes  
image_w = 28
image_h = 28

X = []
Y = []
Z = []

# 손상된 이미지는 rgb가아니라 p가 나온다 img.mode 
# PIL 형식으로 다시짜야함
for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'
  
    for top, dir, f in os.walk(image_dir):
        for filename in f:
            try:
                print(image_dir+filename)
                # img = Image.open(image_dir + filename)
                img = cv2.imread(image_dir + filename)
                img = cv2.resize(img,(image_w, image_h))
                img = img / 255.0
                #img = cv2.resize(img, (image_w, image_h))  # 이미지 크기를 (image_w, image_h)로 조정
                #print(img.shape,'2')
                img = np.array(img) / 255.0  # 이미지 값을 [0, 1] 범위로 정규화
                print(img.shape)
                X.append(img)
                Y.append(label)
            except:
                print(image_dir+filename,'예외처리')
                Z.append(image_dir+filename)
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
xy = (X_train, X_test, Y_train, Y_test)
 
np.save("hansik/kfood_resize/kfood_resize.npy", xy)
print(Z) # 예외처리 파일

print(xy)
type(xy[0][0][0][0])
'''
    ValueError: Unknown resampling filter (28). Use Image.Resampling.NEAREST (0), 
                            Image.Resampling.LANCZOS (1), Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3), 
                            Image.Resampling.BOX (4) or Image.Resampling.HAMMING (5)
    PIL img.resize 사용시 
        img.resize((width,height),보간법)
'''
img = Image.open('hansik/kfood_new/learning/000/Img_000_0197.jpg')
img_mode = img.mode
img_mode
imgr = img.resize((image_w, image_h))
img
img_array = np.array(imgr)/255.0
img_array
print(img)
np.save("hansik/kfood_resize/kfood_resize.npy", img_array)
tp = np.load("hansik/kfood_resize/kfood_resize.npy",allow_pickle=True)
len(tp[0][0][0][0][0])
tp[0][0][0]
'''
     tensorflow 가 자동으로 resize까지 다해준다함.
'''








