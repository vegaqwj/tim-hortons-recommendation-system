
import pandas as pd
import tensorflow as tf
from models.two_tower import TwoTowerModel

orders = pd.read_csv("data/orders.csv")

dataset = tf.data.Dataset.from_tensor_slices({
"user_id":orders["user_id"].astype(str),
"product_id":orders["product_id"].astype(str)
})

dataset = dataset.shuffle(1000).batch(32)

user_ids = orders["user_id"].astype(str).unique()
product_ids = orders["product_id"].astype(str).unique()

model = TwoTowerModel(user_ids,product_ids)

model.compile(optimizer=tf.keras.optimizers.Adagrad(0.1))

model.fit(dataset,epochs=5)

model.save("retrieval_model")
