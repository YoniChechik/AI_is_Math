#%%
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 
#%% [markdown]
# from: https://www.tensorflow.org/tutorials/keras/classification
#%%
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#%%
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#%%
model.fit(x_train, y_train, epochs=5)
#%%
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

#%%
predictions = model.predict(x_test)

thisplot = plt.bar(range(10), predictions[0], color="#777777")
plt.ylim([0, 1])
predicted_label = np.argmax(predictions[0])

thisplot[predicted_label].set_color('red')
thisplot[y_test[0]].set_color('blue')
#%%
plt.figure()
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title('gt= '+str(y_test[0])+"; prediction= "+str(np.argmax(predictions[0])))

#%%
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array, true_label[i], img[i]
#   plt.grid(False)
#   plt.xticks([])
#   plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)



def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.xticks(range(10))
  thisplot = plt.bar(range(10), predictions_array)
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(10,10))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], y_test, x_test)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], y_test)
plt.tight_layout()
plt.show()

#%%
