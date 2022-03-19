echo "cleaning..."
rm -f ack.o
echo "compiling..."
gcc ack.c -o ack.o
echo "running..."
clear
time ./ack.o
