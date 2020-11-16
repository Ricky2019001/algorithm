from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data[:,2:] # feature_names=['sepal length (cm)', 'sepal width (cm)','petal length (cm)', 'petal width (cm)'])
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
rnd_forest_clf = RandomForestClassifier(n_estimators=15, max_leaf_nodes=20, n_jobs=8, oob_score=True)
rnd_forest_clf.fit(X_train, y_train)
y_test_pred = rnd_forest_clf.predict(X_test)
print(accuracy_score(y_test, y_test_pred))
print(rnd_forest_clf.oob_score_)

iris = load_iris()
rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=8)
rnd_clf.fit(iris.data, iris.target)
for name, score in zip(iris.feature_names, rnd_clf.feature_importances_):
    print(name, score)



