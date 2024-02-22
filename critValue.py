from scipy.stats import chi2

# Define the significance level (alpha) and degrees of freedom (df)
alpha = 0.05
df = 9  # Example degrees of freedom

# Calculate the critical value
critical_value = chi2.ppf(1 - alpha, df)

print("Critical value for alpha = {:.2f} and df = {}: {:.4f}".format(alpha, df, critical_value))
