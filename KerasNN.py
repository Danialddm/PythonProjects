import keras;
from keras.utils import to_categorical
import numpy as np;
from keras.models import Sequential;
from keras.layers import Dense, Dropout, Activation;
from keras.optimizers import SGD;
from ann_visualizer.visualize import ann_viz;
from graphviz import Graph;

x_train = np.random.random((50, 20));
y_train = keras.utils.to_categorical(np.random.randint(10, size=(50, 1)), num_classes=10);
x_test = np.random.random((25, 20));
y_test = keras.utils.to_categorical((np.random.randint(10, size=(25, 1))), num_classes=10);
model = Sequential();
model.add(Dense(64, activation='relu', use_bias=True, input_dim=20));  # input layer , hidden 1
model.add(Dropout(0.5));
model.add(Dense(64, activation='relu', use_bias=True));  # hidden 2
model.add(Dropout(0.5));
model.add(Dense(10, activation='softmax'));
sgd = SGD(lr=0.01, momentum=0.9, decay=1e-6);
model.compile(sgd, loss='categorical_crossentropy', metrics=['accuracy']);  # config the model
history = model.fit(x_train, y_train, epochs=20, batch_size=128,
                    validation_data=(x_test, y_test));  # training the model

scoreoftest = model.evaluate(x_test, y_test, batch_size=128);  # evaluate the test model

# y_pred = model.predict(x_test);#prediction of test inputs
# print("\n%s: %.2f%%" % (model.metrics_names[1], score[1]*100));
# ann_viz(model, view=True, filename="MyNetwork.gv", title="MyNeuralNetwork");

# Plotting chart of training and testing accuracy as a function of iterations
from matplotlib import pyplot as plt;

fig = plt.figure(figsize=(11, 7));
plt.subplot(2, 1, 1);
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.subplot(2, 1, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['TrainLoss', 'TestLoss'], loc='upper left')

plt.show();

# az en func ham mitavan estefade kard
# @@mohem@@bayad graphviz hatman rooye system nasb bashad.
from graphviz import Digraph, Source;

g1 = Source.from_file('/usr/local/bin/net.gv');
g1.view();

Source.from_file('/Users/dani/Desktop/PythonProjects/net.gv')
Digraph.render('dot', 'png', '/Users/dani/Desktop/PythonProjects/net.gv', view=True)
# Digraph.render.save(filename='net', directory='/Users/dani/Desktop/PythonProjects/net.pdf')
# filepath = save(filename='net', directory='/Users/dani/Desktop/PythonProjects/net.pdf')

from graphviz import Source;

plo = Source.from_file('/Users/dani/Desktop/PythonProjects/net.gv');
plo.save(filename='network', directory='/Users/dani/Desktop/PythonProjects')
Source.render('self', filename='network', view=True)
