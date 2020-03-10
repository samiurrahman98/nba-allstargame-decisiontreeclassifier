import requests

from dateutil.parser import parse as du_parse
import http_client
from errors import InvalidPlayerAndSeason
from output import output
from writers import CSVWriter, RowFormatter, \
    PLAYER_SEASON_AVERAGES_WITHIN_DATE_RANGE_COLUMN_NAMES

def regular_season_player_averages_within_date_range(player_identifier, season_end_year, from_date, to_date, output_type=None, output_file_path=None,
                                     output_write_option=None, json_options=None):
    
    try:
        values = http_client.regular_season_player_averages_within_date_range(
            player_identifier=player_identifier,
            season_end_year=season_end_year,
            from_date=du_parse(from_date),
            to_date=du_parse(to_date)
        )
    except requests.exceptions.HTTPError as http_error:
        if http_error.response.status_code == requests.codes.internal_server_error \
                or http_error.response.status_code == requests.codes.not_found:
            raise InvalidPlayerAndSeason(player_identifier=player_identifier, season_end_year=season_end_year)
        else:
            raise http_error
    return output(
        values=values,
        output_type=output_type,
        output_file_path=output_file_path,
        output_write_option=output_write_option,
        csv_writer=CSVWriter(
            column_names=PLAYER_SEASON_AVERAGES_WITHIN_DATE_RANGE_COLUMN_NAMES,
            row_formatter=RowFormatter(data_field_names=PLAYER_SEASON_AVERAGES_WITHIN_DATE_RANGE_COLUMN_NAMES)
        ),
        json_options=json_options,
    )