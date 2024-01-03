import pandas as pd
from tqdm.auto import tqdm

# Load the CSV file
file_path = 'nifty50.csv'
nifty50_df = pd.read_csv(file_path, encoding='Windows-1252')

# Show the head of the dataframe
print(nifty50_df.head())

# Describe the dataframe
print(nifty50_df.describe())

# It seems that there are trailing spaces in the column names. Let's fix that.
nifty50_df.columns = [col.strip() for col in nifty50_df.columns]

# Now let's try plotting again
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn
sns.set(style='whitegrid')

# Plotting distributions of the 'Open', 'High', 'Low', 'Close' columns
plt.figure(figsize=(14, 7))

# Subplot for the 'Open' distribution
plt.subplot(2, 2, 1)
sns.histplot(nifty50_df['Open'], bins=30, kde=True)
plt.title('Distribution of Opening Prices')

# Subplot for the 'High' distribution
plt.subplot(2, 2, 2)
sns.histplot(nifty50_df['High'], bins=30, kde=True)
plt.title('Distribution of High Prices')

# Subplot for the 'Low' distribution
plt.subplot(2, 2, 3)
sns.histplot(nifty50_df['Low'], bins=30, kde=True)
plt.title('Distribution of Low Prices')

# Subplot for the 'Close' distribution
plt.subplot(2, 2, 4)
sns.histplot(nifty50_df['Close'], bins=30, kde=True)
plt.title('Distribution of Closing Prices')

plt.tight_layout()
plt.show()
