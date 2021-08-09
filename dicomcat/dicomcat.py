import glob
import math
import os
import random
import string
import sys
from scipy import interpolate
import warnings
import pydicom
import pydicom.pixel_data_handlers.gdcm_handler as gdcm_handler


pydicom.config.image_handlers = [None, gdcm_handler]


import matplotlib.pyplot as plt
import numpy as np
import pydicom
from PIL import Image
from pydicom.tag import Tag


def im_show(output_img: np.array) -> None:
      # boilerplate to show current plt image as imgcat
      letters = string.ascii_letters
      temp_img_name = letters+'.png'
      ''.join(random.choice(letters) for i in range(10))
      Image.fromarray(output_img).save(temp_img_name)
      os.system('imgcat ' + temp_img_name)
      os.remove(temp_img_name)

def pad_to_size_and_normalize(img: np.array, size_to_pad_to : np.array) -> np.array:
    pad_vals = size_to_pad_to - np.array(img.shape)
    img = 255*np.pad(img/img.max(), pad_vals)
    return img


def try_read_dicom(dicom_path_file: str) -> list:
    try:
        return [pydicom.dcmread(dicom_path_file)]
    except: return []

def dicomcat(path: str, max_num_slices: int = 12, num_rows: int = 3, resolution_downscale: float = 0.5)->None:
    assert os.path.exists(path), f"Could not find {path}"
    assert num_rows <= max_num_slices, '''Number of rows should be less than 
                                      max number of slices'''
    assert (resolution_downscale > 0) and (resolution_downscale <= 1), "Resolution downscale should be between 0 and 1"
    dcm_objs = []
    if os.path.isdir(path):
        files = sorted(glob.glob(os.path.join(path,'*')))
        dcm_objs = []
        for file_ in files:
            dcm_objs += try_read_dicom(file_)
    else:
        dcm_objs += try_read_dicom(path)
        num_rows=1

    if len(dcm_objs) == 0: print(f"Could not find any DICOM files at {path}!")

    for dcm_obj in dcm_objs: dcm_obj.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian


    else:
        if all([Tag('ImagePositionPatient') in dcm_obj for dcm_obj in dcm_objs]) and \
           all([Tag('ImageOrientationPatient') in dcm_obj for dcm_obj in dcm_objs]):
           image_orientations = np.array([dcm_obj.ImageOrientationPatient for dcm_obj in dcm_objs]).round()
           image_positions = np.array([dcm_obj.ImagePositionPatient for dcm_obj in dcm_objs]).astype(np.float).round()
           mean_image_orientation = image_orientations.mean(axis=0).round()
           if (mean_image_orientation[[0,3]] == [0,0]).all(): orientation = 'Sagittal'
           elif (mean_image_orientation[[2,5]] == [0,0]).all(): orientation = 'Axial'
           elif (mean_image_orientation[[1,4]] == [0,0]).all(): orientation = 'Coronal'
           else: orientation = 'unknown'
           print(f"Image Orientation {orientation}")
           with warnings.catch_warnings():
            # warnings.simplefilter(action='ignore', category=FutureWarning)

            if   orientation == 'Sagittal':
                sort_idxs=np.argsort(image_positions[:,0].astype(float))
            elif orientation == 'Coronal':
                sort_idxs=np.argsort(image_positions[:,1].astype(float))
            elif orientation == 'Axial':
                sort_idxs=np.argsort(image_positions[:,2].astype(float))
            else: sort_idxs = range(len(dcm_objs))

            dcm_objs = [dcm_objs[sort_idx] for sort_idx in sort_idxs]



        else:
            print('Warning: Could not figure out order of slices! (No IOP/IPP)')
            # determine slicing to decide what to sort by

        # if more than max_num_slices, get rid of some slices before showing image
        if len(dcm_objs) > max_num_slices:
            dcm_objs = [dcm_objs[int(len(dcm_objs)*idx/max_num_slices)] for idx in range(max_num_slices)]
        dcm_imgs = [dcm_obj.pixel_array for dcm_obj in dcm_objs]
        max_dcm_img_size = np.array([dcm_img.shape for dcm_img in dcm_imgs]).max(axis=0)
        dcm_imgs = [pad_to_size_and_normalize(dcm_img, max_dcm_img_size) for dcm_img in dcm_imgs]

        num_cols = math.ceil(len(dcm_objs)/num_rows)

        output_img = np.zeros((num_rows*max_dcm_img_size[0],num_cols*max_dcm_img_size[1]),dtype=np.uint8)

        for idx, dcm_img in enumerate(dcm_imgs):
            row_idx = idx // num_cols 
            col_idx = idx % num_cols
            y_loc = row_idx*max_dcm_img_size[0]
            x_loc = col_idx*max_dcm_img_size[1]
            output_img[y_loc:y_loc+dcm_img.shape[0], 
                       x_loc:x_loc+dcm_img.shape[1]] = dcm_img

        for tag_name in ['PatientID','Modality','SeriesDescription']:
            if Tag(tag_name) in dcm_objs[0]:
                print(tag_name +  ':' + str(dcm_objs[0][Tag(tag_name)].value), end=', ')
        print('\n')

        # downscale image so it doesn't slow terminal
        img = Image.fromarray(np.uint8(output_img),'L')
        output_img = np.array(img.resize((int(output_img.shape[1]*resolution_downscale),int(output_img.shape[0]*resolution_downscale))))
        im_show(output_img)
