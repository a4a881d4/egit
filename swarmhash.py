import sha3
import struct
import sys
import os
def fsize(filename):
	st = os.stat(filename)
	return st.st_size

f = open(sys.argv[1])
lf = struct.Struct("<q")

k = sha3.keccak_256()
k.update(lf.pack(fsize(sys.argv[1])))
k.update(f.read())
f.close()
print k.hexdigest()
