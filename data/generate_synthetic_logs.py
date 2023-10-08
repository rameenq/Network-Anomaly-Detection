import pandas as pd
import random
from faker import Faker

fake = Faker()

# Number of log entries to generate
n = 1000

# Create empty lists to store log data
timestamps = []
ips = []
user_agents = []
status_codes = []
methods = []

# Generate synthetic logs
for _ in range(n):
    timestamps.append(fake.date_time_this_year())
    ips.append(fake.ipv4())
    user_agents.append(fake.user_agent())
    status_codes.append(random.choice([200, 201, 404, 500]))
    methods.append(random.choice(['GET', 'POST', 'PUT', 'DELETE']))

# Create a DataFrame
df = pd.DataFrame({
    'Timestamp': timestamps,
    'IP': ips,
    'UserAgent': user_agents,
    'Status': status_codes,
    'Method': methods
})

# Convert timestamps to Unix time
df['Timestamp'] = pd.to_datetime(df['Timestamp']).astype(int) / 10**9

# One-Hot Encode the HTTP Methods
df = pd.get_dummies(df, columns=['Method'])

# Save as CSV
df.to_csv('logs_train.csv', index=False)
df.sample(frac=0.2).to_csv('logs_test.csv', index=False)
