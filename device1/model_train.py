# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:55:54 2020

@author: Tapan
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import time 
from tensorflow.keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import pickle
#import matplotlib.pyplot as plt 
#from IPython.display import Image
#%matplotlib inline

def train():
	object_name = "Face"
	main_path = '/home/sarth/Desktop/Project/Dataset/Face/client_1'
	train_path = main_path+'/train'
	valid_path = main_path+'/valid'
	test_path = main_path+'/test'

	train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(
		directory=train_path, target_size=(224,224), batch_size=10)
	valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(
		directory=valid_path, target_size=(224,224), batch_size=10)
	test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(
		directory=test_path, target_size=(224,224), batch_size=10, shuffle=False)
	start = time.time()
	mobile = tf.keras.applications.mobilenet.MobileNet()
	#mobile.summary()
	x = mobile.layers[-6].output
	output = Dense(units=2, activation='softmax')(x)
	model = Model(inputs=mobile.input, outputs=output)

	#model.summary()

	for layer in model.layers[:-5]:
		layer.trainable = False

	model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

	history = model.fit(train_batches,
			  steps_per_epoch=len(train_batches),
			  validation_data=valid_batches,
			  validation_steps=len(valid_batches),
			  epochs=10,
			  verbose=1,use_multiprocessing = False
	)
	model.save("/home/sarth/flask/Fedlearn-master/device1/local_model/cat1.h5")
	x = history.history
	#print(history)
	'''
	file = open('dump.txt', 'w')
	file.write( repr(x) + '\n' )
	file.close()
	'''
	end = time.time() - start
	#print("Time for Training : "+str(end))
	return (x,object_name)
'''
print("Convert to  TFLite")
start3 = time.time()

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
# Save the TF Lite model.
with tf.io.gfile.GFile('/home/pi/tflite1/Face/Models/TFLite/Clients/Client_3/detect.tflite', 'wb') as f:
  f.write(tflite_model)
end3 = time.time() - start3
print("Time for converting :" +str(end3))
'''
'''
saved_model_dir = "/home/pi/tflite1/Dataset_Final/Models/Client_2" 
#Converting a SavedModel to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
'''
#train()

