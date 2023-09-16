"""
Start Test
"""

import main 


def test_summary():
    """Test the summary function for descriptive statistics"""
    new = main.summary()
    assert new["calories"][2] == 106.88
    assert new["protein"][-1] == 6.0
    assert new["fat"][4] == 0.0

def test_histogram():
    """Test that the histogram function saves a histogram file"""
    main.histogram()
    # check if the file 'Calories_of_Cereals.png" was created well 

if __name__ == "__main__":
    # Run the tests 
    test_summary()
    test_histogram()
