from setuptools import setup

setup(name= 'dicomcat',
      version= '0.2',
      description='A simple python-based tool based on imgcat for displaying DICOM files in iTerm2.',
      long_description_content_type='text/markdown',
      long_description='README.md',
      url='https://github.com/rwindsor1/DICOMcat',
      author ='Rhydian Windsor',
      author_email= 'windsorrhydian@gmail.com',
      license= 'MIT',
      packages=['dicomcat'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
            'console_scripts': ['dicomcat=dicomcat.cli:show_dicom']
      },
      include_package_data=True,
      ip_safe=False)
