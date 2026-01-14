'''
This is a simple birthday paradox program that predicts how
many people will have the same birthday as each other in a group
that is no bigger than 100

'''

import datetime, random

def getBirthdays(numberOfBirthdays):
    # Returns the list of number random date objects for birthdays
    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        # Getting a random day in the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    # Returns the date object for the birthdays that occur more than once
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique and nothing else is needed
    
    # Compare each birthday to every other birthday
    for A, birthdayA in enumerate(birthdays):
        for B, birthdayB in enumerate(birthdays[A + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # return the matching birthday
            
# Displaying the intro for the game
print('''
    The Birthday Paradox shows us that in a group of M people,
    the odds that two of them have matching birthdays is surprisingly
    large. This program does a Monte Carlo simulation (that is, repeated
    random simulations) to explore this concept.
      
    (It is not actually a paradox, its just a surprising result)
''')

# Set up the tuple of months in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Keep asking until the user enters a valid argument
while True:
    print('How many birthdays shall I generate? (max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount
print()

# Generate and display the birthdays
print('Here are ', numBDays, 'birthdays!')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

# Determining if two birthdays do match
match = getMatch(birthdays)

# Displaying results
print('In this simulation, ', end='')

if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Multiple people have the same birthday on ', dateText)
else:
    print('There are no matching birthdays')
print()

# Running through 100,000 simulations
print('Generating ', numBDays, ' random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # The number of matches within the simulation

for i in range(100000):
    # Reporting on the proress every 10,000 simulations
    if i % 10000 == 0:
        print(i, ' Simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000  simulations run')

# Display the simulation results
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of ', numBDays, ' people, there was a ')
print('matching birthday in that group', simMatch, ' times. This means')
print('that', numBDays, ' people have a ', probability, 'percent chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')