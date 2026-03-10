
import tensorflow as tf

class RankingModel(tf.keras.Model):

    def __init__(self):
        super().__init__()

        self.layers_model = tf.keras.Sequential([
            tf.keras.layers.Dense(64,activation="relu"),
            tf.keras.layers.Dense(32,activation="relu"),
            tf.keras.layers.Dense(1)
        ])

    def call(self,inputs):
        return self.layers_model(inputs)
