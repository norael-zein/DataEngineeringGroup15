#!/bin/bash

cd original_data #Change to folder where our zipped files are

# Loop through all .csv.bz2 files
for file in *.csv.bz2; do
    #Create an output filename based on the input file
    #output_file="${file%.bz2}_new.csv"
    output_file="${file%.bz2}"
    output_file="${output_file%.csv}_new.csv"


    #Use bzcat to read the .bz2 file, then use cut to remove specified columns, and save the output
    bzcat "$file" | cut -d',' --complement -f3,4,5,6,7,8,11,12,13,14,15,20,21,23,24,25,26,27,28,29 > "$output_file"

    #Remove the original decompressed file if you don't want to keep it
    # rm "${file%.bz2}"
done
