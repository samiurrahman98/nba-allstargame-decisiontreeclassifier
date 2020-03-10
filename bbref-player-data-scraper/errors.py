class InvalidPlayerAndSeason(Exception):
    def __init__(self, player_identifier, season_end_year):
        message = "Player with identifier \"{player_identifier}\" in season ending in {season_end_year} is invalid" \
            .format(player_identifier=player_identifier, season_end_year=season_end_year)
        super().__init__(message)

class InvalidMode(Exception):
    def __init__(self, mode):
        message = "The mode value {mode} is invalid".format(mode=mode)
        super().__init__(message)

class InvalidPlayerPosition(Exception):
    def __init__(self, position):
        message = "The player position {position} is invalid".format(position=position)
        super().__init__(message)

class InvalidNumberOfArguments(Exception):
    def __init__(self, num_arguments):
        message = "The required number of arguments for this mode is {num_arguments}".format(num_arguments=num_arguments)
        super().__init__(message)