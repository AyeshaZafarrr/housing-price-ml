import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Housing.csv")

plt.hist(df["price"], bins=5)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()