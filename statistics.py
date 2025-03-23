import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import trim_mean
from statsmodels import robust
import wquantiles

# Load dataset (Ensure the CSV file is in the same directory)
data = pd.read_csv("CAvideos.csv")

# Display first few rows
print(data.head())

# Compute statistics
print("Mean Views:", data['views'].mean())
print("Trimmed Mean Views (10%):", trim_mean(data['views'], 0.1))
print("Median Likes:", data['likes'].median())
print("Median Comment Count:", data['comment_count'].median())
print("Mean Dislikes:", data['dislikes'].mean())
print("Weighted Mean Likes:", np.average(data['likes'], weights=data['views']))
print("Weighted Median Likes:", wquantiles.median(data['likes'], weights=data['views']))
print("Standard Deviation of Views:", data['views'].std())
print("Interquartile Range of Views:", data['views'].quantile(0.75) - data['views'].quantile(0.25))
print("MAD of Likes:", robust.scale.mad(data['likes']))

# Quantiles
print("Quantiles for Likes:\n", data['likes'].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))

# Plot Boxplot for Views
views_millions = data['views'] / 1_000_000
plt.figure(figsize=(6, 8))
sns.boxplot(y=views_millions)
plt.ylabel('Views (millions)')
plt.ylim(0, views_millions.max() * 0.05)
plt.title('Boxplot of Video Views')
plt.tight_layout()
plt.show()

# Bin Views into Ranges
binned_views = pd.cut(data['views'], 10)
print("Binned Views Counts:\n", binned_views.value_counts())

# Histogram of Likes
plt.figure(figsize=(4, 4))
sns.histplot(data['likes'], bins=20, kde=True)
plt.xlabel('Likes')
plt.title('Distribution of Likes')
plt.tight_layout()
plt.show()

# Histogram of Views
plt.figure(figsize=(4, 4))
sns.histplot(data['views'], bins=20, kde=True)
plt.xlabel('Views')
plt.title('Distribution of Views')
plt.tight_layout()
plt.show()

# Percentages for Numeric Columns
total_sum = data.select_dtypes(include='number').values.sum()
percentages = 100 * data.select_dtypes(include='number') / total_sum
print("Percentage Contribution of Numeric Columns:\n", percentages)

# Bar Plot for Selected Columns
columns_to_plot = ['likes', 'comment_count']
data[columns_to_plot].sum().plot(kind='bar', figsize=(8, 6), color=['blue', 'orange'])
plt.xlabel('Metric')
plt.ylabel('Total Count')
plt.title('Comparison of Likes and Comment Count')
plt.tight_layout()
plt.show()
