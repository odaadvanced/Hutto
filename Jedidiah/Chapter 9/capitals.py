import random

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Iowa': 'Des Moines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson',
'Missouri': 'Jefferson City',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada': 'Carson City',
'New Hampshire': 'Concord',
'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe',
'New York': 'Albany',
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont': 'Montpelier',
'Virginia': 'Richmond',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne',
}

list_of_states = []
for key in capitals_dict:
    list_of_states.append(key)

state = random.choice(list_of_states)
capital = capitals_dict[state]
user_answer = input(f"The state is {state}. Please enter the capital: ")
while user_answer.lower() != capital.lower():
    if user_answer.lower() == 'exit':
        print(capital)
        print("Goodbye")
        break
    else:    
        user_answer = input(f"The state is {state}. Please enter the capital: ")
if user_answer.lower() == capital.lower():
    print("Correct")
    