import matplotlib.pyplot as plt

def read_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                key, value = parts[0], int(parts[1])
                data[key] = value
    return data


month_data = read_data('month.txt')
airline_data = read_data('airline.txt')


plt.figure(figsize=(10, 5))
plt.bar(month_data.keys(), month_data.values(), color='skyblue')
plt.xlabel('Month')
plt.ylabel('Flight Count')
plt.title('Monthly Flight Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('monthly_flights.png')
plt.show()


plt.figure(figsize=(8, 8))
plt.pie(airline_data.values(), labels=airline_data.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Flight Distribution by Airline')
plt.axis('equal')
plt.savefig('airline_distribution.png')
plt.show()
