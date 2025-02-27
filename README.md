# DataEngineeringGroup15
Data taken from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7

The data was processed and filtered using the file preprocessing.sh to remove unnecessary information from the files. 

Preprocessing and filtering: preprocessing.sh

MapReduce: mapper.py & reduce.py

Number of cancellations for each carrier: airline.txt
Number of cancellations for each month: airline_month.txt

Calculate number of rows: freq_new.py

Number of rows for each:
- Month: output_freq_month.txt
- Carrier: output_freq_carrier.txt


Produce final frequency distribution: final_frequency.py
Final frequency distribution: final_freq.txt      

Produce plot: airline_month.py 

