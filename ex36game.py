def end_room():
  print "you ahve entered the treasure room"
  print "Do you attempt to take the gold"
  print "Do you take the small coin or the big coin or nothing"
  while (True):
   choice = raw_input('>')
   if "small" in choice:
    print "you win,take your prize"
    exit(0)
   elif "big" in choice:
     dead("you are too greedy")
   elif "nothing" in choice:
    print "take your nothing you humble servant and you shall not return"
    exit(0)
   else:
		   print "I can't understand you try again"
		   
		   
		   
def dead(how):
   print "Sorry you are sooo dead becouse",how
   exit(0)
   
def first_room():
    print "you have entered the first room"
    print "you see scar face staring at you with a shotgun"
    print "what do you do?Shoot him with a magic bullet you just found or you try to reason with him,or you flee away?"
    while (True):
	   choice = raw_input('>')
	   if "shoot" in choice:
	    dead('Scar face alway shoots first')
	   elif "reason" in choice:
	     dead("you can't reason with scarface")
	   elif "flee" in choice:
	     end_room()
	   else:
		   print "I can't understand you try again"	 
def second_room():
    print "you enter into the second room,but you see nothing only the deep chasm before you"
    print "what dou you do?Kill yourself?step into the chasm?"
    while (True):
	    choice = raw_input('>')
	    if "kill" in choice:
		   dead("you are a coward")
	    elif "step" in choice:
		    end_room()
	    else:
		   print "I can't understand you try again"
def control_room():
 print "you ahve woken up ina strange dimly lit room with two very strange and pulsing door"
 print "what dou you choose door number one or number two?"
 while (True):
   choice = raw_input('>')
   if "one" in choice:
		    first_room()
   elif "two" in choice:
		   second_room()
   else:
		  print "please answer one or two"
		  
	 
control_room()