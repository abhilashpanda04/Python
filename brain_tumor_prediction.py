import os
PATH = os.getcwd()

PATH

DATA_PATH = os.path.join(PATH, 'brain')
data_dir_list = os.listdir(DATA_PATH)

print(data_dir_list)

mg_rows=224
img_cols=224
num_channel=3

num_epoch=10
batch_size=32

img_data_list=[]
classes_names_list=[]

import cv2

for dataset in data_dir_list:
    classes_names_list.append(dataset)
    print ('Loading images from {} folder\n'.format(dataset))
    img_list=os.listdir(DATA_PATH+'/'+ dataset)
    for img in img_list:
        input_img=cv2.imread(DATA_PATH + '/'+ dataset + '/'+ img)
        input_img_resize=cv2.resize(input_img,(img_rows, img_cols))
        img_data_list.append(input_img_resize)

classes_names_list

num_classes=len(classes_names_list)

num_classes

import numpy as np
img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255

print (img_data.shape)

num_of_samples = img_data.shape[0]
input_shape = img_data[0].shape

input_shape

classes = np.ones((num_of_samples,), dtype='int64')

classes[0:97]=0
classes[156:253]=1


from keras.utils import to_categorical
classes = to_categorical(classes, num_classes)

from sklearn.utils import shuffle

X, Y = shuffle(img_data, classes, random_state=2)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

y_test.shape


from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D


model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(Conv2D(32, (3, 3), activation='relu')) is one way to modify the ResNet for semantic segmentation. There are several modifications, but the one most relevant to our purposes is the modification to be an encoder-decoder with skip connections (akin to the U-Net). This is done by making the ResNet into the encoder and adding additional upsampling layers to form the decoder. Skip connections use features from intermediate layers of the ResNet and concatenate them to intermediate features in the decoder. See Fig. 2 for a block diagram o
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=["accuracy"])
 is one way to modify the ResNet for semantic segmentation. There are several modifications, but the one most relevant to our purposes is the modification to be an encoder-decoder with skip connections (akin to the U-Net). This is done by making the ResNet into the encoder and adding additional upsampling layers to form the decoder. Skip connections use features from intermediate layers of the ResNet and concatenate them to intermediate features in the decoder. See Fig. 2 for a block diagram o
model.summary()
model.layers
model.weights
model.layers[0].get_weights()

hist = model.fit(X_train, y_train, batch_size=batch_size, epochs=num_epoch, verbose=1, validation_data=(X_test, y_test))

score = model.evaluate(X_test, y_test, batch_size=batch_size)

print('Test Loss:', score[0])
print('Test Accuracy:', score[1])

Y_train_pred = model.predict(X_test)

y_train_pred = np.argmax(Y_train_pred, axis=1)
print(y_train_pred)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(np.argmax(y_test, axis=1), y_train_pred))




from keras.layers import Input, Dense

image_input = Input(shape=(img_rows, img_cols, num_channel))

image_input

from keras.applications.vgg16 import VGG16

model = VGG16(input_tensor=image_input, include_top=True, weights='imagenet')

model.summary()

last_layer = model.get_layer('fc2').output
out = Dense(num_classes, activation='softmax', name='output')(last_layer)

from keras.models import Model

custom_vgg_model = Model(image_input, out)
custom_vgg_model.summary()

for layer in custom_vgg_model.layers[:-1]:
    layer.trainable = False

custom_vgg_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

custom_vgg_model.fit(X_train, y_train, batch_size=batch_size, epochs=num_epoch, verbose=1, validation_data=(X_test, y_test))
(loss, accuracy) = custom_vgg_model.evaluate(X_test, y_test, batch_size=batch_size, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,accuracy * 100))

Y_train_pred = custom_vgg_model.predict(X_test)

y_train_pred = np.argmax(Y_train_pred, axis=1)
print(y_train_pred)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(np.argmax(y_test, axis=1), y_train_pred))
