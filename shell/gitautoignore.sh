#!/bin/bash
#
#
# Git Autoignore 
# 
# - Produce list of MIME type 'application/x-executable' files found by 
#   recursive search of current working directory.

# Exit on error.
set -e

# TODO SEARCHPATH should be relative ./
SEARCHPATH=./ 

# Recures SEARCHPATH to produce tree of files to be tested.
find $SEARCHPATH -name "*" -print > /tmp/.gitautoignore

# TODO tag as gitautoremove for updated appending.
# TAGLINE=GitAutoIgnore

# Test each file for matching MIME type and output .gitignore file in current working directory 
file --mime-type -f /tmp/.gitautoignore | grep -h application\/x-exe | cut -d : -f 1 >> .gitignore 
