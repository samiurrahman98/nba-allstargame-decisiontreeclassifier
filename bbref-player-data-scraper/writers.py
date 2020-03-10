import csv
import json

from utilities import merge_two_dicts

# I wrote the explicit mapping of CSV values because there didn't seem to be a way of outputting the values of enums
# without doing it this way

PLAYER_SEASON_AVERAGES_WITHIN_DATE_RANGE_COLUMN_NAMES = [
    "MP",
    "FGM",
    "FGA",
    "3PM",
    "3PA",
    "FTM",
    "FTA",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "GmSc",
    "+/-"
    ]
    
class WriteOptions:
    def __init__(self, file_path=None, mode=None, custom_options=None):
        self.file_path = file_path
        self.mode = mode
        self.custom_options = custom_options

    def should_write_to_file(self):
        return self.file_path is not None and self.mode is not None

    def __eq__(self, other):
        if isinstance(other, WriteOptions):
            return self.file_path == other.file_path \
                   and self.mode == other.mode \
                   and self.custom_options == other.custom_options
        return False


class JSONWriter:
    DEFAULT_OPTIONS = {
        "sort_keys": True,
        "indent": 4,
    }

    def __init__(self, encoder):
        self.encoder = encoder

    def write(self, data, options):
        output_options = self.DEFAULT_OPTIONS \
            if options.custom_options is None \
            else merge_two_dicts(
                first=self.DEFAULT_OPTIONS,
                second=options.custom_options
            )

        if options.should_write_to_file():
            with open(options.file_path, options.mode.value, newline="") as json_file:
                return json.dump(data, json_file, cls=self.encoder, **output_options)

        return json.dumps(data, cls=self.encoder, **output_options)


class CSVWriter:
    def __init__(self, column_names, row_formatter):
        self.column_names = column_names
        self.row_formatter = row_formatter

    def write(self, data, options):
        with open(options.file_path, options.mode.value, newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column_names)
            writer.writeheader()
            writer.writerows([self.row_formatter.format(row_data) for row_data in data])


class RowFormatter:
    def __init__(self, data_field_names):
        self.data_field_names = data_field_names

    def format(self, row_data):
        return {
            data_field_name: row_data[data_field_name].value
            if data_field_name in [
                "away_team",
                "home_team",
                "team",
                "location",
                "opponent",
                "outcome",
                "relevant_team",
                "period_type",
            ]
            else "-".join(map(lambda position: position.value, row_data[data_field_name]))
            if data_field_name == "positions"
            else row_data[data_field_name]
            for data_field_name in self.data_field_names
        }
