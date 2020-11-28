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
train_x, test_x, train_y, test_y = train_test_split(data, label, test_size=0.25, random_state=42)

# Xgboost 建模
# 模型初始化
dtrain = xgb.DMatrix(train_x, train_y)
dtest = xgb.DMatrix(test_x)
params={'booster':'gbtree',
	'objective': 'binary:logistic',
	'eval_metric': 'auc',
	'max_depth':4,
	'lambda':10,
	'subsample':0.75,
	'colsample_bytree':0.75,
	'min_child_weight':2,
	'eta': 0.025,
	'seed':0,
	'nthread':8,
     'silent':1}
watchlist = {(dtrain,'train')}

# 建模与预测
bst = xgb.train(params, dtrain, num_boost_round=102,evals=watchlist)
ypred = bst.predict(dtest)
y_pred = (ypred > .5) * 1

# 指标评价
print('AUC: %.4f' % metrics.roc_auc_score(test_y,ypred))
print('ACC: %.4f' % metrics.accuracy_score(test_y,y_pred))
print('Recall: %.4f' % metrics.recall_score(test_y,y_pred))
print('F1-score: %.4f' %metrics.f1_score(test_y,y_pred))
print('Precesion: %.4f' %metrics.precision_score(test_y,y_pred))
print('混淆矩阵:',end='\t')
print(metrics.confusion_matrix(test_y,y_pred))

# 可视化输出
"""
bst.predict
Signature: bst.predict(data, output_margin=False, ntree_limit=0, pred_leaf=False, pred_contribs=False, approx_contribs=False)

pred_leaf : bool
    When this option is on, the output will be a matrix of (nsample, ntrees)
    with each record indicating the predicted leaf index of each sample in each tree.
    Note that the leaf index of a tree is unique per tree, so you may find leaf 1
    in both tree 1 and tree 0.

pred_contribs : bool
    When this option is on, the output will be a matrix of (nsample, nfeats+1)
    with each record indicating the feature contributions (SHAP values) for that
    prediction. The sum of all feature contributions is equal to the prediction.
    Note that the bias is added as the final column, on top of the regular features.
"""
# 4.3.1 得分
print(ypred)

# 当设置pred_leaf=True的时候, 这时就会输出每个样本在所有树中的叶子节点
ypred_leaf = bst.predict(dtest, pred_leaf=True)
print(ypred_leaf.shape)
# 特征重要性, 输出的是特征相对于得分的重要性.
# 最后一列是bias, 前面的四列分别是每个特征对最后打分的影响因子, 可以看出, 前面两个特征是不起作用的
ypred_contribs = bst.predict(dtest,pred_contribs=True)
print(ypred_contribs)
print(ypred_contribs.shape)