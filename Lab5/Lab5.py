import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import datetime as dt
import seaborn as sns
from itertools import filterfalse


#Comentario - Look to the path of your current working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
#************************************Exercise 1************************************************
x = []
y = []

sales_data = pd.read_csv(working_directory + '/WA_Fn-UseC_-Sales-Win-Loss.csv', delimiter=',')

from sklearn import preprocessing
#Comentario - create the Labelencoder object
le = preprocessing.LabelEncoder()
sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])

print(sales_data.head())


#Comentario - Escolher outras colunas que não são 'Falha'
cols = [col for col in sales_data.columns if col not in ['Opportunity Number','Opportunity Result']]

data = sales_data[cols]
#Comentario - assigning the Falha column as target
target = sales_data['Opportunity Result']
print(data.head(n=2))

#Comentario - Nós queremos prever o Oppurtunity Result e por isso temos de tirar dos dados
#Comentario - Normalmente guarda-se 80% para treinar e os outros 20% para teste


from sklearn.model_selection import train_test_split
#Comentario - split data into train and test
data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.30, random_state = 10)
#Comentario - 'random_state’ just ensures that we get reproducible results every time
data_validation, data_test, target_validation, target_test = train_test_split(data_test,target_train, test_size = 0.50, random_state = 10)
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(17,17), activation='relu', solver='adam', max_iter=500)
mlp.fit(data_train,target_train)

predict_train = mlp.predict(data_train)
predict_test = mlp.predict(data_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(target_train,predict_train))
print(classification_report(target_train,predict_train))

print(confusion_matrix(target_test,predict_test))
print(classification_report(target_test,predict_test))