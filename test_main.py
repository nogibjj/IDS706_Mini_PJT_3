"""
Start Test
"""

from main import summary
from main import histogram


def test_summary():
    """Test defined summary (or describe) function"""
    return summary()
    assert df_pl["calories"]["mean"] == 106.88311688311688
    assert df1["protein"]["max"] == 6.0
    assert df1["fat"]["min"] == 0

def test_histogram():
    """
    Test defined seeplot function to checkout a scatter plot
    """
    histogram()

if __name__ == "__main__":
    test_summary()
    test_histogram()
