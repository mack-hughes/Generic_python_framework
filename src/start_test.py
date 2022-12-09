from .start import sum_function

def test_sum_function():
    """
        Testing the sum function
    """
    result = sum_function(1, 1)
    assert result == 2
