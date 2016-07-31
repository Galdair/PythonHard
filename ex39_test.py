import hashmapmy

states = hashmapmy.new()
hashmapmy.set(states,'Oregon','OR')
hashmapmy.set(states,'Flroida','FL')
hashmapmy.set(states,'California','CA')
hashmapmy.set(states,'New York','NY')
hashmapmy.set(states,'Michigan','MI')

cities = hashmapmy.new()
hashmapmy.set(cities,'CA','San Francisco')
hashmapmy.set(cities,'MI','Detroit')
hashmapmy.set(cities,'FL','Jacksonville')

hashmapmy.set(cities,'NY','New York')
hashmapmy.set(cities,'OR','Portland')

print '-' * 10
print "NY state has %s" %hashmapmy.get(cities,'NY')
print "OR states has %s" %hashmapmy.get(cities,'OR')

print '-' * 10
print "Michigan has: %s" % hashmapmy.get(cities,hashmapmy.get(states,'Michigan'))
print "Florida has: %s" % hashmapmy.get(cities,hashmapmy.get(states,'Florida'))

print '-' * 10
hashmapmy.list(states)

print '-' * 10
hashmapmy.list(cities)

print '-' * 10
state = hashmapmy.get(states,'Texas')

if not state:
  print "Sorry ,no texas"

city = hashmapmy.get(cities,'TX','Does not Exist')
print "The city for the state TX is %s" % city
