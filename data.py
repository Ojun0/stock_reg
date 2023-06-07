#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:05:27 2023

@author: cjh
"""

import pandas as pd
import random

# 가상의 재무 데이터셋 생성
n = 100  # 데이터 개수
start_date = pd.to_datetime('2023-01-01')  # 시작일
end_date = pd.to_datetime('2023-12-31')  # 종료일

data = []
for _ in range(n):
    date = pd.to_datetime(random.choice(pd.date_range(start_date, end_date)))  # 무작위 날짜 선택
    sales = random.randint(1000, 10000)  # 매출액
    expenses = random.randint(500, 8000)  # 비용
    interest_rate = random.uniform(0.01, 0.1)  # 이자율
    exchange_rate = random.uniform(1.0, 2.0)  # 환율
    
    data.append([date, sales, expenses, interest_rate, exchange_rate])

# 데이터프레임 생성
columns = ['Date', 'Sales', 'Expenses', 'Interest Rate', 'Exchange Rate']
df = pd.DataFrame(data, columns=columns)

# 데이터프레임 출력
print(df.head())