#!/usr/bin/env python
# * coding: utf8 *
'''
image-fixer.py
A module that saves an image with the rotation setting of the operating system and scales the image.

USAGE: image-fixer.py [-h] [--recursive] directory [directory ...]

positional arguments:
  directory

optional arguments:
  -h, --help       show this help message and exit
  --recursive, -r
'''

import argparse
from pathlib import Path

from PIL import Image, ImageOps

SQUARE = 1000


def main():
    ''' The entry point to the script
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', '-d', nargs='+')
    parser.add_argument('--recursive', '-r', action='store_true')
    args = parser.parse_args()

    for directory in args.dir:
        process_directory(directory, args.recursive)


def fix(path):
    ''' This function resizes and updates the rotation a picture
    '''
    image = Image.open(path)

    try:
        image = ImageOps.exif_transpose(image)
    except TypeError:
        pass

    image.thumbnail((SQUARE, SQUARE))

    path = path.with_suffix('.jpg')

    image.save(path)


def process_directory(path, recursive=False):
    ''' This function processes all elements from a directory
    '''
    path = Path(path)

    if not path.is_dir():
        print(f'{path} is not a directory')

        return

    pattern = '*.jpg'

    if recursive:
        pattern = '**/*.jpg'

    for image in path.glob(pattern):
        print(f'processing {image}')

        fix(str(image))


if __name__ == '__main__':
    main()
