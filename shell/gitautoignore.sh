#!/bin/bash
#////////////////////////////////////////////////////////////////////////////////////////
#/ 											#
#/	Git AutoIgnore 									#
#/ 											#
#/ 	Produce a list of MIME type 'application/x-executable' files found by 		#
#/   	recursive search of current working directory.					#
#/											#
#/											#
#/	Usage:										#
#/	./gitautoignore will append list to .gitignore 					#
#/											#
#////////////////////////////////////////////////////////////////////////////////////////
######################################################################################



# Exit on error.
set -e

# TODO SEARCHPATH should be relative ./
SEARCHPATH=./ 

# Recures SEARCHPATH to produce tree of files to be tested.
find $SEARCHPATH -name "*" -print  > /tmp/.gitautoignore

# TODO tag as gitautoremove for updated appending.
# TAGLINE=GitAutoIgnore

# Test each file for matching MIME type and output .gitignore file in current working directory 

# grep --exclude-from=.gitignore
file --mime-type -f /tmp/.gitautoignore | grep -h application\/x-exe | cut -d : -f 1 | sed "s/^\.\/\(.*\)/\1 #AUTOIGNORE/" >> .gitignore

#FILES=`file --mime-type -f /tmp/.gitautoignore` 
#FILES=echo $FILES | grep -h application\/x-exe 
#echo $FILES | cut -d : -f 1 | sed "s/^\.\/\(.*\)/\1/" >> .gitignore
