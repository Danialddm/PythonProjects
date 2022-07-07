from sklearn import datasets;
from sklearn import preprocessing;
iris = datasets.load_iris();
irisdata= iris.data# data value 150 * 4
iristarget= iris.target# target value
targetlabels = iris.target_names #class labels: ['setosa' 'versicolor' 'virginica']
#normaldata = preprocessing.scale(irisdata)#mean 0 , sdv 1
normaldata = preprocessing.normalize(irisdata,'l1')#0 , 1
#SOM network
from minisom import MiniSom;
#eta = MiniSom._decay_function(0.5,2,100);
som = MiniSom(x=8,y=8,input_len=4,sigma=1,learning_rate=0.5);#grid 6 * 6 , data dimen.=4
weights = som.random_weights_init(data=normaldata);
som.train_random(data=normaldata,num_iteration=100);
cordinateofwin = som.winner(normaldata[9]);#the coordinates of the winning neuron for the sample x
win = som.win_map(normaldata);
label = som.labels_map(normaldata,iristarget);
error = som.topographic_error(normaldata);
dist = som.distance_map();
print(error);
#visualizing the results
from pylab import bone, pcolor, colorbar, plot, show
bone();# intiialize figure window
pcolor(som.distance_map().T);#plots distances in one matrix, transpose .T
# optional label
colorbar(); # Adds legend of normalize value
markers = ['a','b','c'] # add marker to data
colors = ['r','g'] #color the markers
show();