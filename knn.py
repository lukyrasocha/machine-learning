# Author: Lukas Rasocha
# livecoded this for the first semester students to show them how KNN works

def distance(x1,x2): #Takes two datapoints in n-space
    sum_ = 0
    for i in range(len(x1)):
        sum_ += (x1[i]-x2[i])**2

    return sum_**(1/2) # Returns the distance of the two datapoints


class KNN:
    def __init__(self,n_neighbours): 
        self.n_neighbours = n_neighbours 
        self.x = None #features
        self.y = None #y_target
        self.n = None #length

    def fit(self,X,y):
        self.x = X
        self.y = y
        self.n = len(X)

    def predict(self, xs):
        predictions = []
        for point in xs:
            distances = []
            for training_index in range(self.n):
                dist = distance(point,self.x[training_index])
                distances.append((dist,self.y[training_index]))
            distances = sorted(distances, key=lambda x: x[0])
            closest_points = []
            for closest in range(self.n_neighbours):
                closest_points.append(distances[closest][1])

            predictions.append(Counter(closest_points).most_common()[0][0])

        return predictions



if __name__ == '__main__':
    from sklearn.datasets import load_iris
    import numpy as np
    from collections import Counter

    dataset = load_iris()
    x = dataset.data # Datapoints (features) like [10,15.2,13.1]
    y_target = dataset.target # Classes like so [0,1,0,2,1,1,...]

    clf = KNN(n_neighbours = 4) # 1 here what happens
    clf.fit(x,y_target)
    y_pred = clf.predict(x)

    print("TRUE LABELS")
    print(y_target)
    print("------------")
    print("PREDICTED LABELS")
    print(y_pred)
        



