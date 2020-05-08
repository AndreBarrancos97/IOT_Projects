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


print(sales_data.head(n=2))
print(sales_data.tail(n=2))
print(sales_data.dtypes)

#**************************Gráfico de Barras*********
#sns.set(style="whitegrid", color_codes=True)
#sns.set(rc={'figure.figsize':(11.7,8.27)})
#Comentario - create a countplot
#sns.countplot('Route To Market',data=sales_data,hue = 'Opportunity Result')
#Comentario - Remove the top and down margin
#sns.despine(offset=10, trim=True)
#sns.violinplot(x="Opportunity  Result",y="Client Size By Revenue", hue="Opportunity Result", data=sales_data)
#plt.show()


#************************Violinplt********************
#Comentario - setting the plot size for all plots
#sns.set(rc={'figure.figsize':(16.7,13.27)})
#Comentario - plotting the violinplot
#sns.violinplot(x="Opportunity Result",y="Client Size By Revenue", hue="Opportunity Result", data=sales_data)
#plt.show()

#***********Convert Strings to numbers example***************
#Comentario - AI doesn't like strings so we convert to numbers
#from sklearn import preprocessing
#Comentario - create the Labelencoder object
#le = preprocessing.LabelEncoder()
#encoded_value = le.fit_transform(["paris","paris","tokyo","amsterdam"])
#print(encoded_value)

#*******************Convert Strings to numbers exercise************************************
#Comentario - .unique() corre a coluna toda e mostra as diferentes opções dentro da coluna
#print("Supplies Subgroup' : ",sales_data['Supplies Subgroup'].unique())
#print("Region : ",sales_data['Region'].unique())
#print("Route To Market : ",sales_data['Route To Market'].unique())
#print("Opportunity Result : ",sales_data['Opportunity Result'].unique())
#print("Competitor Type : ",sales_data['Competitor Type'].unique())
#print("'Supplies Group : ",sales_data['Supplies Group'].unique())

from sklearn import preprocessing
#Comentario - create the Labelencoder object
le = preprocessing.LabelEncoder()
sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])
#Comentario - display the initial records
print(sales_data.head())
#Comentario - Save Data modified to CSV
#sales_data.to_csv(working_directory + '/Saved_Data.csv', index = False)

#********************************************************************************************

#Comentario - Escolher outras colunas que não são 'Opportunity Number','Opportunity Result
cols = [col for col in sales_data.columns if col not in ['Opportunity Number','Opportunity Result']]

data = sales_data[cols]
#Comentario - assigning the Oppurtunity Result column as target
target = sales_data['Opportunity Result']
print(data.head(n=2))

#Comentario - Nós creamos prever o Oppurtunity Result e por isso temos de tirar dos dados
#Comentario - Normalmente guarda-se 80% para treinar e os outros 20% para teste
#Comentario - Mas agora vai se usar 70% (Trainning data) e 30%(Test Data)

from sklearn.model_selection import train_test_split
#Comentario - split data into train and test
data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.30, random_state = 10)
#Comentario - 'random_state’ just ensures that we get reproducible results every time

#Comentario - Escolher algoritmo através do sketch do pdf pág 21
#Comentario - Pelo diagrama podemos escolher os alg: Naive Bayes, Linear SVC e K-Neighbours Classifier

#*****************************Algoritmo Gaussian Naive Bayes********************************************
#Comentario - import the necessary module
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
#Comentario - create an object of the type GaussianNB
gnb = GaussianNB()
#Comentario - train the algorithm on training data and predict using the testing data
pred = gnb.fit(data_train, target_train).predict(data_test)
print(pred.tolist())
#Comentario - print the accuracy score of the model
print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred, normalize = True))


from yellowbrick.classifier import ClassificationReport
# Instantiate the classification model and visualizer
visualizer = ClassificationReport(gnb, classes=['Won','Loss'])
visualizer.fit(data_train, target_train) # Fit the training data to the visualizer
visualizer.score(data_test, target_test) # Evaluate the model on the test data
g = visualizer.poof() # Draw/show/poof the data

#**************************************Algoritmo Linear SVC********************************************
#Comentario - import the necessary modules
#from sklearn.svm import LinearSVC
#from sklearn.metrics import accuracy_score
#Comentario - create an object of type LinearSVC
#svc_model = LinearSVC(random_state=0)
#Comentario - train the algorithm on training data and predict using the testing data
#pred = svc_model.fit(data_train, target_train).predict(data_test)
#Comentario - print the accuracy score of the model
#print("LinearSVC accuracy : ",accuracy_score(target_test, pred, normalize = True))

#**************************************Algoritmo K-Neighbours Classifier********************************************
#Comentario - import necessary modules
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.metrics import accuracy_score
#Comentario - create object of the lassifier
#neigh = KNeighborsClassifier(n_neighbors=3)
#Comentario - Train the algorithm
#neigh.fit(data_train, target_train)
#Comentario - predict the response
#pred = neigh.predict(data_test)
#Comentario - evaluate accuracy
#print("KNeighbors accuracy score : ",accuracy_score(target_test, pred))