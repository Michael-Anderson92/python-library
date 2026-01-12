# builtins_reference.py
"""
Python Built-in Functions Reference
Personal study notes - fill in examples as you learn
"""

# =============================================================================
# TIER 1: USE THESE CONSTANTLY
# =============================================================================

# print() - Output to screen
# Write your examples below:




# input() - Get user input
# Write your examples below:




# len() - Get length of things (strings, lists, etc.)
# Write your examples below:




# range() - Generate number sequences (used in for loops)
# Write your examples below:




# type() - Check what type something is
# Write your examples below:




# int() - Convert to integer
# Write your examples below:




# float() - Convert to decimal number
# Write your examples below:




# str() - Convert to string
# Write your examples below:




# =============================================================================
# TIER 2: USE THESE REGULARLY
# =============================================================================

# list() - Create or convert to list
# Write your examples below:




# abs() - Absolute value (distance from zero)
# Write your examples below:

def abs_basic():
  print("abs(-5):", abs(-5))
  print("abs(3.14):", abs(3.14))
  print("abs(-42):", abs(-42))
  print("abs(0):", abs(0))

def abs_complex():
  number = 42
  number2 = -3 + 4j
  print(f"abs({number}):", abs(number))
  print(f"abs({number2}):", abs(number2))

def abs_variable(number):
  print(f"abs({number}):", abs(number))




# round() - Round numbers
# Write your examples below:

def round_basic():
  print("round(5.4):", round(5.4))
  print("round(5.6):", round(5.6))
  print("round(5.5):", round(5.5))
  print("round(5.45, 1):", round(5.45, 1))


# max() - Find the largest value
# Write your examples below:

def find_maxnum([]):
  numbers = [3, 7, 2, 9, 4]
  print("max(numbers):", max(numbers))

def find_maxchar([]):
  chars = ['a', 'z', 'm', 'b']
  print("max(chars):", max(chars))

def find_maxvar(a, b, c):
  print("max(a, b, c):", max(a, b, c))


# min() - Find the smallest value
# Write your examples below:




# sum() - Add up all items in a list
# Write your examples below:




# sorted() - Sort items (returns new list)
# Write your examples below:




# bool() - Convert to True/False
# Write your examples below:




# =============================================================================
# TIER 3: VERY USEFUL ONCE YOU KNOW THEM
# =============================================================================

# enumerate() - Loop with index AND value
# Write your examples below:




# zip() - Loop through multiple lists together
# Write your examples below:




# all() - Check if ALL items are truthy
# Write your examples below:




# any() - Check if ANY item is truthy
# Write your examples below:




# isinstance() - Check if something is a specific type
# Write your examples below:




# =============================================================================
# TIER 4: LEARN WHEN YOU NEED THEM
# =============================================================================

# open() - Read/write files
# Write your examples below:




# map() - Apply function to every item
# Write your examples below:




# filter() - Keep items that pass a test
# Write your examples below:




# reversed() - Reverse a sequence
# Write your examples below:




# chr() - Convert ASCII code to character
# Write your examples below:




# ord() - Convert character to ASCII code
# Write your examples below:




# =============================================================================
# NOTES
# =============================================================================

# Add any personal notes, tips, or gotchas you discover:
#
#
#




  