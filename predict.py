# Importing the libraries
import pandas as pd
import numpy as np



# Importing the dataset
dataset = pd.read_csv('train.csv')
X = dataset.iloc[:,[0,1,2,3,4,5,7,8,9]].values
y = dataset.iloc[:, 10].values
#Categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X=LabelEncoder()

X[:,5]=labelencoder_X.fit_transform(X[:,5])
X[:,6]=labelencoder_X.fit_transform(X[:,6])
ct=ColumnTransformer([('encoder' ,OneHotEncoder(),[5,6])],remainder='passthrough')
X=np.array(ct.fit_transform(X),dtype=np.float)



#Fitting the Classifier
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=6,metric='minkowski',p=2)
classifier.fit(X,y)

#Predicting the Test set results
datatest=pd.read_csv('test.csv')
X_t= datatest.iloc[:,[0,1,2,3,4,5,7,8,9]].values
y_t = datatest.iloc[:, 10].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X_t=LabelEncoder()
X_t2=datatest.iloc[:,0]
X_t[:,5]=labelencoder_X_t.fit_transform(X_t[:,5])
X_t[:,6]=labelencoder_X_t.fit_transform(X_t[:,6])
ct1=ColumnTransformer([('encoder' ,OneHotEncoder(),[5,6])],remainder='passthrough')
X_t=np.array(ct1.fit_transform(X_t),dtype=np.float)


y_pred=classifier.predict(X_t)
#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_t,y_pred)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_t,y_pred)*100
q=pd.DataFrame({'Team_name':X_t2,'Team_rating':y_pred})