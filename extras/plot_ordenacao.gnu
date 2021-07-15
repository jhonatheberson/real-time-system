# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
# set output 'histograms.1.png'
set key fixed right top vertical Right noreverse noenhanced autotitle nobox
set datafile missing '-'
set style data linespoints
set xtics border in scale 1,0.5 nomirror rotate by -45  autojustify
set xtics  norangelimit 
set xtics   ()
set xlabel "Tamanho do vetor"
set ylabel "Clocks"
set title "Analise experimental de complexidade de algortimos de ordenação por numeros de clock" 
set xrange [ * : * ] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [ * : * ] noreverse writeback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback
NO_ANIMATION = 1
## Last datafile plotted: "immigration.dat"
plot 'results_long.dat' using 2:xtic(1) title  'ClockQuickSort', for [i=3:6] '' using i title 'ClockBubbleSort'