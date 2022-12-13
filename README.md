# <h1 align=center> **PROYECTO INDIVIDUAL Nº2** </h1>

# <h1 align=center>**`Datathon - Machine Learning`**</h1>

<p align="center">
<img src="https://miro.medium.com/max/1000/1*qHbAsMNmdWQJkzm2SUA-8w.jpeg"   
>
</p>


## Introducción:

¡Hola! 👋 Mi nombre es Emmanuel Fernandez, y este es mi segundo proyecto para la etapa de Labs de la carrera de Data Science de SoyHenry. Este proyecto busca situarnos en el rol de un Data Scientist contratado por un importante centro de salud para realizar un modelo de Machine Learning que pueda predecir si la estancia de un futuro paciente será prolongada o no. Para ello se nos entregan dos archivos .csv, uno sobre el cual instanciaremos y entrenaremos nuestro modelo y otro que será en el que debemos aplicarlo. Antes de todo esto, debemos realizar un EDA para corregir imperfecciones como diferencias en el tipo de los datos, valores nulos, duplicados, etc.

## Objetivos: 

+ Entrenamiento y predicción utilizando un Modelo de Machine Learning adecuado al problema (clasificación o regresión).

+ Análisis exploratorio de los datos (EDA).

+ División de dataset en train y test utilizando train_test_split, CV, KFold o similares.

+ Utilización de Pipelines en la producción del modelo.

+ Comentarios y redacción con la fundamentación de la solución propuesta, escrita en Markdown en el Jupyter Notebook (.ipynb) o bien en un documento aparte.

## Explicación del modelo:

Si bien este apartado se encuentra detallado paso a paso en el archivo `EDA_FeatureEng.ipynb`, a modo de resumen comento cómo encaré este problema. Luego de realizar un pequeño análisis de mis datos y algunas conversiones, como por ejemplo, utilizar LabelEncoder para convertir mis variables categóricas, decidí probar dos tipos de modelos de clasificación: Regresión Logística y Árbol de decisión. Hice un test utilizando un Árbol porque es el modelo con el que más familiarizado me encuentro, sin embargo, comparé ambos para verificar cuál de estos tenía una mejor accuracy. Además, a la hora de hacer el árbol utilicé la validación cruzada para sacar la profundidad óptima de mi árbol. Luego de hacer la selección de Features utilizando Chi², determiné las features óptimas para entrenar mi modelo, ajusté mis hiperparámetros y obtuve resultados positivos.

## Aclaraciones:

Hay algunas cosas a tener en cuenta, el análisis y modelo propuestos NO son necesariamente los más óptimos/mejores, varias decisiones fueron tomadas a mi propio criterio, por ejemplo, la profundidad del árbol, el uso del estadístico Chi² (como se comenta en el Notebook) para la selección de features en lugar de la correlación de Pearson, descarte de columnas que personalmente creía innecesarias (Como 'patientid' y 'Visitors with Patient'), etc...

## Explicación de los contenidos del Repositorio:

+ En la carpeta `datasets` se encuentran los datasets analizados, el archivo `hospitalizaciones_train.csv` que es el que utilizamos para instanciar y entrenar el modelo y el archivo `hospitalizaciones_test.csv` que es al que se le aplica el modelo ya terminado para sacar deducciones.

+ En el notebook `EDA_FeatureEng.ipynb` se encuentra el código comentado paso por paso, explicando las decisiones tomadas a la hora de encarar este proyecto;
    Esto se hizo así para tener dividido de manera ordenada los bloques de código, separados por los markdowns que van dividiendo las etapas del proceso.
    Con esto espero documentar y demostrar cada paso del desarrollo.

+ En el archivo `DecisionTree_model.pkl` se encuentra el modelo de árbol de decisión creado, importado con la librería de Joblib.

+ En el archivo `pred_generator.py` se encuentra el código que se encarga de realizar las transformaciones necesarias sobre el dataset `hospitalizaciones_test.csv` además de aplicarle el modelo, sacar las conclusiones y generar el archivo `Emmafer.csv` donde se encuentra mi columna de predicciones.

## Herramientas/librerías utilizadas:

+ Python. 🐍

+ Pandas. 🐼

+ Numpy. 📟

+ Mathplotlib. 📊

+ ScikitLearn. 🤖

+ Joblib. 📁

## Espero haberme sabido explicar y que les haya gustado! Gracias por leer a este nerd 🤓.

<p align="center">
<img src="https://media.tenor.com/e-tu1KPkCucAAAAC/the-simpsons-homer-simpson.gif"   
>
</p>
