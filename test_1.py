import re

def is_valid_string(given_string):
    reg_pattern = r'^(?=(.*\d.*){2,3})(?=(.*\D.*){3})(?=\S{6,})[A-Za-z0-9\D]*$'
    return bool(re.match(reg_pattern, given_string))
