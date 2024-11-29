# %%
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report,confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# %%
X, y = load_iris(return_X_y= True, as_frame = True)
iris = load_iris()
print(iris['DESCR'])

# %%
X.isnull().sum()

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# %%
model = DecisionTreeClassifier(random_state=42)

# %%
model.fit(X_train, y_train)
print(f"\nLa profondità dell'albero è: \t{model.get_depth()}\n")

# %%
y_pred = model.predict(X_test)

# %%
class_report = classification_report(y_test, y_pred, target_names = iris.target_names)
print(class_report)

# %%
cm = confusion_matrix(y_test, y_pred)
cm_display = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels=iris.target_names)
cm_display.plot()
plt.show()


