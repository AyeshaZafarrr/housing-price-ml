import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Housing.csv")

plt.hist(df["price"], bins=10)
plt.xlabel("Price")
plt.ylabel("Number of Houses")
plt.title("Distribution of House Prices")

plt.show()