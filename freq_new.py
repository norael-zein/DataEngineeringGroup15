import sys
import csv
from collections import Counter

csvreader = csv.reader(sys.stdin)

first_column_values = [row[0] for row in csvreader] #row[0] for month and row[1] for UniqueCarrier 
counts = Counter(first_column_values)

for value, count in counts.items():
    print(f"{value}: {count}")
