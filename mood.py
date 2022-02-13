# -*- coding: utf-8 -*-
"""mood.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hxzpgfa4RVIeEND5dudHOR7KFh2J4W0y
"""

import pandas as pd 
import joblib
import numpy as np
import pickle

df = pd.read_csv('/mnt/d/Hashcode/Hashcode_2022/data/25.csv')
y=pd.read_csv('/mnt/d/Hashcode/Hashcode_2022/data/25.csv')

# df.head

# df.columns

df.drop(['date','mood'],axis=1,inplace=True)

y.drop(['date','step_count','calories_burned', 'hours_of_sleep',
       'bool_of_active', 'weight_kg'],axis=1, inplace=True)

# y.head

def fun(x):
  if x==500:
    return 1
  else:
    return 0
df['bool_of_active']=df['bool_of_active'].apply(fun)

def fun2(x):
  if x==100:
    return 1
  elif x==200:
    return 2
  else:
    return 3

y['mood']=y['mood'].apply(fun2)

# df.shape

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

model = XGBClassifier()
X_train, X_test, y_train, y_test = train_test_split(
    df, y, stratify=y, train_size = 0.3 ,random_state=1121218 , shuffle = True
)
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
print(acc)
joblib.dump(model,'model') 
print("dumped!")