# Task 04: Advanced Data Visualization using Matplotlib + pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# Scatter plot with labeled points
plt.figure(figsize=(8,6))
plt.scatter(df["Sales"], df["Profit"], c="blue", alpha=0.7)

# Add labels for each point
for i, row in df.iterrows():
    plt.text(row["Sales"]+1, row["Profit"]+1, row["Category"], fontsize=9)

plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit (with Labels)")
plt.grid(True)
plt.show()

# Statistical overlay using regression line
plt.figure(figsize=(8,6))
sns.regplot(x="Sales", y="Profit", data=df,scatter_kws={"color": "blue"},line_kws={"color": "red"})
plt.title("Sales vs Profit with Regression Line")
plt.show()
