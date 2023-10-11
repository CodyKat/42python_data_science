#!/bin/sh

i=0
while [ "$i" -ne "$1" ]
do
	if [ $i -lt 10 ]
	then
		mkdir ex0$i
	else
		mkdir ex$i
	fi
	i=$((i+1))
done
