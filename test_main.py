"""
Start Test
"""

import polars as pl
from main import summary


def test_summary():
    """
    test summary function in main.py
    """
    data = pl.read_csv("cereal.csv")
    new = summary(data)
    assert new["calories"][2] == 106.88311688311688
    assert new["protein"][-1] == 6.0
    assert new["fat"][4] == 0.0


if __name__ == "__main__":
    test_summary()
