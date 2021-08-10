# DICOMcat

![](example.gif)

DICOMcat is a simple, [pip-installable](https://pypi.org/project/dicomcat/) python package for displaying DICOM files in iTerm2 similar 
to [imgcat](https://github.com/eddieantonio/imgcat) for conventional images and [niicat](https://github.com/MIC-DKFZ/niicat)
for nifti images. This might be useful for quickly viewing DICOMs on a remote
server in your terminal.

## Installation

To use either pip install (`pip install dicomcat`) or clone the source code and add to your python path.

## Usage

DICOMcat can be used, either within a python script or from the terminal

To use in terminal, navigate to the DICOM folder/file and enter

`$ dicomcat EXAMPLE_FILE`

In a python script, use as follows

`
import dicomcat
path='path/to/dicom'
dicomcat.dicomcat(path)
`

There are additional options to change the number of rows, downscaling, or maximum number of slices shown (when displaying 
a directory of DICOM slices).

## Examples/Testing

There are a number of example DICOMS to test with the repo. To run the examples, run `python -m unittest` in the package directory

Example Dicom Sources:
- `LumbarDicomExample` - Radiopedia.org, Case courtesy of Prof. Frank Galliard [source](https://radiopaedia.org/cases/normal-lumbar-spine-mri?lang=gb)
- `Head` - Head CT, courtesy of Visual Human Project [source](https://medicine.uiowa.edu/mri/facility-resources/images/visible-human-project-ct-datasets)
- `Knee` - Knee CT,  courtesy of Visual Human Project [source](https://medicine.uiowa.edu/mri/facility-resources/images/visible-human-project-ct-datasets)
- `BrainExample` - Brain MRI, courtesy of Jeff Mather, Mathworks [source](https://uk.mathworks.com/matlabcentral/fileexchange/2762-dicom-example-files)

## Features to be added

The following are planned to be added in the fullness of time:
- GIF view through slices instead of grid.
- Adding handlers for compressed pixel data (for now, update your pydicom, [see here](https://pydicom.github.io/pydicom/stable/old/image_data_handlers.html)
- [libsixel](https://github.com/saitoha/libsixel) support for use with terminals other than iTerm2

If you'd like to contribute one of these or your own feature, feel free to submit a PR.
