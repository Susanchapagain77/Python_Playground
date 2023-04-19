import pandas as pd
from sklearn.tree import DecisionTreeClassifier


marriage_data=pd.read_csv('marriage.csv')
marriage_data
X=marriage_data.drop(columns=['Nation'])
Y=marriage_data['Nation']

model=DecisionTreeClassifier()
model.fit(X,Y)
predictions=model.predict([[10,13],[11,11],[17,17],[1,21]])
predictions





