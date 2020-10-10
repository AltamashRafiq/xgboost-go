import xgboost as xgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

dtrain = xgb.DMatrix(X_train, label=y_train)
param = {'max_depth': 4, 'eta': 1, 'objective': 'multi:softmax', 'nthread': 4,
         'eval_metric': 'auc', 'num_class': 3}

num_round = 10
bst = xgb.train(param, dtrain, num_round)
y_pred = bst.predict(xgb.DMatrix(X_test))

np.savetxt('../data/iris_xgboost_true_prediction.txt', y_pred, delimiter='\t')
np.savetxt('../data/iris_test.tsv', X_test, delimiter='\t')
bst.dump_model('../data/iris_xgboost_dump.json', dump_format='json')
bst.save_model('../data/iris_xgboost.json')
