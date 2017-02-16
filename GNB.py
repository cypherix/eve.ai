import numpy as np
def machine_learning(x):
    
    X = np.array([[10],[20],[30],[40],[48],[49],[50],[51],[60],[79],[78],[80],[90],[100]])
    Y = np.array(['r','r','r','r','r','r','m','m','m','m','m','x','x','x'])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(X, Y)
    GaussianNB(priors=None)
    return(clf.predict([[x]]))
