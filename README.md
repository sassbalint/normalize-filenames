# utils

## normalize filenames

```bash
$ python normalize_filenames.py -h
usage: normalize_filenames.py [-h] -i INPUT_DIR -o OUTPUT_DIR

Normalize filenames: no space and other silly chars.
From one dir to another dir by symlinks to keep original files.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input-dir INPUT_DIR
                        input directory with problematic filenames
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory for relative symlinks
                        with normalized filenames
```

## random sampler

```bash
usage: random_sampler.py [-h] -f FILENAME -s SAMPLESIZE -r
                         RANDOMSEED

Random sampling from very large files.
[Algorithm #3 from here.](http://metadatascience.com/2014/02/27/random-sampling-from-very-large-files)

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        name of file to sample from
  -s SAMPLESIZE, --samplesize SAMPLESIZE
                        number of lines in sample
  -r RANDOMSEED, --randomseed RANDOMSEED
                        random seed
```
