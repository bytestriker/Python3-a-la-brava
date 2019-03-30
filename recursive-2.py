#!/usr/bin/env python

input_list = [2, ['24s1',0],{[1], 3}, [['¡¡'], 4],(3,'a')]

def get_integers(items):
  result_list = []
  def find_ints(items):
    for item in items:
      find_ints(items) if type(item) in [list, dict, tuple, set] else \
      result_list.append(item) if type(item) is int else \
      print(f"Item {item} was not included")
      
  find_ints(items)
  return result_list
  


get_integers(input_list)
      

    
