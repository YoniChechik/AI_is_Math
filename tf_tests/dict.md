# topics

- [datasets](#datasets)
  - [how to split to batches](#how-to-split-to-batches)
- [layers](#layers)
- [training](#training)
  - [optimizers](#optimizers)
  - [loss](#loss)
  - [advanced](#advanced)
- [evaluate and predict](#evaluate-and-predict)
- [tensorboard](#tensorboard)


## datasets
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

- split to train, validate, test
- data augmentation
- tf hub (also for transfer learning):
  
        embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
        hub_layer = hub.KerasLayer(embedding, input_shape=[], 
                                dtype=tf.string, trainable=True)
        hub_layer(train_examples_batch[:3])
- tfds: https://www.tensorflow.org/datasets/overview 
  basically tfds is another pip install that we can use to build td.dataset - not rellevent...
### how to split to batches

- can be defined in tf.dataset
## layers
- layers types: dense, conv2d, dropout, flatten, activation (relu, softmax)
- advanced layers: lstm, rnn

## training
- using keras.sequantial or keras api for harder stuff
    model.summary()

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

- checkpoints:
    https://www.tensorflow.org/tutorials/keras/save_and_load#save_checkpoints_during_training
- 
### optimizers
- adam
-  sgd

### loss 
sparse_categorical_crossentropy...

### advanced
`tf.GradientTape()`

https://www.tensorflow.org/tutorials/quickstart/advanced


## evaluate and predict


    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

    print('\nTest accuracy:', test_acc)

    predictions = model.predict(test_images)

## tensorboard