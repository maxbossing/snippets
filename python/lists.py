#!/usr/bin/python3
#
# Various methods regarding lists

# Flatten list of lists into one list
def flatten_list(list_of_list: list()):
    return sum(list_of_list, [])