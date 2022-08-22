import pandas as pd

class svm1: 
    df = pd.read_csv('/Users/admin65/Desktop/Python_Machine_Learning_Algorithms/SVM_ALGO/iris.csv')
    df = df.drop(['Id'],axis=1)
    target = df['Species']
    s = set()
    for val in target:
        s.add(val)
    s = list(s)
    rows = list(range(100,150))
    df = df.drop(df.index[rows])
