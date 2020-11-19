import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import make_gaussian_quantiles

x1, y1 = make_gaussian_quantiles(n_samples=100, n_features=2, n_classes=3,shuffle=True, random_state=None)
x2, y2 = make_gaussian_quantiles(mean=(3,3), cov=1.5, n_samples=300, n_features=2, n_classes=2, shuffle=True, random_state=1)
X = np.vstack((x1, x2))
Y = np.hstack((y1, y2))
# plt.scatter(X[:,0], X[:, 1])
# plt.show()

#设定弱分类器CART
weakClassifier = DecisionTreeClassifier(max_depth = 1)

# 构建模型
clf = AdaBoostClassifier(base_estimator=weakClassifier,
                         n_estimators=300,
                         learning_rate=.1,
                         algorithm='SAMME')
clf.fit(X, Y)

# 制图
x1_min=X[:,0].min()-5
x1_max=X[:,0].max()+1
x2_min=X[:,1].min()-5
x2_max=X[:,1].max()+1
x1,x2=np.meshgrid(np.arange(x1_min,x1_max,0.02), np.arange(x2_min,x2_max,0.02))
print(x1.shape)
print(x2.shape)
print(x1.ravel())
print(x2.ravel())
y=clf.predict(np.c_[x1.ravel(),x2.ravel()])
print(y.shape)
print(x1.shape)
# y=y.reshape(x1.shape)
