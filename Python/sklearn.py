

# ------------ Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(criterion='gini')
clf = clf.fit(X_train, y_train)

# feature importance in order of columns of X
feature_importances = clf.feature_importances_


