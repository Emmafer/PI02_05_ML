import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import joblib

df_test = pd.read_csv('datasets\\hospitalizaciones_test.csv', delimiter=',', encoding="utf-8")
df_test = df_test.drop(columns=['patientid','Visitors with Patient'])
le = preprocessing.LabelEncoder()
le.fit(df_test.Department)
df_test.Department = le.transform(df_test.Department)
le.fit(df_test.Ward_Facility_Code)
df_test.Ward_Facility_Code = le.transform(df_test.Ward_Facility_Code)
le.fit(df_test.doctor_name)
df_test.doctor_name = le.transform(df_test.doctor_name)
le.fit(df_test.Age)
df_test.Age = le.transform(df_test.Age)
le.fit(df_test.gender)
df_test.gender = le.transform(df_test.gender)
le.fit(df_test['Type of Admission'])
df_test['Type of Admission'] = le.transform(df_test['Type of Admission'])
le.fit(df_test['Severity of Illness'])
df_test['Severity of Illness'] = le.transform(df_test['Severity of Illness'])
le.fit(df_test.health_conditions)
df_test.health_conditions = le.transform(df_test.health_conditions)
le.fit(df_test.Insurance)
df_test.Insurance = le.transform(df_test.Insurance)
DecisionTree_model = joblib.load('DecisionTree_model.pkl')
X_test = df_test[['staff_available','Severity of Illness','Available Extra Rooms in Hospital','Department','Ward_Facility_Code','doctor_name','Age','gender','Admission_Deposit']]
pred = DecisionTree_model.predict(X_test)
df_test['pred'] = pred
df_test = df_test['pred']
df_test.to_csv('Emmafer.csv', index=False)