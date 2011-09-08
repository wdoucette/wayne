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
#/											#
#/	Do: ./gitautoignore to append list to .gitignore in current directory		#
#/											#
#/											#
#////////////////////////////////////////////////////////////////////////////////////////
######################################################################################



# Exit on error.
#set -e

# TODO SEARCHPATH should be relative ./
SEARCHPATH=./ 
COMMENT="GITAUTOIGNORE"
MIME_TYPE="application\/x-exe"

# Remove existing entires by filtering COMMENT and clobbering .gitignore
if [ -s ".gitignore" ]
then 
cat .gitignore | grep -v $COMMENT > /tmp/.gitignore
mv /tmp/.gitignore ./
fi

# Recures SEARCHPATH to produce tree of files to be tested.
find $SEARCHPATH -name "*" -print  > /tmp/.gitautoignore

# TODO tag as gitautoremove for updated appending.
# TAGLINE=GitAutoIgnore

# Test each file for matching MIME type and output .gitignore file in current working directory 

# grep --exclude-from=.gitignore
# Test MIME type from tmp tree file, strip leading ./ on files in current dir. Append list with #comments.
file --mime-type -f /tmp/.gitautoignore | grep -h $MIME_TYPE | cut -d : -f 1 | sed "s/^\.\/\(.*\)/\1\t#${COMMENT}/" >> .gitignore

#FILES=`file --mime-type -f /tmp/.gitautoignore` 
#FILES=echo $FILES | grep -h application\/x-exe 
#echo $FILES | cut -d : -f 1 | sed "s/^\.\/\(.*\)/\1/" >> .gitignore
