import pandas as pd
import time
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    print("Starting read data ...")
    time_one = time.time()
    raw_data = pd.read_csv('./train.csv', header=0)
    data = raw_data.values
    features = data[::, 1::]
    labels = data[::, 0]
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.25, random_state=False)
    time_two = time.time()
    print("read data cost %f seconds " % (time_two - time_one))
    print('Start training ...')
    # criterion可选‘gini’, ‘entropy’，默认为gini(对应CART算法)，entropy为信息增益（对应ID3算法）
    clf = DecisionTreeClassifier(criterion='gini')
    clf.fit(train_features, train_labels)
    time_three = time.time()
    print('training cost %f second' % (time_three - time_two))
    print('Start predicting...')
    test_predict = clf.predict(test_features)
    time_four = time.time()
    print('predicting cost %f seconds' % (time_four - time_three))
    score = accuracy_score(test_labels, test_predict)
    print('the accurary score id % f' % score)



