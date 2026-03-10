
import tensorflow as tf
import tensorflow_recommenders as tfrs

class UserModel(tf.keras.Model):
    def __init__(self, user_ids):
        super().__init__()
        self.embedding = tf.keras.Sequential([
            tf.keras.layers.StringLookup(vocabulary=user_ids, mask_token=None),
            tf.keras.layers.Embedding(len(user_ids)+1, 32)
        ])

    def call(self, inputs):
        return self.embedding(inputs)


class ProductModel(tf.keras.Model):
    def __init__(self, product_ids):
        super().__init__()
        self.embedding = tf.keras.Sequential([
            tf.keras.layers.StringLookup(vocabulary=product_ids, mask_token=None),
            tf.keras.layers.Embedding(len(product_ids)+1, 32)
        ])

    def call(self, inputs):
        return self.embedding(inputs)


class TwoTowerModel(tfrs.Model):

    def __init__(self, user_ids, product_ids):
        super().__init__()

        self.user_model = UserModel(user_ids)
        self.product_model = ProductModel(product_ids)

        self.task = tfrs.tasks.Retrieval(
            metrics=tfrs.metrics.FactorizedTopK(
                candidates=tf.data.Dataset.from_tensor_slices(product_ids)
                .batch(128)
                .map(self.product_model)
            )
        )

    def compute_loss(self, features, training=False):
        user_embeddings = self.user_model(features["user_id"])
        product_embeddings = self.product_model(features["product_id"])
        return self.task(user_embeddings, product_embeddings)
