import os
import unittest
from unittest import TestCase

import dicomcat

class TestDicomCat(TestCase):

    def test_dicom_cat(self):
        test_dicoms_path = os.path.join(os.path.dirname(__file__),'assets/example_dicoms')
        test_dicoms = os.listdir(test_dicoms_path)
        for test_dicom in test_dicoms:
            print(f'Testing file at {test_dicom}')
            dicomcat.dicomcat(os.path.join(test_dicoms_path,test_dicom))

if __name__ == '__main__':
    unittest.__main__()



