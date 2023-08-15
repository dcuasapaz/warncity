import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Genera un conjunto de datos de ejemplo para clasificación
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un Árbol de Clasificación
clf = DecisionTreeClassifier()

# Entrena el modelo
clf.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcula la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo de Árbol de Clasificación: {:.2f}".format(accuracy))

# Muestra el informe de clasificación
print("Informe de clasificación:")
print(classification_report(y_test, y_pred))
