#### Libraries
# Standard library
import h5py
import gzip

# Third-party libraries
import numpy as np

f = gzip.open('../data/mnist.pkl.gz', 'rb')
training_data, validation_data, test_data = h5py.File(f)
f.close()
