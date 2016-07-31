print "You enter a dark room with two doors.Do you go trhough #1 or door #2?"

door = raw_input('>')

if door == "1":
 print "there is a giant bear here eating a cheese cake what do you do?"
 print "1. take the cake"
 print "2. scream at th bear"
 
 bear = raw_input('>')
 if bear== "1":
  print "The bear eats your face off.Good Job!"
 elif bear == "2":
  print "the bear eats your legs off Good Job!"
 else:
  print "well doing %s is probably better . Bear runs away" %bear
  
  
elif door == "2":
  print "you stare into the endless abyss at Cthulhu's retina"
  print "1. Blueberies"
  print "2. Yellow jacket clothespins"
  print "3. Understanind revolvers yelling melodies"
  
  insanity = raw_input('>')
  
  if insanity == "1" or insanity == "2":
    print "your body survives by a mind of jello.Good Job"
  else:
   print "The insanity rots your eye int a pool of muck Good job!"
   
else:
 print "you stumble arond and fall on a knife and die Good job"
