"""
Start Test
"""

from main import summary
from main import histogram


def test_summary():
    """Test defined summary (or describe) function"""
    return summary()


def test_histogram():
    """
    Test defined seeplot function to checkout a scatter plot
    """
    return histogram()


if __name__ == "__main__":
    test_summary()
    test_histogram()
