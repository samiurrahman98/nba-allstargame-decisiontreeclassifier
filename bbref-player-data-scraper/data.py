from enum import Enum

class OutputType(Enum):
    JSON = "JSON"
    CSV = "CSV"

class OutputWriteOption(Enum):
    WRITE = "w"
    CREATE_AND_WRITE = "w+"
    APPEND = "a"
    APPEND_AND_WRITE = "a+"

class ApplicationMode(Enum):
    ALL_STAR = "1"
    ALL_STAR_NUM_ARGS = 7
    DATE_RANGE = "2"
    DATE_RANGE_NUM_ARGS = 4
    SEPARATE_PLAYERS_BY_POSITION = "3"
    SEPARATE_PLAYERS_BY_POSITION_NUM_ARGS = 1

class PlayerPositions(Enum):
    GUARD = "Guard"
    FORWARD = "Forward"
    POINT_FORWARD = "Point-Forward"
    CENTER = "Center"