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
COMMENT="AutoIgnore"
MIME_TYPE="application\/x-exe"



# Remove existing GitAutoIgnore entires by filtering COMMENT and clobbering .gitignore

if [ ! -s ".gitignore" ]; then
echo "#### File automatically generate by GitAutoIgnore ####" > .gitignore
fi

# TODO This doesn't tollerate an empty file due to requiring \n before <COMMENT...
# however, we also want to filter the preceeding \n to avoid inserting blank lines on every update

# Remember the nasty preceeding newline.
sed -n '1h;1!H; ${;g;s/\(.*[^\n]\)[\n]*#<'${COMMENT}'>.*#<'${COMMENT}'\/>\(.*\)/\1\2/g;p}' .gitignore > /tmp/.gitignore
cp /tmp/.gitignore ./ 


# Recures SEARCHPATH to produce tree of files to be tested.
find $SEARCHPATH -name "*" -print  > /tmp/.gitautoignore.tree


# Test each file for matching MIME type and output .gitignore file in current working directory 

# Test MIME type from tmp file tree, strip leading ./ on files in current dir. Append list with #comments.

file --mime-type -f /tmp/.gitautoignore.tree | grep -h $MIME_TYPE | cut -d : -f 1 | sed "s/^\.\/\(.*\)/\1/" > /tmp/.gitignore.new


echo "#<$COMMENT>" >> .gitignore
cat /tmp/.gitignore.new >> .gitignore 
echo "#<$COMMENT/>" >> .gitignore


echo
echo "Git Auto Ignore --> Files included in .gitignore:"  
cat /tmp/.gitignore.new | more
echo
git status
echo
echo 'Now try: git commit -a -m "[...commit message...]" to add and commit.'

#FILES=`file --mime-type -f /tmp/.gitautoignore` 
#FILES=echo $FILES | grep -h application\/x-exe 
#echo $FILES | cut -d : -f 1 | sed "s/^\.\/\(.*\)/\1/" >> .gitignore
