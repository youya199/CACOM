from sklearn.neighbors import KernelDensity
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# rng = np.random.RandomState(42)
# X = np.array([[0,0],[2,2],[3,3],[3,4],[4,0],[99,98],[999,998]])#when testing, please delete first two lines and use real data instead


def find6(X):#X contains all points, each row is a point, each column is a dimension
    #find core
    kde = KernelDensity(kernel='gaussian', bandwidth=0.8).fit(X)
    log_density = kde.score_samples(X)
    a=log_density
    ai=a.argmax()
    core=X[ai].reshape(1,-1)
     #find 6 points around core
    nbrs = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(core)
    # output a list of these six points
    b=indices.flatten()
    return X[b]

# # b=find6(X)
#Y=pd.read_csv('Extracted_point_fr250-510.csv',header=None,dtype='a')

# Z=np.array([])
# # for index,X in Y.iterrows():
# #     b=X.dropna()
# #     Z[index,:]=find6(b)
#b=Y.iloc[0].dropna()#.astype('float')

#print(type(b.iloc[3]))
X=np.array([
    [171, 628],
    [242, 608],
    [281, 563],
    [285, 534],
    [305, 458],
    [311, 634],
    [312, 634],
    [313, 634],
    [314, 634],
    [316, 635],
    [316, 636],
    [317, 636],
    [318, 636],
    [318, 635]

    ])
#print(X)
#X=find6(X)
plt.scatter(X[:,1],X[:,0])
plt.show()