from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Decision Tree Structure:\n", tree_rules)
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
