states = {
 'oregon' :'OR',
 'Florida' : 'FL',
 'California' :'CA',
 'New York':'NY',
 'Michigan' : 'MI'
}

cities = {
  'CA' :'San Francisco',
  'MI' :'Detroit',
  'FL' : 'Jacksonville'


}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY state has ",cities['NY']
print "OR state has",cities['OR']

print '-' *10
print "Michigan's abbrevation is",states["Michigan"]
print "Florida abbreviation is",states['Florida']

print '-' *10
print "michigan has",cities[states['Michigan']]
print "Florida has ",cities[states["Florida"]]

print '-' *10
for state,abbrev in states.items():
   print "%s is abbreviated %s" %(state,abbrev)
   
print '-' *10
for abbrev ,city in cities.items():
   print"%s has the city %s" %(abbrev,city)
print '-' *10
for state,abbrev in states.items():
   print "%s state is abreviated %s and has the city %s" %(state,abbrev,cities[abbrev])
   
print '-' *10
state = states.get('Texas')

if not state:
 print "sorry no texas"
 
 
city = cities.get('TX','Does not exist')
print "the city for the state 'TX' is %s" %city

