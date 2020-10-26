# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:05:19 2018

@author: admin
"""

import pickle, gzip, numpy

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()