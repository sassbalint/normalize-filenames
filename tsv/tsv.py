"""
Utils for tsv file format.
"""


import csv


def load_tsv_dict(inputfile):
    """Load a (two-column) tsv file into a dict."""
    return dict(load_tsv(inputfile))


def load_tsv(inputfile):
    """Load a tsv file into a list of lists."""
    return list(
        csv.reader(open(inputfile, encoding='utf-8'),
        delimiter='\t'))


def main():
    """Main."""
    print(__doc__)


if __name__ == '__main__':
    main()
