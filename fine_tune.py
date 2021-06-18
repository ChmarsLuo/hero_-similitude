import keras
from keras.layers import (Input,
                          Activation,
                          Dropout,
                          BatchNormalization,
                          Conv2D,
                          Flatten,
                          Dense,
                          )
from keras.applications.inception_v3 import InceptionV3
from keras.models import Model










def create_model(input_shape = (512,512,3),num_classes=2):

    input = Input(shape=input_shape)
    base_model = InceptionV3(weights='imagenet',
                             input_shape=input_shape)
    bn = BatchNormalization()(input)
    x = base_model()(bn)
    x = Conv2D(32,kernel_size=(1,1),activation='relu')(x)
    x = Flatten()(x)
    x = Dropout(0.5)(x)
    x = Dense(1024,activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(num_classes,activation='sigmoid')(x)

    model = Model(input_shape,x)

    return model

model = create_model()
for layer in model.layers:
    layer.trainable = False
model.layers[-1].trainable = True
model.layers[-2].trainable = True
model.layers[-3].trainable = True
model.layers[-4].trainable = True
model.layers[-5].trainable = True













