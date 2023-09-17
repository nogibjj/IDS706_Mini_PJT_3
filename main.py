"""Start main function"""

import polars as pl
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

df = pl.read_csv("cereal.csv")


def summary(data):
    """EDA with Polars describe function to get mean, median, and standard deviation"""
    print(data.describe())
    return data.describe()


def histogram(data):
    """Displays histogram with seaborn and matplotlib"""
    plt.hist(data["calories"], bins=20)
    plt.title("Calories of Cereals (n=77)")
    plt.xlabel("Calories")
    plt.ylabel("Frequency")
    plt.savefig("Calories_of_Cereals.png")
    plt.show()
    pdf_report_generator(data)


def pdf_report_generator(data):
    """Generate summary report"""
    profile = ProfileReport(data, title="Summary Report")
    profile.to_file("Summary_Report.html")


if __name__ == "__main__":
    summary(df)
    histogram(df)
