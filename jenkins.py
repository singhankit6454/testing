import pandas as pd

# Sample data for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('jenkins_data.csv', index=False)

print("Data saved to sample_data.csv")
