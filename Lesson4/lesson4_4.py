import sys
filename = sys.argv[0]
f = open(filename, 'r') 
for line in f: 
	enil=line [::-1]
	print(enil)
f.close()