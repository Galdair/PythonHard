from sys import argv
from os.path import exists

script ,from_file , to_file = argv

print "Copying from %s to %s" %(from_file,to_file)

indata =open(from_file).read()
print "the input file is %d bytes long" %len(indata)

print "does the output file exists? %r" %exists(to_file)
print"Ready hit RETURN to continue CTR-C to abort"
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)
print "Alrigth ,all done"

out_file.close()