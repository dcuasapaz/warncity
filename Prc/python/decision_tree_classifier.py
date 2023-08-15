from sklearn.tree import DecisionTreeClassifier

# Datos de entrenamiento (características)
X_train = [[8, 3], [6, 2], [7, 1], [7, 3], [6, 1], [5, 2], [6, 3], [5, 1]]

# Etiquetas de entrenamiento (clases correspondientes a las frutas: 0 para manzana, 1 para naranja)
y_train = [0, 0, 1, 0, 1, 1, 0, 1]

# Crear el clasificador del árbol de decisión
clf = DecisionTreeClassifier()

# Entrenar el modelo con los datos de entrenamiento
clf.fit(X_train, y_train)

# Datos de prueba (características de frutas desconocidas)
X_test = [[7, 2], [4, 3], [8, 2]]

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Imprimir las predicciones
for i, prediction in enumerate(y_pred):
    fruit = "manzana" if prediction == 0 else "naranja"
    print(f"Fruta {i + 1}: {fruit}")