x = "there are %d types of people" %10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" %(binary,do_not)

print x
print y

print "i said %r"%x
print "i also said '%s' ."%y

hilarious = False
joke_evaluation = "isn't that joke funny?! %r"
#fills in the '%r' in joke_evaluation
print joke_evaluation %hilarious
#joins strings
w = "hit is the left side of "
e = " a string with a rigth side"

print w+e
