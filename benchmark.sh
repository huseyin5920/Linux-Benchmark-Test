#! /bin/bash


banner()
{
  echo "+------------------------------------------+"
  printf "| %-40s |\n" "`date`"
  echo "|                                          |"
  printf "|`tput bold` %-40s `tput sgr0`|\n" "$@"
  echo "+------------------------------------------+"
}

banner " --------  BENCHMARK  -------- "
banner " 1 - MPLAYER VIDEO BENCHMARK "
banner " 2 - FOLDER ZIP BENCHMARK"
banner " 3 - GIMP PHOTO BENCHMARK"
banner " 4 - LIBREOFFICE BENCHMARK"
banner " 5 - BLENDER BENCHMARK"
banner " 6 - FREECAD BENCHMARK"
banner " 7 - KERNEL COMPILE BENCHMARK"

sleep 5



echo " ---- MPLAYER ----"
banner "MPLAYER"
mplayer -nosound -benchmark /home/benchmark/Desktop/bash/video/telescope.mp4 > /home/benchmark/Desktop/bash/results/mplayer.txt



echo " ---- GIMP ---- "
banner "GIMP"
start=`date +%s.%N`
sh /home/benchmark/Desktop/bash/gimp.sh 
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > /home/benchmark/Desktop/bash/results/gimp.txt



echo " ---- LIBREOFFICE ---- "
banner "LOBREOFFICE"
start=`date +%s.%N`
exec python3 /home/benchmark/Desktop/bash/librepythoncontrol.py &
sh /home/benchmark/Desktop/bash/libreoffice.sh 
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > /home/benchmark/Desktop/bash/results/libreoffice.txt


echo " ---- BLENDER ---- "
banner "BLENDER"
start=`date +%s.%N`
sh /home/benchmark/Desktop/bash/blenderRun.sh 
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > /home/benchmark/Desktop/bash/results/blender.txt


echo " ---- FREECAD ---- "
banner "FREECAD"
start=`date +%s.%N`
sh /home/benchmark/Desktop/bash/freecadRun.sh 
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > /home/benchmark/Desktop/bash/results/freecad.txt


echo " ---- FOLDER ZIP ---- "
banner "FOLDER ZIP"
start=`date +%s.%N`
sh /home/benchmark/Desktop/bash/zip.sh 
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > /home/benchmark/Desktop/bash/results/zip.txt


banner " --------  KERNEL COMPILER  -------- "
echo " ---- KERNEL COMPILER ----"
start=`date +%s.%N`
sh /home/benchmark/Desktop/bash/kernel-compiler.sh 
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > /home/benchmark/Desktop/bash/results/kernel.txt


/usr/bin/python3 /home/benchmark/Desktop/bash/score_result/calculate_score.py