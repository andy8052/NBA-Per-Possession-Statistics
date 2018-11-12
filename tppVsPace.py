import csv

teams = []
average = 14.1
seconds = 2880

with open('TimePerPossession - Offense.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    skip = 0
    teamCount = 0
    for row in csv_reader:
        if skip < 2 or teamCount == 30:
            skip += 1;
        else:
            teams.append({"team": row[1], "time": float(row[4])})
            teamCount += 1
print("team,tpp")
for team in teams:
    name = team["team"]
    tpp = team["time"]
    # print(f'The {name} avg {tpp} seconds per possession')

    avgTpp = (tpp + average)/2
    pace = (seconds/avgTpp)/2
    # print(f'The {name} have a TPP pace of {pace}')
    print(f'{name},{pace}')
