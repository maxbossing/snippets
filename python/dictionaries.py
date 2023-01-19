#!/usr/bin/python3
#
# Various methods regarding dictionaries


# Merges two or more Dictionaries into one
def merge_dicts(*dicts):
  mdict = defaultdict(list)
  for d in dicts:
    for key in d:
      mdict[key].append(d[key])
  return dict(mdict)


# Merges two lists into one dictionary
def merge_lists_to_dict(list1: list(), list2: list()):
    return dict(zip(list1, list2))


## Invert key and value of a Dictionary ##

# If all Values are unique
def invert_unique_dict(dictionary: dict()):
    return dict(map(reversed, dictionary.items()))

# If there are non-unique values
def invert_non_unique_dict(dictionary: dict()):
    from collections import defaultdict
    inverted_dict = defaultdict(list)
    {inverted_dict[v].append(k) for k, v in dictionary.items()}

# if any of the values are not hashable
def invert_unhashable_dict(dictionary: dict()):
    inverted_dict = defaultdict(list)
    return {value: key for key in inverted_dict for value in inverted_dict[key]}


# Split a dict into a list of tuples
def split_dict(dictionary: dict()):
    return zip(*dictionary.iterateitems())
