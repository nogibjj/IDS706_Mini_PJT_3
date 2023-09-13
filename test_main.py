"""
Start Test
"""

import main 
import polars as pl 

df_pl = pl.read_csv("cereal.csv")
pandas_df1 = df_pl.to_pandas()

def test_summary():
    new = summary()
    """Test defined summary (or describe) function"""
    assert new["calories"]["mean"] == 106.88311688311688
    assert new["protein"]["max"] == 6.0
    assert new["fat"]["min"] == 0

def test_histogram():
    """
    Test defined seeplot function to checkout a scatter plot
    """
    main.histogram()

if __name__ == "__main__":
    test_summary()
    test_histogram()
