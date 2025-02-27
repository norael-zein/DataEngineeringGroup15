#!/usr/bin/env python3
import sys

current_key = None
cancel_count = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    
    try:
        count = int(value)
    except ValueError:
        continue

    if key == current_key:
        cancel_count += count
    else:
        if current_key is not None:
            print(f"{current_key}\t{cancel_count}")  
        current_key = key
        cancel_count = count


if current_key is not None:
    print(f"{current_key}\t{cancel_count}")

