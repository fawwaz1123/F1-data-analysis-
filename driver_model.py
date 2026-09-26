from sklearn import linear_model
def driver_model(X,y):
  model = linear_model.LinearRegression()
  model.fit(X,y)

  return model