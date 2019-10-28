#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:47:40 2019

@author: sagihaider
"""

import os
import glob
import shutil
import itertools
from keras import models
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D


#%% Define parameters for looping
people = 1  # Change the number of subjects to work on
subjects = dict(enumerate([str(s).zfill(2) for s in range(1, people+1)]))
print(subjects)

#class_id = [1, 2, 3, 4]  # Class information
class_id = [1, 2]  # Class information
comb_class = [list(x) for x in itertools.combinations(class_id, 2)]  # All possible class-pairs
print(comb_class)


#%% Train Data copy into folders

for subject, band in enumerate(subjects):
    for row in comb_class:
        print(row)        
        train_class1_dir = "/Users/sagihaider/GitHub/CNN_HA/FeaturesIM_Sorted/A0" + str(subject+1) +  "/Train/class" + str(row[0])
        train_class2_dir = "/Users/sagihaider/GitHub/CNN_HA/FeaturesIM_Sorted/A0" + str(subject+1) + "/Train/class" + str(row[1])
        #test_class1_dir = "/Users/sagihaider/Features/EEG_2A/MI_Topo_Sorted/S" + str(subject+1) + "/whole_test_C" + str(row[0]) + str(row[1]) + "/class" + str(row[0])
        #test_class2_dir = "/Users/sagihaider/Features/EEG_2A/MI_Topo_Sorted/S" + str(subject+1) + "/whole_test_C" + str(row[0]) + str(row[1]) + "/class" + str(row[1])
        print('total train class 1 images before partition:', len(os.listdir(train_class1_dir)))
        print('total train class 2 images before partition:', len(os.listdir(train_class2_dir)))
        #print('total test class 1 images before partition:', len(os.listdir(test_class1_dir)))
        #print('total test class 2 images before partition:', len(os.listdir(test_class2_dir)))        
#        train_dir = "G:/Data/EEG/2A_Saugat/data/topofeatures/S" + str(subject+1) + "/whole_train_C"  + str(row[0]) + str(row[1]) + "/"
#        test_dir = "G:/Data/EEG/2A_Saugat/data/topofeatures/S" + str(subject+1) +  "/whole_test_C" + str(row[0]) + str(row[1]) + "/"
#        print(train_dir)
#        print(test_dir)
        
        destDirTrainCl1 = "/Users/sagihaider/GitHub/CNN_HA/temp_data/train/class" + str(row[0])
        destDirTrainCl2 = '/Users/sagihaider/GitHub/CNN_HA/temp_data/train/class' + str(row[1])
        destDirValCl1 = '/Users/sagihaider/GitHub/CNN_HA/temp_data/val/class' + str(row[0])
        destDirValCl2 = '/Users/sagihaider/GitHub/CNN_HA/temp_data/val/class' + str(row[1])
        
        shutil.rmtree(destDirTrainCl1[:-7], ignore_errors=True, onerror=None)
        os.makedirs(destDirTrainCl1) 
        os.makedirs(destDirTrainCl2) 
        
        shutil.rmtree(destDirValCl1[:-7], ignore_errors=True, onerror=None)
        os.makedirs(destDirValCl1) 
        os.makedirs(destDirValCl2) 
#        
        # Get the file names in both source directories
        filesClass1 = os.listdir(train_class1_dir)
        filesClass2 = os.listdir(train_class2_dir)

        # input the % of training data
        trainPercent = 75
        trainSetCl1 = int((len(filesClass1)*trainPercent)/100)
        trainSetCl2 = int((len(filesClass2)*trainPercent)/100)

        # split the filename Lists into train and test
        filesTrainSetCl1 = filesClass1[:trainSetCl1]
        filesValSetCl1 = filesClass1[trainSetCl1:]

        filesTrainSetCl2 = filesClass2[:trainSetCl2]
        filesValSetCl2 = filesClass2[trainSetCl2:]

        # Copy files to destimation folders for class1
        for f in filesTrainSetCl1:
            shutil.copy(train_class1_dir+'/'+f,destDirTrainCl1)

        for f in filesValSetCl1:
            shutil.copy(train_class1_dir+'/'+f,destDirValCl1) 
  
        # Copy files to destimation folders for class1
        for f in filesTrainSetCl2:
            shutil.copy(train_class2_dir+'/'+f,destDirTrainCl2)
  
        for f in filesValSetCl2:
            shutil.copy(train_class2_dir+'/'+f,destDirValCl2)
            
            
        train_dir_class1_AP = "/Users/sagihaider/GitHub/CNN_HA/temp_data/train/class" + str(row[0])
        train_dir_class2_AP = "/Users/sagihaider/GitHub/CNN_HA/temp_data/train/class" + str(row[1])
        val_dir_class1_AP = "/Users/sagihaider/GitHub/CNN_HA/temp_data/val/class" + str(row[0])
        val_dir_class2_AP = "/Users/sagihaider/GitHub/CNN_HA/temp_data/val/class" + str(row[1])

        print('total train class 1 images after partition:', len(os.listdir(train_dir_class1_AP)))
        print('total train class 2 images after partition:', len(os.listdir(train_dir_class2_AP)))
        print('total test class 1 images after partition:', len(os.listdir(val_dir_class1_AP)))
        print('total test class 2 images after partition:', len(os.listdir(val_dir_class2_AP))) 

        train_dir = "/Users/sagihaider/GitHub/CNN_HA/temp_data/train"
        val_dir = "/Users/sagihaider/GitHub/CNN_HA/temp_data/val"
        ################# Build Model #########################################    
#        model = models.Sequential()
#        model.add(layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(150, 150, 3)))
#        model.add(layers.MaxPooling2D((2, 2)))
#        model.add(layers.Conv2D(32, (3, 3), activation='relu'))
#        model.add(layers.MaxPooling2D((2, 2)))
#        model.add(layers.Flatten())
#        model.add(layers.Dense(128, activation='relu'))
#        model.add(layers.Dense(1, activation='softmax'))
#        model.summary()
        model = models.Sequential()
        model.add(Conv2D(32, (3, 3), activation='elu', input_shape=(200, 160, 3)))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
#        model.add(Conv2D(64, (3, 3), activation= 'relu'))
#        model.add(MaxPooling2D(pool_size=(2, 2)))
#        model.add(Conv2D(128, (3, 3), activation= 'relu'))
#        model.add(MaxPooling2D(pool_size=(2, 2)))     
        model.add(Flatten())
        model.add(Dense(32, activation = 'elu'))
        model.add(BatchNormalization())
       # model.add(Dropout(0.5))
        model.add(Dense(1, activation = 'sigmoid'))
        model.summary()
        
        ################# Build Optimizer #########################################         
        from keras import optimizers
        opt = optimizers.Adam(lr=0.001)
        model.compile(loss='binary_crossentropy', 
              optimizer=opt,#optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])
        
       ################# Build Optimizer ######################################### 

        train_datagen = ImageDataGenerator(rescale=1./255)
        test_datagen = ImageDataGenerator(rescale=1./255)


#        training_data_generator = ImageDataGenerator(rescale=1./255,
#                                                     shear_range=0.1,
#                                                     zoom_range=0.1,
#                                                     horizontal_flip=True)  
        
        training_data_generator = ImageDataGenerator(rescale=1./255)  
     
        train_generator = train_datagen.flow_from_directory(train_dir,
                                                            target_size=(200, 160), 
                                                            batch_size=20,
                                                            class_mode='binary')

        validation_generator = test_datagen.flow_from_directory(val_dir,
                                                                target_size=(200, 160),
                                                                batch_size=20,
                                                                class_mode='binary')

        
        ################# Build Model ######################################### 
        history = model.fit_generator(train_generator,
                              steps_per_epoch=100,
                              epochs=20, #30
                              validation_data=validation_generator,
                              validation_steps=10) #10)
        
        ################# Plot Model Performance ######################################### 
        import matplotlib.pyplot as plt

        acc = history.history['acc']
        val_acc = history.history['val_acc']
        loss = history.history['loss']
        val_loss = history.history['val_loss']
        
        epochs = range(1, len(acc) + 1)
        
        plt.figure()
        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.legend()               
        #plot_train_val_acc = "/Users/sagihaider/Features/EEG_2A/Plots/Plot_S" + str(subject+1) + "train_Val_acc_" + str(row[0]) + str(row[1]) + ".png"
        #plt.savefig(plot_train_val_acc)
        
        plt.figure()
        plt.plot(epochs, loss, 'bo', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.legend()        
        #plt.show()        
        #plot_train_val_loss = "/Users/sagihaider/Features/EEG_2A/Plots/Plot_S" + str(subject+1) + "train_Val_loss" + str(row[0]) + str(row[1])  + ".png"
        #plt.savefig(plot_train_val_loss)
        ###################### clear model #########################################
        #keras.backend.clear_session() 

