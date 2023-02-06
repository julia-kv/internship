import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def read_data():
    X_train, Y_train = [], []

    for _ in range(5):
        data = [float(x) for x in input().split("\t")]
        X_train.append(data[:5])
        Y_train.append(data[-1:])

    X_test = []
    for _ in range(5):
        data = [float(x) for x in input().split("\t")]
        X_test.append(data)

    X = np.array(X_train)
    X_test = np.array(X_test)
    y = np.array(Y_train)

    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(X)
    X_poly_test = poly_reg.transform(X_test)


    regr = LinearRegression()
    regr.fit(X_poly, y)

    y_test = regr.predict(X_poly_test)

    for i in y_test:
        print(str(i[0]))

