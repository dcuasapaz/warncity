from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Clase para retorno
class Category:
    def __init__(self, sitio,color,texto,option, value):
        self.sitio = sitio
        self.color = color
        self.texto = texto
        self.option = option
        self.value = value

@app.post("/category/{id_sitio}")
def categorizar_sitio(id_sitio: int):
    # 1. Leer el csv de datos consolidados
    import pandas as pd
    df=pd.read_csv('./data/municipios.csv', sep=',',header=0)
    df.head()
    # 2. Desplegar info del dataset (df)
    df.info()
    print('Dataset shape ::', df.shape)
    # 3. Filtrar dataset por el sitio
    df = df[(df['i_ste_cde'] == id_sitio)]
    print('Dataset shape ::', df.shape)
    # 4. Definir variables Predictoras
    X=df.iloc[:,3:11]
    X.head()
    # 5. Definir variables a predecir
    Y=df.iloc[:,1]
    Y.head()
    # 6. Establecer datos de entrenamiento
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.75, random_state = 0)
    # Llamar al constructor del arbol de decision 
    tree = DecisionTreeClassifier()
    # Entrenamos el modelo
    tree_site = tree.fit(X_train, Y_train)
    print(tree_site)
    # 7. Predecir variable
    Y_pred=tree_site.predict(X_test)
    print(Y_pred)
    # 8. Matriz de confusion
    from sklearn.metrics import confusion_matrix
    matrix_confution=confusion_matrix(Y_test,Y_pred)
    print(confusion_matrix(Y_test,Y_pred))
    # 9. Precision global del modelo
    import numpy as np 
    global_precition = np.sum(matrix_confution.diagonal())/np.sum(matrix_confution)
    print(global_precition)
    # 10. Precision por categorias del modelo
    global_precition_class_0 = ((matrix_confution[0,0]))/sum(matrix_confution[0,])
    print(global_precition_class_0)
    global_precition_class_1 = ((matrix_confution[1,1]))/sum(matrix_confution[1,])
    print(global_precition_class_1)
    global_precition_class_2 = ((matrix_confution[2,2]))/sum(matrix_confution[2,])
    print(global_precition_class_2)
    global_precition_class_3 = ((matrix_confution[3,3]))/sum(matrix_confution[3,])
    print(global_precition_class_3)
    # 11. Clasificar resultados
    list_values = [
        Category(id_sitio,'Gris','NO CALIFICADO',0, global_precition_class_0),
        Category(id_sitio,'Rojo','INICIANDO',1, global_precition_class_1),
        Category(id_sitio,'Amarillo','SATISFACTORIO',2, global_precition_class_2),
        Category(id_sitio,'Verde','OPTIMO',3, global_precition_class_3)
    ]
    # 12. Obtener valor a mostrar
    max_class = max(list_values, key=lambda category: category.value)
    return max_class