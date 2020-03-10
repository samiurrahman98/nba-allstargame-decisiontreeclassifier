import sys
import csv
import pandas as pd
import readers
import client
import numpy as np
from data import ApplicationMode, PlayerPositions
from errors import InvalidMode, InvalidNumberOfArguments, InvalidPlayerPosition
from utilities import get_minutes
import pprint

def fetch_all_star_player_data(starters, reserves, top_100, season_end_year, from_date, starters_to_date, reserves_top_100_to_date):
    output_file_path = '../' + str(season_end_year) + '/' + str(season_end_year) + '.csv'

    player_identifiers_starters = readers.get_player_identifiers(starters)
    header = True
    for player_identifier in player_identifiers_starters:
        player_data = client.regular_season_player_averages_within_date_range(player_identifier=player_identifier,
                                                                                season_end_year=season_end_year,
                                                                                from_date=from_date,
                                                                                to_date=starters_to_date)
        df = pd.DataFrame(player_data)
        games_played = df.shape[0]
        series = df.mean()
        df2 = pd.DataFrame(series).T
        field_goal_percentage = round(df2.loc[0, 'FGM'] / df2.loc[0, 'FGA'], 3) if df2.loc[0, 'FGA'] > 0 else np.NaN
        three_point_percentage = round(df2.loc[0, '3PM'] / df2.loc[0, '3PA'], 3) if df2.loc[0, '3PA'] > 0 else np.NaN
        free_throw_percentage = round(df2.loc[0, 'FTM'] / df2.loc[0, 'FTA'], 3) if df2.loc[0, 'FTA'] > 0 else np.NaN
        df2 = df2.round(1)
        df2.loc[0, 'MP'] = round(get_minutes(df2.loc[0, 'MP']), 2)

        df2.insert(loc=(df2.columns.get_loc('FGA') + 1), column='FG%', value=field_goal_percentage)
        df2.insert(loc=(df2.columns.get_loc('3PA') + 1), column='3P%', value=three_point_percentage)
        df2.insert(loc=(df2.columns.get_loc('FTA') + 1), column='FT%', value=free_throw_percentage)
        df2.insert(loc=0, column='Player Identifier', value=player_identifier)
        df2.insert(loc=1, column='Position', value='')
        df2.insert(loc=2, column='GP', value=games_played)
        df2.insert(loc=len(df2.columns), column='Classification', value='Selected')
        mode = 'w+' if header else 'a'
        df2.to_csv(output_file_path, index=False, mode=mode, header=header)
        header = False

    player_identifiers_reserves = readers.get_player_identifiers(reserves)

    for player_identifier in player_identifiers_reserves:
        player_data = client.regular_season_player_averages_within_date_range(player_identifier=player_identifier,
                                                                                season_end_year=season_end_year,
                                                                                from_date=from_date,
                                                                                to_date=reserves_top_100_to_date)

        df = pd.DataFrame(player_data)
        games_played = df.shape[0]
        series = df.mean()
        df2 = pd.DataFrame(series).T
        field_goal_percentage = round(df2.loc[0, 'FGM'] / df2.loc[0, 'FGA'], 3) if df2.loc[0, 'FGA'] > 0 else np.NaN
        three_point_percentage = round(df2.loc[0, '3PM'] / df2.loc[0, '3PA'], 3) if df2.loc[0, '3PA'] > 0 else np.NaN
        free_throw_percentage = round(df2.loc[0, 'FTM'] / df2.loc[0, 'FTA'], 3) if df2.loc[0, 'FTA'] > 0 else np.NaN
        df2 = df2.round(1)
        df2.loc[0, 'MP'] = round(get_minutes(df2.loc[0, 'MP']), 2)

        df2.insert(loc=(df2.columns.get_loc('FGA') + 1), column='FG%', value=field_goal_percentage)
        df2.insert(loc=(df2.columns.get_loc('3PA') + 1), column='3P%', value=three_point_percentage)
        df2.insert(loc=(df2.columns.get_loc('FTA') + 1), column='FT%', value=free_throw_percentage)
        df2.insert(loc=0, column='Player Identifier', value=player_identifier)
        df2.insert(loc=1, column='Position', value='')
        df2.insert(loc=2, column='GP', value=games_played)
        df2.insert(loc=len(df2.columns), column='Classification', value='Selected')
        mode = 'w+' if header else 'a'
        df2.to_csv(output_file_path, index=False, mode=mode, header=header)

    player_identifiers_top_100 = readers.get_player_identifiers(top_100)

    for player_identifier in player_identifiers_top_100:
        player_data = client.regular_season_player_averages_within_date_range(player_identifier=player_identifier,
                                                                                season_end_year=season_end_year,
                                                                                from_date=from_date,
                                                                                to_date=reserves_top_100_to_date)

        df = pd.DataFrame(player_data)
        games_played = df.shape[0]
        series = df.mean()
        df2 = pd.DataFrame(series).T
        field_goal_percentage = round(df2.loc[0, 'FGM'] / df2.loc[0, 'FGA'], 3) if df2.loc[0, 'FGA'] > 0 else np.NaN
        three_point_percentage = round(df2.loc[0, '3PM'] / df2.loc[0, '3PA'], 3) if df2.loc[0, '3PA'] > 0 else np.NaN
        free_throw_percentage = round(df2.loc[0, 'FTM'] / df2.loc[0, 'FTA'], 3) if df2.loc[0, 'FTA'] > 0 else np.NaN
        df2 = df2.round(1)
        df2.loc[0, 'MP'] = round(get_minutes(df2.loc[0, 'MP']), 2)

        df2.insert(loc=(df2.columns.get_loc('FGA') + 1), column='FG%', value=field_goal_percentage)
        df2.insert(loc=(df2.columns.get_loc('3PA') + 1), column='3P%', value=three_point_percentage)
        df2.insert(loc=(df2.columns.get_loc('FTA') + 1), column='FT%', value=free_throw_percentage)
        df2.insert(loc=0, column='Player Identifier', value=player_identifier)
        df2.insert(loc=1, column='Position', value='')
        df2.insert(loc=2, column='GP', value=games_played)
        df2.insert(loc=len(df2.columns), column='Classification', value='Not selected')
        mode = 'w+' if header else 'a'
        df2.to_csv(output_file_path, index=False, mode=mode, header=header)

def fetch_date_range_restricted_player_data(player_identifiers, season_end_year, from_date, to_date):
    output_file_path = '../' + str(season_end_year) + '/' + str(season_end_year) + '-custom.csv'
    player_identifiers = readers.get_player_identifiers(player_identifiers)
    for player_identifier in player_identifiers:
        player_data = client.regular_season_player_averages_within_date_range(player_identifier=player_identifier, season_end_year=season_end_year,
                                                        from_date=from_date, to_date=to_date)
        df = pd.DataFrame(player_data)
        games_played = df.shape[0]
        series = df.mean()
        df2 = pd.DataFrame(series).T
        field_goal_percentage = round(df2.loc[0, 'FGM'] / df2.loc[0, 'FGA'], 3) if df2.loc[0, 'FGA'] > 0 else np.NaN
        three_point_percentage = round(df2.loc[0, '3PM'] / df2.loc[0, '3PA'], 3) if df2.loc[0, '3PA'] > 0 else np.NaN
        free_throw_percentage = round(df2.loc[0, 'FTM'] / df2.loc[0, 'FTA'], 3) if df2.loc[0, 'FTA'] > 0 else np.NaN
        df2 = df2.round(1)
        df2.loc[0, 'MP'] = round(get_minutes(df2.loc[0, 'MP']), 2)

        df2.insert(loc=(df2.columns.get_loc('FGA') + 1), column='FG%', value=field_goal_percentage)
        df2.insert(loc=(df2.columns.get_loc('3PA') + 1), column='3P%', value=three_point_percentage)
        df2.insert(loc=(df2.columns.get_loc('FTA') + 1), column='FT%', value=free_throw_percentage)
        df2.insert(loc=0, column='Player Identifier', value=player_identifier)
        df2.insert(loc=1, column='GP', value=games_played)
        df2.to_csv(output_file_path, index=False, mode='w+', header=True)

def separate_players_by_position(path):
    players = {}
    players[PlayerPositions.GUARD.value] = players[PlayerPositions.FORWARD.value] = players[PlayerPositions.POINT_FORWARD.value] = players[PlayerPositions.CENTER.value] = []
    player_data = readers.get_player_data(path)
    read_columns = False
    columns = None
    for data_tuple in player_data:
        if not read_columns:
            columns = data_tuple[1]
            read_columns = True
        else:
            player = data_tuple[1]
            player_position = player[0]
            if player_position == PlayerPositions.GUARD.value:
                players[PlayerPositions.GUARD.value].append(player)
            elif player_position == PlayerPositions.FORWARD.value:
                players[PlayerPositions.FORWARD.value].append(player)
            elif player_position == PlayerPositions.POINT_FORWARD.value:
                players[PlayerPositions.POINT_FORWARD.value].append(player)
            elif player_position == PlayerPositions.CENTER.value:
                players[PlayerPositions.CENTER.value].append(player)
            else:
                raise InvalidPlayerPosition(player_position)
    
    for key in players:
        output_file_path = '../position-divided-player-data/' + key + '.csv'
        with open(output_file_path, mode='w+', newline='', encoding='utf-8-sig') as output_file:
            writer = csv.writer(output_file, delimiter=',')
            writer.writerow(columns)
            for row in players[key]:
                if row[0] == key:
                    writer.writerow(row)

def main(mode, args):
    if mode == ApplicationMode.ALL_STAR.value:
        if len(args) == ApplicationMode.ALL_STAR_NUM_ARGS.value:
            fetch_all_star_player_data(starters=args[0], reserves=args[1], top_100=args[2], season_end_year=args[3],
                                        from_date=args[4], starters_to_date=args[5], reserves_top_100_to_date=args[6])
        else:
            raise InvalidNumberOfArguments(ApplicationMode.ALL_STAR_NUM_ARGS.value)
    elif mode == ApplicationMode.DATE_RANGE.value:
        if len(args) == ApplicationMode.DATE_RANGE_NUM_ARGS.value:
            fetch_date_range_restricted_player_data(player_identifiers=args[0], season_end_year=args[1], from_date=args[2],
                                                    to_date=args[3])
        else:
            raise InvalidNumberOfArguments(ApplicationMode.DATE_RANGE_NUM_ARGS.value)
    elif mode == ApplicationMode.SEPARATE_PLAYERS_BY_POSITION.value:
        if len(args) == ApplicationMode.SEPARATE_PLAYERS_BY_POSITION_NUM_ARGS.value:
            separate_players_by_position(path=args[0])
        else:
            raise InvalidNumberOfArguments(ApplicationMode.SEPARATE_PLAYERS_BY_POSITION_NUM_ARGS.value)
    else:
        raise InvalidMode(mode)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])