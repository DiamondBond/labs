echo "cleaning..."
rm -f a.o
echo "compiling..."
gcc primes.c -o a.o
echo "running..."
clear
time for i in {1..100}; do ./a.o; done
