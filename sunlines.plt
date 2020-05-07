set datafile separator ','
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S.%ns"
set format x "%d %H:%M:%S"
plot \
    ARG1 using 2:1 with lines lw 4 title 'Flight', \
    ARG1 using 3:1 with lines lw 3 lc rgb 'yellow' title 'SunRise', \
    ARG1 using 4:1 with lines lw 3 lc rgb 'red' title 'SunSet', \
    ARG1 using 5:1 with lines lw 3 lc rgb 'yellow' title 'SunRise + 1d', \
    ARG1 using 6:1 with lines lw 3 lc rgb 'red' title 'SunSet + 1d'

pause 5
reread
