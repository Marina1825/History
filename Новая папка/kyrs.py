import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
%matplotlib inline
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
y_train = y_train / 255

y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

plt.figure(figsize=(10,5))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    
plt.show()

madel = keras.Sequential([
    Flaten(input_shape=(28,28,1))
    Dense(128, activation='relu')
    Dense(10, activation='softmax')
])

print(model.sumary())

model.comile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fix(x_train, y_train_cat, batch_size=32, epochs=1, validation_split=0.2)

model.eveluate(x_test, y_test_cat)

n=0
x = np.expand_dims(x_test[n], axis=0)
res = model.predict(x)
print(res)
print(f"Распозноная цифра: {np.argmax(res)}")

plt.imshow(x_test[n], cmap=plt.cm.binari)
plt.show()

pred = model.predict(x_test)
pred = np.argmax(pred, axis=1)
print(pred.shape)

print(pred[:20])
print(y_test[:20])

mask = pred == y_test
print(mask[:10])

x_false = x_test[~mask]
y_false = x_test[~mask]

print(x_false.shape)

for i in range(5):
    print("Значение сети: "+str(y_test[i]))
    plt.imshow(x_false[i], cmap=plt.cm.binary)
    plt.show


