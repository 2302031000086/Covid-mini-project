import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\HP\Downloads\01-05-2020.csv")

# Rename columns for easier access
df.rename(columns=
{
    'Name of State / UT': 'State',
    'Total Confirmed cases (Including 111 foreign Nationals)': 'Total_Cases',
    'Cured/Discharged/Migrated': 'Recovered',
    'Death': 'Deaths'
}, inplace=True)

# Plot total confirmed cases by state
# Drop rows with missing State or Total_Cases
df = df.dropna(subset=['State', 'Total_Cases'])

# Convert State to string (just in case there are non-string types)
df['State'] = df['State'].astype(str)

# Now plot
plt.figure(figsize=(14, 8))
plt.barh(df['State'], df['Total_Cases'], color='skyblue')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('State/UT')
plt.title('COVID-19 Total Confirmed Cases in India (01-05-2020)')
plt.tight_layout()
plt.show()
