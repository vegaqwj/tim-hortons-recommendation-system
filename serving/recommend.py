
import tensorflow as tf

model = tf.keras.models.load_model("retrieval_model")

def recommend(user_id):
    user = tf.constant([str(user_id)])
    scores, products = model(user)
    return products[:5]
