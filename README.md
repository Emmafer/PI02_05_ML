# <h1 align=center> **PROYECTO INDIVIDUAL N潞2** </h1>

# <h1 align=center>**`Datathon - Machine Learning`**</h1>

<p align="center">
<img src="https://miro.medium.com/max/1000/1*qHbAsMNmdWQJkzm2SUA-8w.jpeg"   
>
</p>


## Introducci贸n:

隆Hola! 馃憢 Mi nombre es Emmanuel Fernandez, y este es mi segundo proyecto para la etapa de Labs de la carrera de Data Science de SoyHenry. Este proyecto busca situarnos en el rol de un Data Scientist contratado por un importante centro de salud para realizar un modelo de Machine Learning que pueda predecir si la estancia de un futuro paciente ser谩 prolongada o no. Para ello se nos entregan dos archivos .csv, uno sobre el cual instanciaremos y entrenaremos nuestro modelo y otro que ser谩 en el que debemos aplicarlo. Antes de todo esto, debemos realizar un EDA para corregir imperfecciones como diferencias en el tipo de los datos, valores nulos, duplicados, etc.

## Objetivos: 

+ Entrenamiento y predicci贸n utilizando un Modelo de Machine Learning adecuado al problema (clasificaci贸n o regresi贸n).

+ An谩lisis exploratorio de los datos (EDA).

+ Divisi贸n de dataset en train y test utilizando train_test_split, CV, KFold o similares.

+ Utilizaci贸n de Pipelines en la producci贸n del modelo.

+ Comentarios y redacci贸n con la fundamentaci贸n de la soluci贸n propuesta, escrita en Markdown en el Jupyter Notebook (.ipynb) o bien en un documento aparte.

## Explicaci贸n del modelo:

Si bien este apartado se encuentra detallado paso a paso en el archivo `EDA_FeatureEng.ipynb`, a modo de resumen comento c贸mo encar茅 este problema. Luego de realizar un peque帽o an谩lisis de mis datos y algunas conversiones, como por ejemplo, utilizar LabelEncoder para convertir mis variables categ贸ricas, decid铆 probar dos tipos de modelos de clasificaci贸n: Regresi贸n Log铆stica y 脕rbol de decisi贸n. Hice un test utilizando un 脕rbol porque es el modelo con el que m谩s familiarizado me encuentro, sin embargo, compar茅 ambos para verificar cu谩l de estos ten铆a una mejor accuracy. Adem谩s, a la hora de hacer el 谩rbol utilic茅 la validaci贸n cruzada para sacar la profundidad 贸ptima de mi 谩rbol. Luego de hacer la selecci贸n de Features utilizando Chi虏, determin茅 las features 贸ptimas para entrenar mi modelo, ajust茅 mis hiperpar谩metros y obtuve resultados positivos.

## Aclaraciones:

Hay algunas cosas a tener en cuenta, el an谩lisis y modelo propuestos NO son necesariamente los m谩s 贸ptimos/mejores, varias decisiones fueron tomadas a mi propio criterio, por ejemplo, la profundidad del 谩rbol, el uso del estad铆stico Chi虏 (como se comenta en el Notebook) para la selecci贸n de features en lugar de la correlaci贸n de Pearson, descarte de columnas que personalmente cre铆a innecesarias (Como 'patientid' y 'Visitors with Patient'), etc...

## Explicaci贸n de los contenidos del Repositorio:

+ En la carpeta `datasets` se encuentran los datasets analizados, el archivo `hospitalizaciones_train.csv` que es el que utilizamos para instanciar y entrenar el modelo y el archivo `hospitalizaciones_test.csv` que es al que se le aplica el modelo ya terminado para sacar deducciones.

+ En el notebook `EDA_FeatureEng.ipynb` se encuentra el c贸digo comentado paso por paso, explicando las decisiones tomadas a la hora de encarar este proyecto;
    Esto se hizo as铆 para tener dividido de manera ordenada los bloques de c贸digo, separados por los markdowns que van dividiendo las etapas del proceso.
    Con esto espero documentar y demostrar cada paso del desarrollo.

+ En el archivo `DecisionTree_model.pkl` se encuentra el modelo de 谩rbol de decisi贸n creado, importado con la librer铆a de Joblib.

+ En el archivo `pred_generator.py` se encuentra el c贸digo que se encarga de realizar las transformaciones necesarias sobre el dataset `hospitalizaciones_test.csv` adem谩s de aplicarle el modelo, sacar las conclusiones y generar el archivo `Emmafer.csv` donde se encuentra mi columna de predicciones.

## Herramientas/librer铆as utilizadas:

+ Python. 馃悕

+ Pandas. 馃惣

+ Numpy. 馃摕

+ Mathplotlib. 馃搳

+ ScikitLearn. 馃

+ Joblib. 馃搧

## Espero haberme sabido explicar y que les haya gustado! Gracias por leer a este nerd 馃.

<p align="center">
<img src="https://media.tenor.com/e-tu1KPkCucAAAAC/the-simpsons-homer-simpson.gif"   
>
</p>
