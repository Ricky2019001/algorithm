from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
import xgboost as xgb

# 构造数据集
iris = datasets.load_iris()
data = iris.data[:100]
# print(data.shape)
label = iris.target[:100]
# print(label.shape)

# 训练集和测试集划分
train_x, test_x, train_y, test_y = train_test_split(data, label, random_state=42)

# Xgboost 建模
# 模型初始化
dtrain = xgb.DMatrix(train_x, test_y)
dtest = xgb.DMatrix(test_x)
paras = {'booster':'gbtree',
	'eval_metric': 'auc',
	'max_depth':4,
	'subsample':0.75,
	'colsample_bytree':0.75,
	'min_child_weight':2,
	'eta': 0.025,
	'seed':12}
watchlist = {(dtrain,'train')}

# 建模与预测
bst = xgb.train(paras, dtrain, num_boost_round=100,evals=watchlist)
ypred = bst.predict(dtest)
y_pred = (ypred > .5) * 1

# 指标评价
print('AUC: %.4f' % metrics.roc_auc_score(test_y,ypred))
print('ACC: %.4f' % metrics.accuracy_score(test_y,y_pred))
print('Recall: %.4f' % metrics.recall_score(test_y,y_pred))
print('F1-score: %.4f' %metrics.f1_score(test_y,y_pred))
print('Precesion: %.4f' %metrics.precision_score(test_y,y_pred))
print(metrics.confusion_matrix(test_y,y_pred))




