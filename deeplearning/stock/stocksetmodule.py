# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:12:04 2023

@author: KITCOOP
"""

import numpy as np

def MinMaxScaler(data) : 
    # 최솟값과 최대값을 이용하여 0과 1사이의 값으로 변환
    mingap = data - np.min(data,0)
    gap = np.max(data,0) - np.min(data,0)
    # 0 으로 나누기 에러가 발생하지 않도록 ㅂ매우작은 값(1e-7)을 더해서 나눔
    return mingap/(gap + 1e-7)


'''
    tempx = data - min / (max - min + 1e - 7)
    data = tempx * (max - min) + min
    
'''