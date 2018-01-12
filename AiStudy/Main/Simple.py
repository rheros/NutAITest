'''
Created on Jan 12, 2018

@author: sjl
'''
from keras.models import Sequential

from Main.Utility import *
from keras.layers.core import Dense
import keras


model=Sequential()
model.add(Dense(2,input_shape=(2,)))
model.add(Dense(100,activation='softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

x,y=getPlusOper(50)
z,w=getRandomPlusOper(100)
yy=keras.utils.to_categorical(y,num_classes=100)
# ww=keras.utils.to_categorical(w, num_classes=100)
# print(x)
# print(y)
# print(z)
# print(w)

# x_train = np.random.random((1000, 20))
# print(x_train)
model.fit(x,yy,epochs=10,batch_size=32)
# score=model.evaluate(z,ww,batch_size=32)
# print(score)