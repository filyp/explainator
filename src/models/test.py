import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

SIZE = 224
hub_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/4"
embed = hub.KerasLayer(hub_url)
model = tf.keras.Sequential([
    embed
])

model.build([None, SIZE, SIZE, 3])  # Batch input shape.
model.summary()

file_path = '/Users/Anna/Explainator/explainator/data/panda.jpg'

img = tf.io.read_file(file_path)
img = tf.image.decode_jpeg(img)

images = tf.expand_dims(img, 0)
images = tf.cast(images, tf.float32) / 128.
images.set_shape((None, None, None, 3))
test_image = tf.image.resize(images, (SIZE, SIZE))


predictions = model.predict(test_image)

pred = np.argmax(predictions[0])

print(pred)