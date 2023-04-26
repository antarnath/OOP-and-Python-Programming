from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

digits = load_digits()
# print(digits.data.shape)
# plt.gray()
# plt.matshow(digits.images[])
# plt.show()
# print(dir(digits))
# print(digits.data[0])
# print(dir(digits))
X = digits.data
Y = digits.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)

Model = LogisticRegression()
Model.fit(X_train, Y_train)

# print(digits.target[1700])
# result = Model.predict([digits.data[1700]])
# print('test result', result)

accuracy = Model.score(X_test, Y_test)
# print(accuracy)

Y_predicted = Model.predict(X_test)
confusion = confusion_matrix(Y_test, Y_predicted)
# print(confusion)
plot_confusion_matrix(Model, X_test, Y_test)
plt.show()
