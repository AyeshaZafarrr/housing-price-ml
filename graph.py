import matplotlib
matplotlib.use('Agg')  # no window, saves image

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Housing.csv")

# Create plot
plt.figure()
plt.scatter(df["area"], df["price"])

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Housing Price vs Area")

# Save graph
plt.savefig("graph.png", dpi=300, bbox_inches='tight')

print("Graph saved as graph.png")