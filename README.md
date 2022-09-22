# utils

## normalize filenames

```pre
$ python3 normalize_filenames.py -h
usage: normalize_filenames.py [-h] -i INPUT_DIR -o OUTPUT_DIR

Normalize filenames: no space and other silly chars.
From one dir to another dir by symlinks to keep original files.

arguments:
  -i INPUT_DIR, --input-dir INPUT_DIR
                        input directory with problematic filenames
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory for relative symlinks
                        with normalized filenames
```

## print duplex pages

```pre
$ python3 print_duplex_pages.py -h
usage: print_duplex_pages.py [-h] [-f FR] [-t TO]
                             [--exclude-from EXCLUDE_FROM]
                             [--exclude-to EXCLUDE_TO]

Generate page numbers for print A5 in duplex.
For pages 1-20 the output is:
1,2,5,6,9,10,13,14,17,18 and 3,4,7,8,11,12,15,16,19,20

optional arguments:
  -f FR, --fr FR        from this page number (default: 1)
  -t TO, --to TO        to this page number (default: 2)
  --exclude-from EXCLUDE_FROM
                        exclude from this page number (default: 2)
  --exclude-to EXCLUDE_TO
                        exclude to this page number (default: 1)
```

## random sampler

```pre
$ python3 random_sampler.py -h
usage: random_sampler.py [-h] -f FILENAME -s SAMPLESIZE -r RANDOMSEED

Random sampling from very large files.

arguments:
  -f FILENAME, --filename FILENAME
                        name of file to sample from
  -s SAMPLESIZE, --samplesize SAMPLESIZE
                        number of lines in sample
  -r RANDOMSEED, --randomseed RANDOMSEED
                        random seed
```

[Based on _algorithm 3_ from this post.](http://metadatascience.com/2014/02/27/random-sampling-from-very-large-files)
