from keras.models import Sequential
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.optimizers import adadelta
from keras import metrics
import numpy as np

X_Train = np.genfromtxt(r'C:\Users\Devin\Desktop\PokerBot\HandDataTrain.txt', dtype=int)
X_Test = np.genfromtxt(r'C:\Users\Devin\Desktop\PokerBot\HandDataTest.txt', dtype=int)
Y_Train = np.genfromtxt(r'C:\Users\Devin\Desktop\PokerBot\HandResultsTrain.txt', dtype=int)
Y_Test = np.genfromtxt(r'C:\Users\Devin\Desktop\PokerBot\HandResultsTest.txt', dtype=int)

epochs = 50

model = Sequential()

model.add(Dense(1024, activation='relu', input_shape=(366, )))
model.add(Dense(1024, activation='relu'))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(4096, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_Train, Y_Train, batch_size=256, validation_data=(X_Test, Y_Test), verbose=1, epochs = 40)

model.save('Poker_Model.h5')
