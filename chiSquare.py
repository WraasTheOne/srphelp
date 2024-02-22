import numpy as np

def chi_squared(observed, expected):
   
    observed = np.array(observed)
    expected = np.array(expected)
    
    # Calculate the chi-squared statistic
    chi_squared_stat = np.sum((observed - expected)**2 / expected)
    
    return chi_squared_stat

# Example usage:
observed_freq = [13, 6, 13, 6, 9,9,11,15,9,9]
expected_freq = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

chi_squared_value = chi_squared(observed_freq, expected_freq)
print("Chi-squared statistic:", chi_squared_value)
