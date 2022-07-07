import os
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

start_time = time.process_time()  # processor time


# convert an array of values into a dataset matrix
def create_dataset(dataset, time_steps):
    dataX, dataY = [], []
    for i in range(time_steps, dataset.size):
        dataX.append(dataset[i - time_steps:i, 0])
        dataY.append(dataset[i, 0])
    return np.array(dataX), np.array(dataY)


# --------------------- Data Preprocessing --------------------
total_dataset = pd.read_csv("data.csv")
data_set_1 = total_dataset.iloc[:, 1:2].values  # feature 1
data_set_2 = total_dataset.iloc[:, 2:3].values  # feature 2
# ---------------------------------------------------------------
# ---------------------Feature scaling-------------------------------------
sc = MinMaxScaler(feature_range=(0, 1))
data_set_scaled_1 = sc.fit_transform(data_set_1)
data_set_scaled_2 = sc.fit_transform(data_set_2)
# -------------------------------------------------------------------------
# -----------------split into train and test sets--------------------------
train_size_1 = int(len(data_set_scaled_1) * 0.67)
train_set_1 = data_set_scaled_1[0:train_size_1, :]
test_size_1 = len(data_set_scaled_1) - train_size_1
test_set_1 = data_set_scaled_1[train_size_1:len(data_set_scaled_1), :]

train_size_2 = int(len(data_set_scaled_2) * 0.67)
train_set_2 = data_set_scaled_2[0:train_size_2, :]
test_size_2 = len(data_set_scaled_2) - train_size_2
test_set_2 = data_set_scaled_2[train_size_2:len(data_set_scaled_2), :]
# --------------------------------------------------------------------------
time_steps = 2
features = 1
trainX_1, trainY_1 = create_dataset(train_set_1, time_steps)
trainX_2, trainY_2 = create_dataset(train_set_2, time_steps)
train_X = np.column_stack((trainX_1, trainX_2))
train_Y = np.column_stack((trainY_1, trainY_2))

testX_1, testY_1 = create_dataset(test_set_1, time_steps)
testX_2, testY_2 = create_dataset(test_set_2, time_steps)
test_X = np.column_stack((testX_1, testX_2))
test_Y = np.column_stack((testY_1, testY_2))
# -------------------------------------------------------------------------
# --------------- Vital Parameters (must be integer)-------------------------------
train_set_row = train_X.shape[0]
train_set_col = train_X.shape[1]
samples_train = (train_set_row * train_set_col)//2
test_set_row = test_X.shape[0]
test_set_col = test_Y.shape[1]
samples_test = (test_set_row * test_set_col)//1
# -----------------------------------------------------------------------------------


# Instead of phrasing the past observations as separate input features, we can use them as time steps of the one
# input feature, which is indeed a more accurate take prior time steps in our time series as inputs to predict the
# output at the next time step.
# [samples, time_steps, features]
# samples are the number of data, or say how many rows are there in your data set
# time step is the number of times to feed in the model or LSTM
# features is the number of columns of each sample OR [Pressure,Temperature] OR sequence input and a sequence output
# Many-to-Many (Encoder-Decoder Model) Sequence Problems with Single or multiple Features
# X = np.array(X).reshape(20, 3, 2) -- multiple Features(Many-to-Many)
# Y = np.array(Y).reshape(20, 3, 1)-- multiple Features(Many-to-Many)
# X = np.array(X).reshape(20, 3, 1) -- one Feature(Many-to-Many)
# Y = np.array(Y).reshape(20, 3, 1) -- one Feature(Many-to-Many)
# if we want one time-step (in fact we have multiple features) with two features then the dense=2 (one to many with multiple features) - y=[a,b]
# if we want multiple time-steps with two features then the dense=1 (many to many with multiple features)
# if we want one time-step with two features then the dense =1 (many to one with one feature)

x_train = np.array(train_X).reshape(32, 2, 2)
y_train = np.array(train_Y).reshape(32, 2, 1)


x_test = np.array(test_X).reshape(16, 2, 2)
y_test = np.array(test_Y).reshape(16, 2, 1)

# --------------------- Building RNN/LSTM model --------------------#
# if you have 1000 training examples, and your batch size is 500, then it will take 2 iterations to complete 1 epoch. #
# create and fit the LSTM network
model = Sequential()
# model.add(Bidirectional(LSTM(50, activation='relu'), input_shape=(3, 1)))
model.add(LSTM(32, input_shape=(2, 2)))
model.add(Dense(units=1))
model.compile(loss='mean_squared_error', optimizer='adam')
print(model.summary())
model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1)
"""
# Adding the first LSTM layer--Stacked LSTM
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))

# Adding the second LSTM layer--return_sequence means neuron is used as an input to the next LSTM layer.
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

# Adding the third LSTM layer
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

# Adding the forth LSTM layer
## model.add(LSTM(units=32, return_sequences=True))
## model.add(Dropout(0.2))

# Adding the fifth LSTM layer
# note that this is the final LSTM layer, hence we change the binary argument to False
model.add(LSTM(units=50))
model.add(Dropout(0.2))

# Adding output layer to the RNN to make a fully connected NN
model.add(Dense(units=1))

# --------------------- Compiling the RNN model --------------------#
model.compile(optimizer='adam', loss='mean_squared_error')

# --------------------- Training RNN model --------------------#
# connecting the built model to the training model
model.fit(x_train, y_train, epochs=250, batch_size=1, verbose=2)
"""
# obtaining predicted values
predicted_price_train = model.predict(x_train)
predicted_price_test = model.predict(x_test)

predicted_price_train = sc.inverse_transform(predicted_price_train)
y_train = ((y_train.shape[0]), 1)
y_train = sc.inverse_transform(y_train)
predicted_price_test = sc.inverse_transform(predicted_price_test)
y_test = sc.inverse_transform([test_Y])
# --------------------- Visualizing the LTSM model results--------------------#
# calculate root mean squared error

trainScore = math.sqrt(mean_squared_error(y_train[0], predicted_price_train[:, 0]))
print('Train Score: %.2f RMSE' % trainScore)
testScore = math.sqrt(mean_squared_error(y_test[0], predicted_price_test[:, 0]))
print('Test Score: %.2f RMSE' % testScore)

# shift train predictions for plotting
trainPredictPlot = np.empty_like(data_set_scaled)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(predicted_price_train) + look_back, :] = predicted_price_train
# shift test predictions for plotting
testPredictPlot = np.empty_like(data_set_scaled)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(predicted_price_train) + (look_back * 2) + 1:len(data_set_scaled) - 1, :] = predicted_price_test
# plot baseline and predictions
plt.plot(sc.inverse_transform(data_set_scaled), label="Real Dataset", color='blue')
plt.plot(trainPredictPlot, label="predicted train set", color='green')
plt.plot(testPredictPlot, label="predicted test set", color='red')
plt.legend(loc='upper left')
plt.show()
print(time.process_time() - start_time)
output_y = y_test[0]
print(output_y)
print("..........................")
output_predict = predicted_price_test[:, 0]
print(output_predict)
