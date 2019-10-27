import tensorflow as tf
import tensorflow_hub as hub


hub_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_035_128/classification/4"
embed = hub.KerasLayer(hub_url)
model = tf.keras.Sequential([
    embed
])

model.build([None, 128, 128, 3])  # Batch input shape.
model.summary()
