"""
Start Test
"""

import main 


def test_summary_descriptive_statistics():
    """Test the summary function for descriptive statistics"""
    statistics = main.summary()
    
    assert statistics["calories"]["mean"] == 106.88
    assert statistics["protein"]["max"] == 6.0
    assert statistics["fat"]["25%"] == 0.0

def test_histogram_plot_saved():
    """Test that the histogram function saves a histogram file"""
    main.histogram()
    # check if the file 'Calories_of_Cereals.png" was created well 
    import os 
    assert os.path.isfile("Calories_of_Cereals.png")

if __name__ == "__main__":
    # Run the tests 
    test_summary_descriptive_statistics()
    test_histogram_plot_saved()
