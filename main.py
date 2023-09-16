"""Start main function"""

import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

df_pl = pl.read_csv("cereal.csv")
pandas_df1 = df_pl.to_pandas()

def summary_descriptive_statistics():
    """EDA with Polars describe function to get mean, median, and standard deviation"""
    statistics = df_pl.describe()
    print(statistics)
    return statistics 

def histogram_plot_saved():
    """Displays histogram with seaborn and matplotlib"""
    sns.histplot(data=df_pl, x="calories", kde=False, bins=20)
    plt.title("Calories of Cereals (n=77)")
    plt.savefig("Calories_of_Cereals.png")
    plt.show()
    pdf_report_generator(pandas_df1)

def pdf_report_generator(df):
    profile = ProfileReport(df, title="Summary Report")
    profile.to_file("Summary_Report.html")
