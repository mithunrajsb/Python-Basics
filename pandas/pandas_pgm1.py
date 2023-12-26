import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Anil', 'Bobby', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New Delhi', 'Chicago', 'London']}

df = pd.DataFrame(data)

# Displaying specific columns
print(df['Name'])  # Display 'Name' column

# Filtering data
filtered_data = df[df['Age'] > 25]  # Get rows where Age > 25

print(filtered_data)
