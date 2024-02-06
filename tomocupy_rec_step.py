import tomopy
import dxchange
import tomocupy

import numpy as np
import tkinter as tk
import ipywidgets as widgets
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join
from types import SimpleNamespace
from queue import Queue
from threading import Thread

import reader as dx
import writer as wr

import utils

fname = '/data/2022-12/Luxi_173.h5'
data, flat, dark, theta = dxchange.read_aps_tomoscan_hdf5(fname)#, sino=(100, 400))
_, meta_dict = dxchange.read_hdf_meta(fname)

params_dict = {}
for section in tomocupy.config.RECON_STEPS_PARAMS:
    for key, value in tomocupy.config.SECTIONS[section].items():
        key = key.replace('-', '_')
        params_dict[key] = value['default']

# create a parameter object identical to the one passed using the CLI
args = SimpleNamespace(**params_dict)

# set only the parameters that are different from the default
args.reconstruction_type          = 'full'
args.file_name                    = fname
args.rotation_axis_auto           = 'auto'
args.out_path_name                = '/data/tmpfdc/' 
args.clear_folder                 = True
args.fbp_filter                   = 'shepp' 
args.retrieve_phase_method        = None 
args.remove_stripe_method         = 'vo'
args.pixel_size                   = meta_dict['measurement_instrument_detection_system_objective_resolution'][0] * 1e-4
args.propagation_distance         = meta_dict['measurement_instrument_detector_motor_stack_setup_z'][0]
args.energy                       = meta_dict['measurement_instrument_monochromator_energy'][0]
args.retrieve_phase_alpha         = 0.0008
args.rotation_axis_sift_threshold = 0.5 # remove this once the default for rotation-axis-sift-threshold in config.py is set to 0.5 (now is '0.5')


clrotthandle = tomocupy.FindCenter(args)
args.rotation_axis = clrotthandle.find_center()*2**args.binning
print(f'set rotaion  axis {args.rotation_axis}')

cl_reader = dx.Reader(args)
print('Reading data.')
data, flat, dark = cl_reader.read_data_parallel()

cl_writer = wr.Writer(cl_reader)

clpthandle = tomocupy.GPURecSteps(cl_reader, cl_writer)
clpthandle.recon_steps_all(data, flat, dark)

print('Done!')


