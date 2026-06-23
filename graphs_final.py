import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Housing.csv")

# ---------------------------
# 1. Area vs Price (Scatter)
# ---------------------------
plt.figure()
plt.scatter(df["area"], df["price"])
plt.title("Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.savefig("1_area_vs_price.png", dpi=300)

# ---------------------------
# 2. Bedrooms vs Price (Bar)
# ---------------------------
plt.figure()
avg1 = df.groupby("bedrooms")["price"].mean()
plt.bar(avg1.index, avg1.values)
plt.title("Average Price by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.savefig("2_bedrooms_vs_price.png", dpi=300)

# ---------------------------
# 3. Bathrooms vs Price (Bar)
# ---------------------------
plt.figure()
avg2 = df.groupby("bathrooms")["price"].mean()
plt.bar(avg2.index, avg2.values)
plt.title("Average Price by Bathrooms")
plt.xlabel("Bathrooms")
plt.ylabel("Price")
plt.savefig("3_bathrooms_vs_price.png", dpi=300)

# ---------------------------
# 4. Price Distribution (Histogram)
# ---------------------------
plt.figure()
plt.hist(df["price"], bins=5)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig("4_price_distribution.png", dpi=300)

# ---------------------------
# 5. Boxplot (Outliers)
# ---------------------------
plt.figure()
plt.boxplot(df["price"])
plt.title("Price Outliers")
plt.ylabel("Price")
plt.savefig("5_price_outliers.png", dpi=300)

print("All graphs saved successfully!")