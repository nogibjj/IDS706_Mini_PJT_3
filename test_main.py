"""
Start Test
"""

import main 


def test_summary_descriptive_statistics():
    """Test the summary function for descriptive statistics"""
    statistics = main.summary_descriptive_statistics()
    
    assert statistics["mean", "calories"] == 106.88
    assert statistics["max", "protein"] == 6.0
    assert statistics["25%", "fat"] == 0.0

def test_histogram_plot_saved():
    """Test that the histogram function saves a histogram file"""
    main.histogram_plot_saved()
    # check if the file 'Calories_of_Cereals.png" was created well 
    import os 
    assert os.path.isfile("Calories_of_Cereals.png")

if __name__ == "__main__":
    # Run the tests 
    test_summary_descriptive_statistics()
    test_histogram_plot_saved()
