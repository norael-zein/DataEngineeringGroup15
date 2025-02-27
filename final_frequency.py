
with open('output_freq_carrier.txt', 'r') as f:
    output_freq_carrier = dict(line.strip().split(': ') for line in f)

with open('output_freq_month.txt', 'r') as f:
    output_freq_month = dict(line.strip().split(': ') for line in f)

with open('airline.txt', 'r') as f:
    airline_data = dict(line.strip().split() for line in f)

with open('airline_month.txt', 'r') as f:
    airline_month_data = dict(line.strip().split() for line in f)


output_freq_carrier = {key: int(value) for key, value in output_freq_carrier.items()}
output_freq_month = {key: int(value) for key, value in output_freq_month.items()}
airline_data = {key: int(value) for key, value in airline_data.items()}
airline_month_data = {key: int(value) for key, value in airline_month_data.items()}


for key in airline_month_data:
    if key in output_freq_month:
        airline_month_data[key] = airline_month_data[key] / output_freq_month[key]

for key in airline_data:
    if key in output_freq_carrier:
        airline_data[key] = airline_data[key] / output_freq_carrier[key]

for key, value in airline_month_data.items():
    print(f"{key}: {value}")

for key, value in airline_data.items():
    print(f"{key}: {value}")
