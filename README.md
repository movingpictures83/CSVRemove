# CSVRemove
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV (indexed)
# Tested with: PluMA 1.0, Python 3.6
# Dependency: numpy==1.16.0

A PluMA plugin that takes a CSV file and removes a user-specified
column, creating a new CSV file with the remaining columns.

The plugin takes as input a tab-separated file of two keyword value
pairs: csvfile (name of the input CSV file) and column number (an integer
representing the column to remove).

