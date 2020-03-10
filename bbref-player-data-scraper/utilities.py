from time import strftime, gmtime

def str_to_int(value, default=int(0)):
    stripped_value = value.strip()
    try:
        return int(stripped_value)
    except ValueError:
        return default


def str_to_float(value, default=float(0)):
    stripped_value = value.strip()
    try:
        return float(stripped_value)
    except ValueError:
        return default


def merge_two_dicts(first, second):
    combined = first.copy()
    combined.update(second)
    return combined

def get_seconds(time_str):
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

def get_minutes(seconds):
    return seconds / 60