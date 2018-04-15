import struct
import sys

class unpack:
	def __init__(self):
		self.toc = struct.Struct(">4sI")
		self.layer1 = struct.Struct(">256I")
		self.layer2 = struct.Struct("20s")
		self.layer3 = struct.Struct("4s")
		self.layer4 = struct.Struct(">I")

	def Toc(self,f):
		buf = f.read(8)
		r,version = self.toc.unpack(buf)
		return r[1:],version

	def L1(self,f):
		buf = f.read(256*4)
		return self.layer1.unpack(buf)

	def L2(self,f):
		buf = f.read(20)
		r, = self.layer2.unpack(buf)
		return r.encode('hex')
	def L3(self,f):
		buf = f.read(4)
		r, = self.layer3.unpack(buf)
		return r.encode('hex')
	def L4(self,f):
		buf = f.read(4)
		r, = self.layer4.unpack(buf)
		return r

def main():
	gitidx = unpack()

	f = open(sys.argv[1])
	f3 = open(sys.argv[1])
	f4 = open(sys.argv[1])

	t,v = gitidx.Toc(f)
	print "Toc",t,"version",v

	idx = list(gitidx.L1(f))
	# print idx
	total = idx[-1]
	f3.seek(8+256*4+total*20)
	f4.seek(8+256*4+total*24)
	
	for n in range(len(idx)):
		if n==0:
			s = 0
		else:
			s = idx[n-1]
		print "hash begin with",hex(n)
		for i in range(idx[n]-s):
			hash = gitidx.L2(f)
			crc = gitidx.L3(f3)
			off = gitidx.L4(f4)
			if i==0:
				print hash,crc,off

	# for n in range(len(idx)):
	# 	if n==0:
	# 		s = 0
	# 	else:
	# 		s = idx[n-1]
	# 	print "crc",hex(n)
	# 	for i in range(idx[n]-s):
	# 		crc = gitidx.L3(f)
	# 		if i==0:
	# 			print crc

	# for n in range(len(idx)):
	# 	if n==0:
	# 		s = 0
	# 	else:
	# 		s = idx[n-1]
	# 	print "off",hex(n)
	# 	for i in range(idx[n]-s):
	# 		off = gitidx.L4(f)
	# 		if i==0:
	# 			print off




if __name__ == '__main__':
	main()

