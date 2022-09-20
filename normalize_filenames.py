"""
Normalize filenames: no space and other silly chars.
From one dir to another dir by symlinks to keep original files.
"""

import argparse
import os

SILLY_CHARS = [
    ' ','[',']','(',')',
    '\\','`','*','{','}',
    '>','#','!','$','\'', '"'
]

REPLACEMENT = '_'


def normalize(filename):
    """Do the thing."""

    for ch in SILLY_CHARS:
        if ch in filename:
            filename = filename.replace(ch, REPLACEMENT)

    return filename


def main():
    """Main."""
    args = get_args()

    inputdir = args.input_dir
    outputdir = args.output_dir

    for entry in os.scandir(inputdir):

        entryname = entry.name

        norm_name = normalize(entryname)

        relpath = os.path.relpath(inputdir, outputdir)

        os.symlink(
            os.path.join(relpath, entryname),
            os.path.join(outputdir, norm_name)
        )


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input-dir',
        help='input directory with problematic filenames',
        required=True,
        type=str,
        default=argparse.SUPPRESS
    )
    parser.add_argument(
        '-o', '--output-dir',
        help='output directory for relative symlinks with normalized filenames',
        required=True,
        type=str,
        default=argparse.SUPPRESS
    )  
    
    return parser.parse_args()


if __name__ == '__main__':
    main()
