"""
Start Test
"""

import main 


def test_summary():
    new = main.summary()
    """Test summary (or describe) function"""
    assert new["calories"][2] == 106.88311688311688
    assert new["protein"][-1] == 6.0
    assert new["fat"][4] == 0.0

def test_histogram():
    """
    Test histogram function set on main file
    """
    main.histogram()

if __name__ == "__main__":
    test_summary()
    test_histogram()
