import csv

offense = {}
defense = {}
average = 14.1
seconds = 2880

games = [{'home': 'CHA', 'away': 'DET'},
         {'home': 'IND', 'away': 'HOU'},
         {'home': 'ORL', 'away': 'NYK'},
         {'home': 'MIL', 'away': 'DEN'},
         {'home': 'BOS', 'away': 'POR'},
         {'home': 'ATL', 'away': 'LAL'}]

with open('TimePerPossession - Offense.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    skip = 0
    teamCount = 0
    for row in csv_reader:
        if skip < 2 or teamCount == 30:
            skip += 1;
        else:
            offense[row[1]] = {"time": float(row[4]), "points": float(row[6])}
            teamCount += 1

with open('TimePerPossession - Defense.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    skip = 0
    teamCount = 0
    for row in csv_reader:
        if skip < 2 or teamCount == 30:
            skip += 1;
        else:
            defense[row[1]] = {"points": float(row[6])}
            teamCount += 1

for game in games:
    home = game["home"]
    away = game["away"]
    print(f'The {home} avg {offense[home]["time"]} seconds per possession')
    print(f'The {away} avg {offense[away]["time"]} seconds per possession')

    avg = (offense[home]['time'] + offense[away]['time'])/2

    if avg > offense[home]['time']:
        dif = ((offense[home]['time'] - avg) / offense[home]['time']) * 100
        print(f'The {home} possessions should be {dif}% of normal')

        dif = ((offense[away]['time'] - avg) / offense[away]['time']) * 100
        print(f'The {away} possessions should be {dif}% of normal')

    else:
        dif = ((avg - offense[home]['time']) / offense[home]['time']) * 100
        print(f'The {home} possessions should be {dif}% of normal')

        dif = ((avg - offense[away]['time']) / offense[away]['time']) * 100
        print(f'The {away} possessions should be {dif}% of normal')

    possessionsPerTeam = (seconds / avg)/2
    print(f'This model projects {possessionsPerTeam} possessions per team')

    print(f'The {home} avg {offense[home]["points"]} points per possession and allow {defense[home]["points"]} points per possession')
    print(f'The {away} avg {offense[away]["points"]} points per possession and allow {defense[away]["points"]} points per possession')

    homePPP = (offense[home]["points"] + defense[away]["points"])/2
    awayPPP = (offense[away]["points"] + defense[home]["points"])/2

    print(f'This projects {home} to score {possessionsPerTeam * homePPP}')
    print(f'This projects {away} to score {possessionsPerTeam * awayPPP} \n')
