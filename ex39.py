#create a mapping if state to abbreveation
states = {
    "Oregon":'OR',
    "Florida": 'FL',
    "California":'CA',
    "New York": 'NY',
    "Michigan": 'MI'
}

#create a basic set of states and cities in them
cities = {
    'CA': "San Francisco",
    'MI': "Detroit",
    'FL': "Jacksonsville"
}

#add some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreveation is: ", states["Florida"])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

#print every states abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every sity in state
print('-' * 10)
for abbrev, city in list(cities.items())
print('-' * 10)
for state, abbrev in list(states.item()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]})

print('-' * 10)
#safely get a abbtrbietion by state that might not be there
state = states.get("Texas")
if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city fot the state "TX" is: {city})
