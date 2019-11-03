import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

SIZE = 224
CLASSES_PATH = '/Users/Anna/Explainator/explainator/src/models/imagenet_classes.txt'
TEST_IMAGE_PATH = '/Users/Anna/Explainator/explainator/data/panda.jpg'


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
classes = [line.rstrip('\n') for line in open(CLASSES_PATH)]


# read test image and vectorize it
img = tf.io.read_file(TEST_IMAGE_PATH)
img = tf.image.decode_jpeg(img)

img = tf.expand_dims(img, 0)
img = tf.cast(img, tf.float32) / 128.
img.set_shape((None, None, None, 3))
test_image = tf.image.resize(img, (SIZE, SIZE))

# get model predictions on image
predictions = model.predict(test_image)
class_index = np.argmax(predictions[0])

image_class = classes[class_index]

print('Predicted class: {}. Score: {} in score range: ({} , {})'.format(image_class, np.max(predictions[0]), np.min(predictions[0]), np.max(predictions[0])))
# print(class_index)
