#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:10:36 2023

@author: cjh
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# 가상의 데이터셋 생성
X = np.array([[1066, 6440, 0.096170],
              [4974, 2585, 0.028739],
              [3792, 5277, 0.060960],
              [7395, 6735, 0.048697],
              [4064, 6321, 0.036650]])
y = np.array([3469, 5240, 9079, 1702, 3730])

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X, y)

# 새로운 입력 데이터에 대한 예측 수행
new_data = np.array([[2000, 1000, 0.039483]])
predicted = model.predict(new_data)

print("예측 결과:", predicted)
