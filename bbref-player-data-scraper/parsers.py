import re
from dateutil.parser import parse as du_parse

from utilities import str_to_int, str_to_float, get_seconds

class PlayerSeasonAveragesWithinDateRangeParser:
    def parse(box_scores, from_date, to_date):
        return [
            {
                "MP": get_seconds(box_score.playing_time),
                "FGM": str_to_int(box_score.made_field_goals),
                "FGA": str_to_int(box_score.attempted_field_goals),
                "3PM": str_to_int(box_score.made_three_point_field_goals),
                "3PA": str_to_int(box_score.attempted_three_point_field_goals),
                "FTM": str_to_int(box_score.made_free_throws),
                "FTA": str_to_int(box_score.attempted_free_throws),
                "ORB": str_to_int(box_score.offensive_rebounds),
                "DRB": str_to_int(box_score.defensive_rebounds),
                "TRB": str_to_int(box_score.total_rebounds),
                "AST": str_to_int(box_score.assists),
                "STL": str_to_int(box_score.steals),
                "BLK": str_to_int(box_score.blocks),
                "TOV": str_to_int(box_score.turnovers),
                "PF": str_to_int(box_score.personal_fouls),
                "PTS": str_to_int(box_score.points_scored),
                "GmSc": str_to_float(box_score.game_score),
                "+/-": str_to_int(box_score.plus_minus),
            } for box_score in box_scores
            if box_score.is_active and from_date <= du_parse(box_score.date) < to_date
        ]