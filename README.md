# Photo-Sort

[![Build Status](https://travis-ci.org/Matt-Gleich/Photo-Sort.svg?branch=master)](https://travis-ci.org/Matt-Gleich/Photo-Sort)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1856b1ae8bb44b4b87a01f420109d5ae)](https://www.codacy.com/app/matthewgleich/Photo-Sort?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Matt-Gleich/Photo-Merge&amp;utm_campaign=Badge_Grade)

## Description
The Photo Merging application will sort a directory of photos. It does this by getting the creation date for the file and making a folder for its date. For example, a photo that was taken on April 8th, 2004 will go into a 2004 folder, then an April folder, and then a April-8th folder. If the folder already exists than it will simply move it into the folder. This program will also see if two photos have the same name and if they do, they will be moved to the duplicates folder.

## Features
Below is a list of all the features of this program:

1. Get the creation date of the file
2. Move the file into the corresponding folder


## Requirements
Before running the program for the first time, you need to install the one piece of software that this app needs. Once you have the folder for the app downloaded, you need to run the install command from inside this folder. Please run the following commands:
1. `cd Photo-Merge`
2. `pip install -r requirements.txt`

## Usage:
Once you have installed the requirements, you can now run the program! You run the program by inputing the following command once you are in the folder:

`python main.py`

## Bugs
If you find a bug in my program, please report it to the issues page on GitHub

## Contributors
* Matthew Gleich (@Matt-Gleich)
