rm -f mc.o
gcc p.c -o mc.o
clear
time for i in {1..100}; do ./mc.o; done
