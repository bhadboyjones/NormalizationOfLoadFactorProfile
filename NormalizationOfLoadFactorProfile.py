import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as mtick

# importing the data
df = pd.read_excel('normalization.xlsx', index_col='Unnamed: 0', usecols=[0, 1, 2], skiprows=1)

# Renaming columns
df.columns = ['P1', 'P2']

# Getting maximum of profile in df1
profile1_max = df['P1'].max()
profile2_max = df['P2'].max()

print('Daily Peak (KW) for profile 1:', profile1_max)
print('Daily Peak (KW) for profile 2:', profile2_max)

# Creating new columns
df['Normalized Profile 1'] = ''
df['Normalized Profile 2'] = ''

# Calculating load profile
df['Normalized Profile 1'] = df['P1']/profile1_max
df['Normalized Profile 2'] = df['P2']/profile2_max

pd.set_option('display.max_columns', 5)

# Plotting using plt
fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(df.index, df['P1'], color='blue', label='Profile 1')
ax.plot(df.index, df['P2'], color='red', label='Profile 2')

# To ensure correct axis limits
ax.set_xlim([df.index[0], df.index[-1]])

# To set axis properties
plt.xticks(rotation=90)

print(type(df.index))

# Select df.index[] to show only Hr & secs
ax.xaxis.set_major_locator(md.MinuteLocator(byminute=[0, 30]))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M)'))


plt.title('Actual Profiles (kW)')
plt.legend()
#plt.show()


# Plotting for the Normalized profiles
ax.plot(df.index, df['Normalized Profile 1'], color='blue', label='Profile 1')
ax.plot(df.index, df['Normalized Profile 2'], color='red', label='Profile 2')

# To ensure correct axis limits
ax.set_xlim([df.index[0], df.index[-1]])

# To set axis properties
plt.xticks(rotation=90)

print(type(df.index))

# Select df.index[] to show only Hr & secs
ax.xaxis.set_major_locator(md.MinuteLocator(byminute=[0, 30]))
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M)'))

plt.title('Normalized Profiles (kW)')
plt.legend()
#plt.show()


