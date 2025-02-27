# DataEngineeringGroup15
Data taken from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7

Preprocessing and filtering: **preprocessing.sh**

MapReduce: **mapper.py** & **reduce.py**

Number of cancellations for each carrier: **airline.txt**
Number of cancellations for each month: **airline_month.txt**

Calculate number of data rows in month and carrier columns: **freq_new.py**

Number of rows for each:
- Month:**output_freq_month.txt**
- Carrier: **output_freq_carrier.txt**

Produce final frequency distribution: **final_frequency.py**
Final frequency distribution: 
- Month:**final_freq_month.txt**
- Carrier: **final_freq_carrier.txt**     

Produce plot for number of cancellations: **airline_month.py**

Produce plot for frequency of cancellations:**plot_freq.py**

