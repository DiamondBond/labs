f = open("a.log", "w")
for n in range(4*1000*1000):
    k = 120-n%100
    f.write(str(n+1)+' '+chr(k%26+ord('a'))*k+'\n')
