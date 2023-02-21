captains = {}
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'

if 'Enterprise' in captains:
    print(captains['Enterprise'])
else:
    captains['Enterprise'] = 'unknown'

if 'Discovery' in captains:
    print(captains['Discovery'])
else:
    captains['Discovery'] = 'unkown'

for ship in captains:
    print(f"The {ship} is captained by {captains[ship]}")

del captains['Discovery']

other_captains_dictionary = dict()
other_captains_dictionary['Enterprise'] = 'Picard'
other_captains_dictionary['Voyager'] = 'Janeway'
other_captains_dictionary['Defiant'] = 'Sisko'