tournamentName = input('Enter the tournament name: ')

playerFirstNames = []
playerSurnames = []
playerRatings = []
playerSchools = []
playerSexes = []
playerYOB = []

# easy way to store player details is a file
playerData = open('playerDetails.csv', 'wt')
# add columns
playerData.write('first_name, surname, rating, school, sex, year_of_birth' +
                 '\n')
playerData.close()

playerData = open('playerDetails.csv', 'a')

arbiters = []
numArbiters = input('Enter how many arbiters there are in the tournament: ')
for i in range(0, int(numArbiters)):
    arbiters.append(input('Enter the name of the arbiter: '))

sections = []
numSections = input('Enter how many sections there are in the tournament: ')
for i in range(0, int(numSections)):
    sections.append(input('Enter the name of the tournament section: '))
    numPlayers = input('Enter how many players there are in this section: ')
    for count in range(0, int(numPlayers)):
        playerFirstNames.append(input('Enter the first name of a player: '))
        playerSurnames.append(input('Enter ' + playerFirstNames[count] + "'s surname: "))
        playerRatings.append(input('Enter ' + playerFirstNames[count] + "'s rating: "))
        playerSchools.append(input('Enter ' + playerFirstNames[count] + "'s school: "))
        playerSexes.append(input('Enter ' + playerFirstNames[count] + "'s sex: "))
        playerYOB.append(input('Enter ' + playerFirstNames[count] + "'s year of birth: "))
        playerDetails = [playerFirstNames[count], playerSurnames[count],
                         playerRatings[count], playerSchools[count],
                         playerSexes[count], playerYOB[count]]
        # doesn't work with list AND txt
        playerData.write(str(playerDetails) + '\n')
        print(playerDetails)

playerData.close()

print(tournamentName)
print(arbiters)
print(sections)
print()
print()