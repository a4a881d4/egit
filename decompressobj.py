import zlib
import sys

f = open(sys.argv[1])

print repr(zlib.decompress(f.read()))

