time for i in {1..100}; do
rm -f a.o
gcc -O2 primes.c -o a.o
echo "running..."
./a.o
done
