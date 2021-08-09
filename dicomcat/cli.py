import argparse

from dicomcat import dicomcat

def parse_args() -> argparse.Namespace:
    parser= argparse.ArgumentParser(description='Shows DICOM scans in terminal')
    parser.add_argument("path", 
                        type=str, 
                        help='''The path to the DICOM to be shown. This 
                                can be a folder or individual .dcm file.''')
    parser.add_argument("--max_slices", 
                        type=int, 
                        default=12,
                        help='''The maximum number of slices of the dicom to show''')   
    parser.add_argument("--num_rows",
                        type=int,
                        default=3,
                        help="The number of rows to show the slices on")
    return parser.parse_args()


def show_dicom(): 
    args = parse_args()
    dicomcat(args.path,
             max_num_slices=args.max_slices,
             num_rows=args.num_rows)


