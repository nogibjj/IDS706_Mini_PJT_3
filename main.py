"""Start main function"""

import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt

df_pl = pl.read_csv("cereal.csv")

def summary():
    """EDA with Polars describe function to get mean, median, and standard deviation"""
    outcome = df_pl.describe()
    summary_html = outcome.to_html("summary_statistics.html")
    return outcome, summary_html

def histogram():
    """Displays histogram with seaborn and matplotlib"""
    sns.histplot(data=df_pl, x="calories", kde=False, bins=20)
    plt.title("Calories of Cereals (n=77)")
    plt.show()
    plt.savefig("Calories_of_Cereals.png")
