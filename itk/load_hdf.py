import h5py
from pathlib import Path
import numpy as np
import dxchange
from pprint import pprint

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

def data2numpy(file_name):
    # convert the dataset contained in an hdf file into a numpy array
    # works only when data are in the hdf file, not when are linked to external files 
    with h5py.File(file_name, 'r') as hdf5_file:
        dataset = hdf5_file['exchange/data']
        # dump(dataset)
        numpy_array = np.array(dataset) 
        return numpy_array

def datalinks2numpy(file_name):
    # convert the dataset contained in an hdf file into a numpy array
    # works only when data linked to external files 
    with h5py.File(file_name, 'r') as main_file:
        # Access the dataset which contains links to external files
        linked_dataset = main_file['exchange/data']
        path = Path(file_name).with_suffix('')
        parts_path = f'{path}_parts'
        # Initialize an empty list to store NumPy arrays
        numpy_arrays = []
        # Iterate over each external HDF file
        for file_path in list(Path(parts_path).glob('*.*')):
             # Open the external HDF file
            with h5py.File(file_path, 'r') as external_file:
                # Access the dataset within the external file
                dataset = external_file['exchange/data']  
                # Convert the dataset to a NumPy array and append to the list
                numpy_array = np.array(dataset)
                numpy_arrays.append(numpy_array)
        # Concatenate the NumPy arrays along the desired axis
        final_numpy_array = np.concatenate(numpy_arrays, axis=0)
        return final_numpy_array

fname = '/data/2022-12/Luxi_173.h5'
numpy_array_1 = data2numpy(fname)

fname = '/data/2022-12_rec/Luxi_173_rec.h5'
numpy_array_2 = datalinks2numpy(fname)

