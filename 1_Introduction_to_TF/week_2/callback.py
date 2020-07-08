import tensorflow as tf
from tensorflow import keras

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.4):
            print("\nLoss is low so cancelling training")
            self.model.stop_training = True

callbakcs = myCallback()


#  Construct the model

model.fit(training_images, training_labels, epochs=15, callbacks=[callbacks])
