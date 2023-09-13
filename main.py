"""Start main function"""

import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

df_pl = pl.read_csv("cereal.csv")


def summary():
    """EDA with Polars describe function to get mean, median, and standard deviation"""
    print(df_pl.describe())

def pdf_report_generator(df):
    profile = ProfileReport(df, title="Summary Report")
    profile.to_file("Summary_Report.html")

def histogram():
    """Displays histogram with plotly.express library"""
    sns.histplot(data=df_pl, x="calories", kde=False, bins=20)
    plt.title("Calories of Cereals (n=77)")
    plt.show()
    plt.savefig("Calories_of_Cereals.png")
    print(df_pl)
    pdf_report_generator(df_pl)
    return df_pl
