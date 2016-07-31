from sys import argv

script ,user_name = argv 
prompt = '>'

print "Hi %s I'm %s script" %(user_name,script)
print "I'd like to aska  few questions"
print "do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have"
coputer = raw_input(prompt)

print """
alrigth ,so you said %r about liking me.
you live in %r . Not sure where is that.
And you have a %r computer .Nice.
""" % (likes,lives,coputer)

