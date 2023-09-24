from secrets import randbits
def gen_hamming(x):
    x = [x>>3,x>>2&1,x>>1&1,x&1]
    p1 = x[0] ^ x[1] ^ x[3]
    p2 = x[0] ^ x[2] ^ x[3]
    p4 = x[1] ^ x[2] ^ x[3]
    p8 = x[0] ^ x[1] ^ x[2]
    bits = [p1,p2,x[0],p4,x[1],x[2],x[3],p8]
    if randbits(2) != 0:
        bits[randbits(3)] ^= 1
    return ''.join(map(str,bits))
    
def transmit(m,fout):
    for c in m:
        fout.write(gen_hamming(ord(c)>>4)+'\n')
        fout.write(gen_hamming(ord(c)&0xf)+'\n')
fout = open("output.txt","w")
transmit(open("flag.txt").read(),fout)
