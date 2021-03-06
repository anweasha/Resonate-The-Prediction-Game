# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np

data = pd.read_csv('resonateData.csv')

director = input("enter the director name")
cast1 = input("enter the first cast name")
cast2 = input("enter the second cast name")
cast3 = input("enter the third cast name")
genre = input("enter the genre of the movie")
runtime = float(input("enter the runtime of the movie"))
release_year = int(input("enter the release year of the movie"))


dict1 = {'director': director,
'cast1' : cast1,
'cast2' : cast2,
'cast3' : cast3,
'genre' : genre,
'runtime' : runtime,
'release_year' : release_year}

data = data.append(dict1,ignore_index=True)

X_cat = data[['director',
 'cast1',
 'cast2',
 'cast3',
 'genre']]

X_Num = data[['runtime',
 'release_year']]

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
X_cat = onehotencoder.fit_transform(X_cat).toarray()
X_cat = pd.DataFrame(X_cat)


X_all = pd.concat([X_cat, X_Num], axis = 1)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(X_all)

data.drop(index=data.shape[0]-1,inplace = True,axis=0)

y = data['category']
reshape = X_all.shape[-1]
data1 = X[-1]
data1 = data1.reshape(-1,reshape)

X = np.delete(X,-1,axis = 0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

inputShape = X_train.shape[1]

import tensorflow as tf 

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(units = 500 , activation = 'relu' , input_shape =(inputShape, )))
model.add(tf.keras.layers.Dense(units = 500 , activation =  'relu'))
model.add(tf.keras.layers.Dense(units = 500 , activation =  'relu'))
model.add(tf.keras.layers.Dense(units = 1 , activation =  'sigmoid'))

model.compile(optimizer= "Adam" , loss = "binary_crossentropy", metrics=['accuracy'])

epochs_hist = model.fit(X_train,y_train , epochs=10, batch_size=50)

y_pred = model.predict(data1)

y_pred = (y_pred > 0.5)

value = (y_pred)
if value[0,0] ==  True:
 print("Hit!")
else:
 print("Flop!")

