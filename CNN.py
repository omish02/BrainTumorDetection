# Convolutional Neural Network

# Part 1 - Building the CNN
# Importing the keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialising the CNN
classifier=Sequential()
#Step 1-Convolution
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu'))
#Step 2-Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))
#Adding a second convolutional layer
classifier.add(Convolution2D(32,3,3,activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
#Step 3- Flattening
classifier.add(Flatten())
#Step 4-Full Connection
classifier.add(Dense(units=128,activation='relu'))
classifier.add(Dense(units=1,activation='sigmoid'))


# Part 3 - Training the CNN
# Compiling the CNN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#Fitting the CNN to images
from keras.preprocessing.image import ImageDataGenerator
# Generating images for the Training set
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
# Generating images for the Test set
test_datagen = ImageDataGenerator(rescale = 1./255)
# Creating the Training set
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
# Creating the Test set
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')
classifier.fit_generator(training_set,
                         samples_per_epoch=8000,
                         nb_epoch=25,
                         validation_data=test_set,
                         nb_val_samples=2000)
#4. Making new prediction
import numpy as np
from keras.preprocessing import image
test_image=image.load_image('samples.png',target_size=(160,160))
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=classifier.predict(test_image)
if(result[0][0]==1):
    print("Yes")
else:
    print("NO")
