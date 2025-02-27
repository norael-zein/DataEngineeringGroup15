#!/usr/bin/env python3
import sys


next(sys.stdin)

for line in sys.stdin:
    fields = line.strip().split(",")
    
    
    if len(fields) < 8:
        continue

    try:
        month = fields[0]  
        carrier = fields[1] 
        cancelled = int(fields[7])  
        
        if cancelled == 1:
            print(f"{month}\t1")  
            print(f"{carrier}\t1")  
            
    except ValueError:
        continue  

