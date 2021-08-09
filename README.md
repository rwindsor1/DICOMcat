# DICOMcat

![](example.gif)

DICOMcat is a simple, pip-installable python package for displaying DICOM files in iTerm2 similar 
to [imgcat](https://github.com/eddieantonio/imgcat) for conventional images and [niicat](https://github.com/MIC-DKFZ/niicat)
for nifti images. This might be useful for quickly viewing DICOMs on a remote
server in your terminal.



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
