clean:
	rm -f *.o
	rm -f *.out

ack:
	gcc ack.c -o ack.o

ack_c:
	gcc ack_cache.c -o ack_c.o
primes:
	gcc prime.c -o primes.o

fb:
	gcc fizzbuzz.c -o fb.o

mc:
	gcc p.c -o mc.o
