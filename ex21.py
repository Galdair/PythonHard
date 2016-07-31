def add(a,b):
 print "adding %d + %d " %(a ,b)
 return a+b
def substract (a,b):
 print "substracting %d - %d " %(a ,b)
 return a-b
 
def multiply (a,b):
 print "multiplying %d * %d" %(a,b)
 return a*b
 
def divide(a,b):
 print "dividing %d / %d" %(a,b)
 return a/b

print "let's do some maths with just functions"

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d ,Height: %d ,Weight: %d ,IQ: %d " %(age,height,weight,iq)

print "here is a puzzle"

what = add(age,substract(height,multiply(weight,divide(iq,2))))
my_answer = 35+(74-(25*180))
print "is what equals to my calculations?", what == my_answer