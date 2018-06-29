#!/bin/sh
dir=$1
echo $1
start=$2
end=$3
out=$4

function cvtSeconds(){
	echo time is $1
	t=$1
	h=${t:0:2}
	m=${t:3:2}
	s=${t:6:2}
	ms=${t:9}
	let tt=`expr $h*60*60+$m*60+$s+$ms/100`
	return $tt
}

if test -d $1
then
	cd $1
	flist=`ls`
	for ff in $flist
	do
		if test -f $ff
		then
			time=`ffmpeg -i $ff 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//`
			echo $ff total time is $time
			cvtSeconds $time
			ss=$?
			echo $ss
			let dd=$ss-$start-$end
			echo $dd
			a=`ffmpeg -ss $start -t $dd  -accurate_seek -i $ff -codec copy -avoid_negative_ts 1 $out/$ff -y`
		#	mv cut.mp4 $out/$ff
		fi
		if test -d $ff
		then
			echo $ff is dir
		fi
	done
	cd -
fi
#for file in $dir/*
#filelist=`ls $1/*`
#for file in $filelist
#do
#	if test -f $file
#	then
#		echo $file is file
#		time=`ffmpeg -i $file 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//`
#		echo $file total time is $time
#		cvtSeconds $time
#		ss=$?
#		echo $ss
#	fi
#	if test -d $file
#	then
#		echo $file is dir
#	fi
#done 
