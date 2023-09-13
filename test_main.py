"""
Start Test
"""

import main 

def test_summary():
    """Test defined summary (or describe) function"""
    assert pandas_df1["calories"]["mean"] == 106.88311688311688
    assert pandas_df1["protein"]["max"] == 6.0
    assert pandas_df1["fat"]["min"] == 0

def test_histogram():
    """
    Test defined seeplot function to checkout a scatter plot
    """
    main.histogram()

if __name__ == "__main__":
    test_summary()
    test_histogram()
