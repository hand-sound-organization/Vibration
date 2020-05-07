from sklearn import neighbors, datasets
import numpy as np
n_neighbors = 2

# import some data to play with
iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target
# print(X)

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    k_neighbors = clf.kneighbors(np.array([[5.5,3.7]]),n_neighbors)
    print(X[k_neighbors[1][0][0]],X[k_neighbors[1][0][1]])

