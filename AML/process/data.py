import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 

df = pd.DataFrame()

def get_cols(path):
    df = pd.read_csv(path)
    cols = list(df.columns.values)
    print(cols)
    return cols

def train_test_split(df, label):
    Features = df.loc[:, df.columns != label]
    labels =  df.loc[:, label]
    X_train, X_test, y_train, y_test = train_test_split(Features,
                                                        labels,
                                                        test_size=0.2,
                                                       random_state = 5)
    return (X_train, X_test, y_train, y_test)

def regressor(label):
    models = []
    metrix = []
    train_accuracy = []
    test_accuracy = []
    models.append(('LinearRegression', LinearRegression()))
    #models.append(('DecisionTreeRegressor', DecisionTreeRegressor()))
    #models.append(('RandomForestRegressor', RandomForestRegressor()))
    #models.append(('BaggingRegressor', BaggingRegressor()))
    #models.append(('GradientBoostingRegressor', GradientBoostingRegressor()))
    #models.append(('AdaBoostRegressor', AdaBoostRegressor()))
    #models.append(('SVR', SVR()))
    #models.append(('KNeighborsRegressor', KNeighborsRegressor()))
    for name, model in models:
            m = model
            m.fit(X_train, y_train)
            y_pred = m.predict(X_test)
            r_square = r2_score(y_test,y_pred)
            rmse = np.sqrt(mean_squared_error(y_test,y_pred))
            #print(name," ( r_square , rmse) is: ", r_square, rmse)
            metrix.append((name, r_square, rmse))
    return metrix

def classifier():
    models = []
    metrix = []
    c_report = []
    train_accuracy = []
    test_accuracy = []
    models.append(('LogisticRegression', LogisticRegression(solver='liblinear', multi_class='ovr')))
    #models.append(('LinearDiscriminantAnalysis', LinearDiscriminantAnalysis()))
    #models.append(('KNeighborsClassifier', KNeighborsClassifier()))
    #models.append(('DecisionTreeClassifier', DecisionTreeClassifier()))
    #models.append(('GaussianNB', GaussianNB()))
    #models.append(('RandomForestClassifier', RandomForestClassifier(n_estimators=100)))
    #models.append(('SVM', SVC(gamma='auto')))
    #models.append(('Linear_SVM', LinearSVC()))
    #models.append(('XGB', XGBClassifier()))
    #models.append(('SGD', SGDClassifier()))
    #models.append(('Perceptron', Perceptron()))
    for name, model in models:
            m = model
            m.fit(X_train, y_train)
            y_pred = m.predict(X_test)
            train_acc = round(m.score(X_train, y_train) * 100, 2)
            test_acc = metrics.accuracy_score(y_test,y_pred) *100
            c_report.append(classification_report(y_test, y_pred))
            #print(name," (train accuracy , test_accuracy) is: ", train_acc, test_acc)
            metrix.append([name, train_acc, test_acc])
    return metrix
