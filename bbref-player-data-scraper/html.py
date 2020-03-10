import re

class PlayerSeasonBoxScoresPage:
    def __init__(self, html):
        self.html = html

    @property
    def regular_season_box_scores_table_query(self):
        return '//table[@id="pgl_basic"]'

    @property
    def regular_season_box_scores_table(self):
        matching_tables = self.html.xpath(self.regular_season_box_scores_table_query)

        if len(matching_tables) != 1:
            return None

        return RegularSeasonPlayerBoxScoresTable(html=matching_tables[0])


class PlayerSeasonBoxScoresTable:
    def __init__(self, html):
        self.html = html

    @property
    def rows_query(self):
        raise NotImplementedError()

    @property
    def rows(self):
        return [
            PlayerSeasonBoxScoresRow(html=row_html)
            for row_html in self.html.xpath(self.rows_query)
        ]


class RegularSeasonPlayerBoxScoresTable(PlayerSeasonBoxScoresTable):
    @property
    def rows_query(self):
        # Every 20 rows, there's a row that has the column header values - those should be ignored
        return '//tbody' \
               '/tr[not(contains(@class, "thead"))]'


class PlayerSeasonBoxScoresRow:
    def __init__(self, html):
        self.html = html

    def __eq__(self, other):
        if isinstance(other, PlayerSeasonBoxScoresRow):
            return self.html == other.html
        return False

    @property
    def is_active(self):
        # When a player is not active (for a reason like "Inactive", "Did Not Play", "Did Not Dress")
        # the game played counter is blank (and a "reason" column will exist)
        return self.html[1].text_content() != ""

    @property
    def date(self):
        return self.html[2].text_content()

    @property
    def playing_time(self):
        return self.html[9].text_content()

    @property
    def made_field_goals(self):
        return self.html[10].text_content()

    @property
    def attempted_field_goals(self):
        return self.html[11].text_content()

    @property
    def made_three_point_field_goals(self):
        return self.html[13].text_content()

    @property
    def attempted_three_point_field_goals(self):
        return self.html[14].text_content()

    @property
    def made_free_throws(self):
        return self.html[16].text_content()

    @property
    def attempted_free_throws(self):
        return self.html[17].text_content()

    @property
    def offensive_rebounds(self):
        return self.html[19].text_content()

    @property
    def defensive_rebounds(self):
        return self.html[20].text_content()

    @property
    def total_rebounds(self):
        return self.html[21].text_content()

    @property
    def assists(self):
        return self.html[22].text_content()

    @property
    def steals(self):
        return self.html[23].text_content()

    @property
    def blocks(self):
        return self.html[24].text_content()

    @property
    def turnovers(self):
        return self.html[25].text_content()

    @property
    def personal_fouls(self):
        return self.html[26].text_content()

    @property
    def points_scored(self):
        return self.html[27].text_content()

    @property
    def game_score(self):
        return self.html[28].text_content()

    @property
    def plus_minus(self):
        return self.html[29].text_content()


class PlayerBoxScoreRow:
    def __init__(self, html):
        self.html = html

    @property
    def slug(self):
        return self.html[1].get('data-append-csv')

    @property
    def name(self):
        return self.html[1].text_content()

    @property
    def team_abbreviation(self):
        return self.html[2].text_content()

    @property
    def location_abbreviation(self):
        return self.html[3].text_content()

    @property
    def opponent_abbreviation(self):
        return self.html[4].text_content()

    @property
    def outcome(self):
        return self.html[5].text_content()

    @property
    def playing_time(self):
        return self.html[6].text_content()

    @property
    def made_field_goals(self):
        return self.html[7].text_content()

    @property
    def attempted_field_goals(self):
        return self.html[8].text_content()

    @property
    def made_three_point_field_goals(self):
        return self.html[10].text_content()

    @property
    def attempted_three_point_field_goals(self):
        return self.html[11].text_content()

    @property
    def made_free_throws(self):
        return self.html[13].text_content()

    @property
    def attempted_free_throws(self):
        return self.html[14].text_content()

    @property
    def offensive_rebounds(self):
        return self.html[16].text_content()

    @property
    def defensive_rebounds(self):
        return self.html[17].text_content()

    @property
    def assists(self):
        return self.html[19].text_content()

    @property
    def steals(self):
        return self.html[20].text_content()

    @property
    def blocks(self):
        return self.html[21].text_content()

    @property
    def turnovers(self):
        return self.html[22].text_content()

    @property
    def personal_fouls(self):
        return self.html[23].text_content()

    @property
    def game_score(self):
        return self.html[26].text_content()