import pandas as pd
import numpy as np
import keras
from keras.utils import np_utils
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Conv1D
from sklearn.preprocessing import LabelBinarizer
from keras import losses, optimizers

#load csv
trainset = pd.read_csv('Train.csv')
testset = pd.read_csv('Test.csv')

#get labels
trainY = train[100]
testY = test[100]

#set variable to categorical type


#drop labels in data
train = train.drop(columns=[100])
test = test.drop(columns=[100])

#Converts to vectors
train = train.as_matrix()
test = test.as_matrix()

trainY = np_utils.to_categorical(trainY.values)
testY = np_utils.to_categorical(testY.values)

#create CNN model
model = Sequential()
#first layer precise input shape (other use automatic shape inference)
model.add(Conv1D(100, 1, activation='relu', input_shape=(100,)))
model.add(Conv1D(100, 2, activation='relu'))
model.add(Conv1D(100, 3, activation='relu'))
model.add(Conv1D(100, 4, activation='relu'))
model.add(Conv1D(100, 5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(4, activation='softmax'))

#configure learning process (loss = objective to minimize, optimizer = way of training, metric = judge perf)
model.compile(loss='categorical_crossentropy',
                optimizer='adadelta',
                metrics=['accuracy'])

#train the model
model.fit(train, trainY, epochs=12, batch_size=128, shuffle=True, verbose=1)

#returns the loss value & metrics values for the model in test mode.
score = model.predict(test, verbose=2)
print('Test score:', score)

