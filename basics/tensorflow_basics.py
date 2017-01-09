# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:11:44 2016

@author: yjl20
"""

#packages importations

import tensorflow as tf
import numpy as np

#differents definitions of matrix

mat1 = np.array([[1.7,2.1],[3.2,4.5]])
mat2 = tf.constant([[1.7,2.1],[3.2,4.5]])
print('type of mat1' , type(mat1)) 
print('type of mat2' , type(mat2))

print('=========================================================')


mat1prime = tf.convert_to_tensor(mat1)
print('type of mat1prime',type(mat1prime))
print( 'type of mat2',type(mat2))

print('############################################################')

x = tf.constant([1,2])
neg_x = tf.neg(x)
print(neg_x)

print('=========================================================')
with tf.Session() as sess:
    result = sess.run(neg_x)
    print(result)

print('############################################################')

sess = tf.InteractiveSession()
x = tf.constant([[1. , 2.]])
neg_op = tf.neg(x)

result = neg_op.eval()
print(result)

sess.close()
