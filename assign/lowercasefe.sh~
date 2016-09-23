#!/bin/bash
if [ $# -eq 0 ] ; then
	for filename in *
	do 
		file_ext="$($_CMD echo $filename |awk -F . '{if (NF>1) {print $NF}}')"
		n="$($_CMD echo $file_ext | tr A-Z a-z )"
		if [ "$file_ext" != "$n" ] ; then
				mv $filename `echo $filename | sed 's/\(.*\.\)$file_ext /\1$n/'`
		fi
	done
fi
