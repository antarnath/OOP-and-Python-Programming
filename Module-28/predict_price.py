import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
# print(data)
model = LinearRegression()
model.fit(data[['version']], data[['price']])
predicted_price = model.predict([[48]])
print(predicted_price)