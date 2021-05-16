import re
def arithmetic_arranger(problems):
  if len(problems) > 5:
    raise Exception("Error: Too many problems.")
  
  illegal_operators = ["*", "/"]
  # Could also use regex here...
  if any([i_o in p for p in problems for i_o in illegal_operators]):
    raise Exception("Error: Operator must be '+' or '-'.")
  
  if any([re.search('[A-Za-Z]+',x) for x in problems]):
    raise Exception("Error: Numbers must only contain digits")

    return arranged_problems