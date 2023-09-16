"""Start main function"""

import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

df_pl = pl.read_csv("cereal.csv")
pandas_df = df_pl.to_pandas()

def summary():
    """EDA with Polars describe function to get mean, median, and standard deviation"""
    print(df_pl.describe())
    return df_pl.describe() 

def histogram():
    """Displays histogram with seaborn and matplotlib"""
    sns.histplot(data=df_pl, x="calories", kde=False, bins=20)
    plt.title("Calories of Cereals (n=77)")
    plt.savefig("Calories_of_Cereals.png")
    plt.show()
    pdf_report_generator(pandas_df)

def pdf_report_generator(df):
    profile = ProfileReport(df, title="Summary Report")
    profile.to_file("Summary_Report.html")
