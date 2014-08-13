Palette-Swap
============

Takes the pixels from a picture and reorders them to create another picture

## Dependencies

This script requires the Python PIL package which can be downloaded here http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow for Windows

## Usage

Input the path to the source picture, destination picture, and the time (in seconds) you want to run the program for. 2.5 minutes is good enough and works best with two images that have the same number of pixels (dimensions can be different). If there aren't enough pixels in the source picture then pixels will be reused starting from the top left and if the source picture is larger than the destination picture then only the necessary amount will be used (starting from the top left)

## Example: Mona Lisa and American Gothic

| Mona Lisa | American Gothic |
| --------- | --------------- |
|![Original Mona Lisa](Original/Mona%20Lisa.png "Original Mona Lisa") | ![Original American Gothic](Original/American%20Gothic.png "Original American Gothic")|


| Mona Lisa to American Gothic |
| :--------------------------: |
|![Mona Lisa to American Gothic](Created/Mona%20Lisa%20to%20American%20Gothic.png "Mona Lisa to American Gothic") |
