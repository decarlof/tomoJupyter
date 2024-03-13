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
        # print(Path(file_name))
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
        # Concatenate the NumPy arrays along the desired axis, if needed
        final_numpy_array = np.concatenate(numpy_arrays, axis=0)  # Adjust axis as per your requirement
        return final_numpy_array

# fname = '/data/2022-12/Luxi_173.h5'
# numpy_array = data2numpy(fname)

fname = '/data/2022-12_rec/Luxi_173_rec.h5'
numpy_array = datalinks2numpy(fname)
print(numpy_array.shape)

# fname = '/data/2022-12/Luxi_173.h5'
# obj.__array__ = <bound method Dataset.__array__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__bool__ = <bound method HLObject.__bool__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__class__ = <class 'h5py._hl.dataset.Dataset'>
# obj.__delattr__ = <method-wrapper '__delattr__' of Dataset object at 0x7fced04a3bb0>
# obj.__dict__ = {'_id': <h5py.h5d.DatasetID object at 0x7fced0488db0>, '_dcpl': <h5py.h5p.PropDCID object at 0x7fcf77d11400>, '_dxpl': <h5py.h5p.PropDXID object at 0x7fced0494810>, '_filters': {}, '_readonly': True, '_cache_props': {'shape': (1800, 852, 2800)}}
# obj.__dir__ = <built-in method __dir__ of Dataset object at 0x7fced04a3bb0>
# obj.__doc__ = '\n        Represents an HDF5 dataset\n    '
# obj.__eq__ = <bound method HLObject.__eq__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__format__ = <built-in method __format__ of Dataset object at 0x7fced04a3bb0>
# obj.__ge__ = <method-wrapper '__ge__' of Dataset object at 0x7fced04a3bb0>
# obj.__getattribute__ = <method-wrapper '__getattribute__' of Dataset object at 0x7fced04a3bb0>
# obj.__getitem__ = <bound method Dataset.__getitem__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__getnewargs__ = <bound method HLObject.__getnewargs__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__getstate__ = <bound method HLObject.__getstate__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__gt__ = <method-wrapper '__gt__' of Dataset object at 0x7fced04a3bb0>
# obj.__hash__ = <bound method HLObject.__hash__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__init__ = <bound method Dataset.__init__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__init_subclass__ = <built-in method __init_subclass__ of type object at 0x558456ddd1c0>
# obj.__iter__ = <bound method Dataset.__iter__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__le__ = <method-wrapper '__le__' of Dataset object at 0x7fced04a3bb0>
# obj.__len__ = <bound method Dataset.__len__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__lt__ = <method-wrapper '__lt__' of Dataset object at 0x7fced04a3bb0>
# obj.__module__ = 'h5py._hl.dataset'
# obj.__ne__ = <method-wrapper '__ne__' of Dataset object at 0x7fced04a3bb0>
# obj.__new__ = <built-in method __new__ of type object at 0x5584557b9d60>
# obj.__nonzero__ = <bound method HLObject.__bool__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__reduce__ = <built-in method __reduce__ of Dataset object at 0x7fced04a3bb0>
# obj.__reduce_ex__ = <built-in method __reduce_ex__ of Dataset object at 0x7fced04a3bb0>
# obj.__repr__ = <bound method Dataset.__repr__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__setattr__ = <method-wrapper '__setattr__' of Dataset object at 0x7fced04a3bb0>
# obj.__setitem__ = <bound method Dataset.__setitem__ of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.__sizeof__ = <built-in method __sizeof__ of Dataset object at 0x7fced04a3bb0>
# obj.__str__ = <method-wrapper '__str__' of Dataset object at 0x7fced04a3bb0>
# obj.__subclasshook__ = <built-in method __subclasshook__ of type object at 0x558456ddd1c0>
# obj.__weakref__ = None
# obj._cache_props = {'shape': (1800, 852, 2800)}
# obj._d = <bound method CommonStateObject._d of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj._dcpl = <h5py.h5p.PropDCID object at 0x7fcf77d11400>
# obj._dxpl = <h5py.h5p.PropDXID object at 0x7fced0494810>
# obj._e = <bound method CommonStateObject._e of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj._extent_type = 1
# obj._fast_read_ok = True
# obj._fast_reader = <h5py._selector.Reader object at 0x7fced5a36a40>
# obj._filters = {}
# obj._id = <h5py.h5d.DatasetID object at 0x7fced0488db0>
# obj._is_empty = False
# obj._lapl = <h5py.h5p.PropLAID object at 0x7fced5c28540>
# obj._lcpl = <h5py.h5p.PropLCID object at 0x7fced5c284f0>
# obj._readonly = True
# obj._selector = <h5py._selector.Selector object at 0x7fced0287b30>
# obj.asstr = <bound method Dataset.asstr of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.astype = <bound method Dataset.astype of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.attrs = <Attributes of HDF5 object at 140526234406320>
# obj.chunks = (1, 852, 2800)
# obj.compression = None
# obj.compression_opts = None
# obj.dims = <Dimensions of HDF5 object at 140526234406320>
# obj.dtype = dtype('uint16')
# obj.external = None
# obj.fields = <bound method Dataset.fields of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.file = <HDF5 file "Luxi_173.h5" (mode r)>
# obj.fillvalue = 0
# obj.fletcher32 = False
# obj.flush = <bound method Dataset.flush of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.id = <h5py.h5d.DatasetID object at 0x7fced0488db0>
# obj.is_scale = False
# obj.is_virtual = False
# obj.iter_chunks = <bound method Dataset.iter_chunks of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.len = <bound method Dataset.len of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.make_scale = <bound method Dataset.make_scale of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.maxshape = (1840, 852, 2800)
# obj.name = '/exchange/data'
# obj.nbytes = 8588160000
# obj.ndim = 3
# obj.parent = <HDF5 group "/exchange" (5 members)>
# obj.read_direct = <bound method Dataset.read_direct of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.ref = <HDF5 object reference>
# obj.refresh = <bound method Dataset.refresh of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.regionref = <h5py._hl.base._RegionProxy object at 0x7fced5a347f0>
# obj.resize = <bound method Dataset.resize of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.scaleoffset = None
# obj.shape = (1800, 852, 2800)
# obj.shuffle = False
# obj.size = 4294080000
# obj.virtual_sources = <bound method Dataset.virtual_sources of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>
# obj.write_direct = <bound method Dataset.write_direct of <HDF5 dataset "data": shape (1800, 852, 2800), type "<u2">>


# fname = '/data/2022-12_rec/Luxi_173_rec.h5'
# obj.__array__ = <bound method Dataset.__array__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__bool__ = <bound method HLObject.__bool__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__class__ = <class 'h5py._hl.dataset.Dataset'>
# obj.__delattr__ = <method-wrapper '__delattr__' of Dataset object at 0x7efe599737f0>
# obj.__dict__ = {'_id': <h5py.h5d.DatasetID object at 0x7efe54381b80>, '_dcpl': <h5py.h5p.PropDCID object at 0x7efefbc50400>, '_dxpl': <h5py.h5p.PropDXID object at 0x7efe543d48b0>, '_filters': {}, '_readonly': True, '_cache_props': {'shape': (852, 2800, 2800)}}
# obj.__dir__ = <built-in method __dir__ of Dataset object at 0x7efe599737f0>
# obj.__doc__ = '\n        Represents an HDF5 dataset\n    '
# obj.__eq__ = <bound method HLObject.__eq__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__format__ = <built-in method __format__ of Dataset object at 0x7efe599737f0>
# obj.__ge__ = <method-wrapper '__ge__' of Dataset object at 0x7efe599737f0>
# obj.__getattribute__ = <method-wrapper '__getattribute__' of Dataset object at 0x7efe599737f0>
# obj.__getitem__ = <bound method Dataset.__getitem__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__getnewargs__ = <bound method HLObject.__getnewargs__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__getstate__ = <bound method HLObject.__getstate__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__gt__ = <method-wrapper '__gt__' of Dataset object at 0x7efe599737f0>
# obj.__hash__ = <bound method HLObject.__hash__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__init__ = <bound method Dataset.__init__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__init_subclass__ = <built-in method __init_subclass__ of type object at 0x5584ed1271c0>
# obj.__iter__ = <bound method Dataset.__iter__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__le__ = <method-wrapper '__le__' of Dataset object at 0x7efe599737f0>
# obj.__len__ = <bound method Dataset.__len__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__lt__ = <method-wrapper '__lt__' of Dataset object at 0x7efe599737f0>
# obj.__module__ = 'h5py._hl.dataset'
# obj.__ne__ = <method-wrapper '__ne__' of Dataset object at 0x7efe599737f0>
# obj.__new__ = <built-in method __new__ of type object at 0x5584eb5e1d60>
# obj.__nonzero__ = <bound method HLObject.__bool__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__reduce__ = <built-in method __reduce__ of Dataset object at 0x7efe599737f0>
# obj.__reduce_ex__ = <built-in method __reduce_ex__ of Dataset object at 0x7efe599737f0>
# obj.__repr__ = <bound method Dataset.__repr__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__setattr__ = <method-wrapper '__setattr__' of Dataset object at 0x7efe599737f0>
# obj.__setitem__ = <bound method Dataset.__setitem__ of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.__sizeof__ = <built-in method __sizeof__ of Dataset object at 0x7efe599737f0>
# obj.__str__ = <method-wrapper '__str__' of Dataset object at 0x7efe599737f0>
# obj.__subclasshook__ = <built-in method __subclasshook__ of type object at 0x5584ed1271c0>
# obj.__weakref__ = None
# obj._cache_props = {'shape': (852, 2800, 2800)}
# obj._d = <bound method CommonStateObject._d of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj._dcpl = <h5py.h5p.PropDCID object at 0x7efefbc50400>
# obj._dxpl = <h5py.h5p.PropDXID object at 0x7efe543d48b0>
# obj._e = <bound method CommonStateObject._e of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj._extent_type = 1
# obj._fast_read_ok = True
# obj._fast_reader = <h5py._selector.Reader object at 0x7efe59963a40>
# obj._filters = {}
# obj._id = <h5py.h5d.DatasetID object at 0x7efe54381b80>
# obj._is_empty = False
# obj._lapl = <h5py.h5p.PropLAID object at 0x7efe59b67680>
# obj._lcpl = <h5py.h5p.PropLCID object at 0x7efe59b676d0>
# obj._readonly = True
# obj._selector = <h5py._selector.Selector object at 0x7efe541c6b30>
# obj.asstr = <bound method Dataset.asstr of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.astype = <bound method Dataset.astype of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.attrs = <Attributes of HDF5 object at 139630799756160>
# obj.chunks = None
# obj.compression = None
# obj.compression_opts = None
# obj.dims = <Dimensions of HDF5 object at 139630799756160>
# obj.dtype = dtype('<f4')
# obj.external = None
# obj.fields = <bound method Dataset.fields of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.file = <HDF5 file "Luxi_173_rec.h5" (mode r)>
# obj.fillvalue = 0.0
# obj.fletcher32 = False
# obj.flush = <bound method Dataset.flush of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.id = <h5py.h5d.DatasetID object at 0x7efe54381b80>
# obj.is_scale = False
# obj.is_virtual = True
# obj.iter_chunks = <bound method Dataset.iter_chunks of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.len = <bound method Dataset.len of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.make_scale = <bound method Dataset.make_scale of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.maxshape = (852, 2800, 2800)
# obj.name = '/exchange/data'
# obj.nbytes = 26718720000
# obj.ndim = 3
# obj.parent = <HDF5 group "/exchange" (1 members)>
# obj.read_direct = <bound method Dataset.read_direct of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.ref = <HDF5 object reference>
# obj.refresh = <bound method Dataset.refresh of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.regionref = <h5py._hl.base._RegionProxy object at 0x7efefbc5fee0>
# obj.resize = <bound method Dataset.resize of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.scaleoffset = None
# obj.shape = (852, 2800, 2800)
# obj.shuffle = False
# obj.size = 6679680000
# obj.virtual_sources = <bound method Dataset.virtual_sources of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
# obj.write_direct = <bound method Dataset.write_direct of <HDF5 dataset "data": shape (852, 2800, 2800), type "<f4">>
