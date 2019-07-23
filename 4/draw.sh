set terminal png
set output '../graph.png'

set autoscale

set title "Process time of Sorting algorithms"
set style data linespoints

plot "p.dat" using 1:2 title "Pyramid sort", \
     "m.dat" using 1:2 title "Merge sort", \
     "q.dat" using 1:2 title "Quick sort", \
     "b.dat" using 1:2 title "Bubble sort", \
