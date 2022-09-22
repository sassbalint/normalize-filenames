"""
Generate page numbers for print A5 in duplex.
For pages 1-20 the output is:
1,2,5,6,9,10,13,14,17,18 and
3,4,7,8,11,12,15,16,19,20
"""

import argparse
import sys

from more_itertools import chunked


def main():
    """Do the thing."""
    args = get_args()

    fr = args.fr
    to = args.to
    exclude_fr = args.exclude_from
    exclude_to = args.exclude_to

    x = []
    y = []

    include_range = range(fr, to + 1)
    exclude_range = range(exclude_fr, exclude_to + 1)

    pages = sorted(set(include_range) - set(exclude_range))

    is_x = True
    for pagepair in chunked(pages, 2):
        if is_x:
            x.extend(pagepair)
            is_x = False
        else:
            y.extend(pagepair)
            is_x = True

    print(','.join(map(str, x)))
    print(','.join(map(str, y)))


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-f', '--fr',
        help='from this page number',
        type=int,
        default='1'
    )
    parser.add_argument(
        '-t', '--to',
        help='to this page number',
        type=int,
        default='2'
    )
    parser.add_argument(
        '--exclude-from',
        help='exclude from this page number',
        type=int,
        default='2'
    )
    parser.add_argument(
        '--exclude-to',
        help='exclude to this page number',
        type=int,
        default='1'
    )
 
    
    return parser.parse_args()


if __name__ == '__main__':
    main()
