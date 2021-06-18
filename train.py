import os
from keras.callbacks import (EarlyStopping,
                             ModelCheckpoint,
                             ReduceLROnPlateau,
                             TensorBoard,
                             CSVLogger)
from keras.optimizers import SGD, Adam

from nets.siamese import siamese
from nets.siamese_training import Generator
from nets.siamese_training_own_dataset import \
    Generator as Generator_own_dataset


def get_image_num(path, train_own_data):
    num = 0
    if train_own_data:
        train_path = os.path.join(path, 'hero_new')
        for character in os.listdir(train_path):
            character_path = os.path.join(train_path, character)
            num += len(os.listdir(character_path))
    else:
        train_path = os.path.join(path, 'cdk')
        for alphabet in os.listdir(train_path):
            alphabet_path = os.path.join(train_path, alphabet)
            for character in os.listdir(alphabet_path):
                character_path = os.path.join(alphabet_path, character)
                num += len(os.listdir(character_path))
    return num

if __name__ == "__main__":
    dataset_path = "datasets"


    log_dir = "logs/hero_log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


    input_shape = [350,160,3]

    freeze_layers = 19


    train_own_data = True

    model = siamese(input_shape)


    model_path = "model_data/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5"
    model.load_weights(model_path, by_name=True, skip_mismatch=True)
    


    tensorboard = TensorBoard(log_dir=log_dir)
    checkpoint_period = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
                                        monitor='val_loss',
                                        save_weights_only=True,
                                        save_best_only=True,
                                        period=1)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                                  factor=0.1,
                                  patience=5,
                                  verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss',
                                   min_delta=0,
                                   patience=20,
                                   verbose=1)
    csvlogger = CSVLogger('./hero_train.csv',append=True)


    train_ratio = 0.9
    images_num = get_image_num(dataset_path, train_own_data)
    train_num = int(images_num*0.9)
    val_num = int(images_num*0.1)

    # for layer in model.layers:
    #     layer[:] = False
    # for i in range(freeze_layers):
    #     model.layers[i].trainable = False


    if True:
        Batch_size = 8
        Lr = 1e-3
        Init_epoch = 0
        Freeze_epoch = 50

        model.compile(loss = "binary_crossentropy",
                      optimizer = Adam(lr=Lr),
                      metrics = ["binary_accuracy"])
        print('Train with batch size {}.'.format(Batch_size))

        if train_own_data:
            gen = Generator_own_dataset(input_shape, dataset_path, Batch_size, train_ratio)
        else:
            gen = Generator(input_shape, dataset_path, Batch_size, train_ratio)

        model.fit_generator(gen.generate(True),
                steps_per_epoch=max(1,train_num//Batch_size),
                validation_data=gen.generate(False),
                validation_steps=max(1,val_num//Batch_size),
                epochs=Freeze_epoch,
                initial_epoch=Init_epoch,
                callbacks=[checkpoint_period, reduce_lr, early_stopping, tensorboard,csvlogger])

    # for i in range(freeze_layers):
    #     model.layers[i].trainable = True

    if True:
        Batch_size = 16
        Lr = 1e-4
        Freeze_epoch = 50
        Epoch = 100
        
        model.compile(loss = "binary_crossentropy",
                      optimizer = Adam(lr=Lr),
                      metrics = ["binary_accuracy"])
        print('Train with batch size {}.'.format(Batch_size))

        if train_own_data:
            gen = Generator_own_dataset(input_shape, dataset_path, Batch_size, train_ratio)
        else:
            gen = Generator(input_shape, dataset_path, Batch_size, train_ratio)
            
        model.fit_generator(gen.generate(True),
                steps_per_epoch=max(1,train_num//Batch_size),
                validation_data=gen.generate(False),
                validation_steps=max(1,val_num//Batch_size),
                epochs=Epoch,
                initial_epoch=Freeze_epoch,
                callbacks=[checkpoint_period, reduce_lr, early_stopping, tensorboard,csvlogger])
