#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_list = [1, [2, True, 24, ('hí', None, 12.4)], 4, 5]

def get_integers(items):
  result_list = []

  def find_ints(items):
    for item in items:
      find_ints(item) \
			if type(item) in [list, tuple, set] else \
			result_list.append(item) if type(item) is int else\
			print(f"{item} Not added!")

  find_ints(items)
  return result_list

s = get_integers(input_list)
print(f"Integer elements: {s}")
