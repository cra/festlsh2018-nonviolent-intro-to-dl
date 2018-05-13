#!/usr/bin/gnuplot -persist
set border 3 front lt black linewidth 1.000 dashtype solid
set xdata time
set format x "%Y" timedate
set format y "% h"
set timefmt "%Y-%m"
unset grid
set theta counterclockwise right
set style parallel front  lt black linewidth 2.000 dashtype solid
set key title "" center
set key fixed center top vertical Right noreverse enhanced autotitle nobox
set key noinvert samplen 4 spacing 1 width 0 height 0

set xtics border in scale 1,0.5 nomirror norotate  autojustify
set ytics border in scale 1,0.5 nomirror norotate  autojustify

set xrange [ "2004-01" : "2018-05" ]

set locale "en_US.UTF-8"

set term svg
set output "trends.svg"
DATAFILE="multiTimeline.csv"
plot DATAFILE skip 4 u 1:2 title 'Deep Learning'    with lines lw 3 linecolor "#E4A1C", \
     DATAFILE skip 4 u 1:3 title "Machine Learning" with lines      linecolor "#984EA3",\
     DATAFILE skip 4 u 1:4 title "Artificial Intelligence" w l lc "#FF7F00"
