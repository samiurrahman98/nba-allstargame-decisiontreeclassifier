import csv

def get_player_identifiers(infile):
    with open(infile, mode='r', encoding='utf-8-sig') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        player_identifiers = []
        for row in enumerate(reader):
            player_identifiers.append(row[1][0])
    return player_identifiers

def get_player_data(infile):
    player_data = []
    with open(infile, mode='r', encoding='utf-8-sig') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        for row in enumerate(reader):
            player_data.append(row)
    return player_data