
def while_stacker(max):
	i = 0
	numbers = []
	while i < max:
	   print "At the top i is %d " %i
	   numbers.append(i)
	   
	   i += 1
	   print "numbers now: ",numbers
	   print "at the bottom i is %d" %i
	   
	print "the numbers"

	for num in numbers:
	   print num
	   

  
while_stacker(120)