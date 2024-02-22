import numpy as np

def chi_squared(observed, expected):
   
    observed = np.array(observed)
    expected = np.array(expected)
    print((observed - expected)**2 / expected)
    
    # Calculate the chi-squared statistic
    chi_squared_stat = np.sum((observed - expected)**2 / expected)
    
    return chi_squared_stat

# Example usage:
observed_freq = [4, 13, 11, 15, 7, 10 , 8 ,10 , 8 , 14]
expected_freq = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

chi_squared_value = chi_squared(observed_freq, expected_freq)
print("Chi-squared statistic:", chi_squared_value)
