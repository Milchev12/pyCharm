import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle

from matplotlib import style




data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1","G2","G3","studytime","failures","absences"]]


predict = "G3"

X = np.array(data.drop([predict],1 ))
Y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
'''
best= 0
for _ in range(30):
    x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)


    linear = linear_model.LinearRegression()

    linear.fit(x_train,y_train)

    acc= linear.score(x_test,y_test)

    print(acc)
    if acc>best:
        best= acc
        with open("Studentmode.pickle","wb")as f:
            pickle.dump(linear,f)
            

print("The best: ", best)
'''
pickle_in = open("Studentmode.pickle","rb")

linear = pickle.load(pickle_in)




#print('Coefficient: \n',linear.coef_)
#print('Interecept: \n',linear.intercept_) #Interecept - nachalnata tochka na regresiqta

predictions = linear.predict(x_test)

for x in range(len(predictions)):
        print(predictions[x],y_test[x],y_test[x])

p = 'studytime'
style.use("ggplot")
pyplot.scatter(data[p],data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()