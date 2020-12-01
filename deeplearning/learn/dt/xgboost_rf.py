from xgboost import XGBRegressor as XGBR
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split, cross_val_score, KFold
import numpy as np

data = load_boston()
X = data.data
Y = data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.75, random_state=42)
# xgb
xgb_reg = XGBR(n_estimators=100).fit(X_train, Y_train)
print('训练模型的： %.9f' % xgb_reg.score(X_train, Y_train))
print('预测模型MSE： %.9f' % MSE(Y_test, xgb_reg.predict(X_test)))
print('交叉验证得分 % .9f' % cross_val_score(xgb_reg, X_train, Y_train, cv=5).mean())
