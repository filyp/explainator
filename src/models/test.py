import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

SIZE = 224
CLASSES_FILENAME = '/Users/Anna/Explainator/explainator/data/classes.txt'

# download construct model
hub_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/4"
embed = hub.KerasLayer(hub_url)
model = tf.keras.Sequential([
    embed
])

# build model
model.build([None, SIZE, SIZE, 3])  # Batch input shape.
model.summary()

# read classes
classes = [line.rstrip('\n') for line in open(CLASSES_FILENAME)]


# read test image and vectorize it
file_path = '/Users/Anna/Explainator/explainator/data/panda.jpg'

img = tf.io.read_file(file_path)
img = tf.image.decode_jpeg(img)

images = tf.expand_dims(img, 0)
images = tf.cast(images, tf.float32) / 128.
images.set_shape((None, None, None, 3))
test_image = tf.image.resize(images, (SIZE, SIZE))

# get model predictions on image
predictions = model.predict(test_image)
class_index = np.argmax(predictions[0])

image_class = classes[class_index]

print('Predicted class: {}. Score: {} '.format(image_class, np.max(predictions[0])))

