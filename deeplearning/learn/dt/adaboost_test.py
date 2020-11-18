import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
import time

if __name__ == '__main__':
    time_1 = time.time()
    raw_data = pd.read_csv('./train_binary.csv', header=0)
    data = raw_data.values
    features = data[:,1:]
    labels = data[:,0]
    print(features.shape, labels.shape)
    train_features, test_features, train_labels, test_labels = train_test_split(data, labels, test_size = 0.25, random_state = 42)
    time_2 = time.time()
    print('read data cost %f second' % (time_2 - time_1))
    clf = AdaBoostClassifier(n_estimators=50,algorithm='SAMME.R')
    clf.fit(train_features, train_labels)
    time_3 = time.time()
    print('train data cost %f second' % (time_3 - time_2))
    test_predict = clf.predict(test_features)
    time_4 = time.time()
    print('by model predicting data cost %f second' % (time_4 - time_3))
    score = accuracy_score(test_labels,test_predict)
    print('accuracy rate %f ' % score)