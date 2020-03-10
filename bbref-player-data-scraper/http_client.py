import requests
from lxml import html

from errors import InvalidPlayerAndSeason
from html import PlayerSeasonBoxScoresPage
from parsers import PlayerSeasonAveragesWithinDateRangeParser

BASE_URL = 'https://www.basketball-reference.com'

def regular_season_player_averages_within_date_range(player_identifier, season_end_year, from_date, to_date):
    # Makes assumption that basketball reference pattern of breaking out player pathing using first character of
    # surname can be derived from the fact that basketball reference also has a pattern of player identifiers
    # starting with first few characters of player's surname
    url = '{BASE_URL}/players/{player_surname_starting_character}/{player_identifier}/gamelog/{season_end_year}'.format(
        BASE_URL=BASE_URL,
        player_surname_starting_character=player_identifier[0],
        player_identifier=player_identifier,
        season_end_year=season_end_year,
    )

    response = requests.get(url=url, allow_redirects=False)
    response.raise_for_status()

    page = PlayerSeasonBoxScoresPage(html=html.fromstring(response.content))
    if page.regular_season_box_scores_table is None:
        raise InvalidPlayerAndSeason(player_identifier=player_identifier, season_end_year=season_end_year)

    return PlayerSeasonAveragesWithinDateRangeParser.parse(box_scores=page.regular_season_box_scores_table.rows, from_date=from_date, to_date=to_date)