def count_numbers_in_bins(numbers, num_bins, range_max):
    bin_size = range_max // num_bins
    bins = [0] * num_bins
    
    for number in numbers:
        bin_index = min(number // bin_size, num_bins - 1)
        bins[bin_index] += 1

    return bins

# Example input
numbers = [96, 61, 145, 114, 60, 37, 95, 67, 19, 23, 126, 171, 44, 147, 130, 187, 125, 132, 70, 108, 158, 174, 77, 112, 69, 72, 169, 121, 158, 44, 59, 148, 97, 21, 172, 180, 2, 49, 92, 38, 25, 142, 99, 28, 7, 78, 192, 138, 40, 108, 58, 62, 60, 58, 45, 112, 14, 154, 80, 88, 149, 74, 50, 159, 37, 189, 145, 24, 31, 21, 41, 91, 154, 110, 117, 99, 139, 190, 132, 19, 24, 53, 162, 186, 180, 92, 137, 198, 177, 72, 135, 154, 56, 57, 65, 29, 183, 1, 174, 48]
num_bins = 10  # Adjust the number of bins as needed
range_max = 199

# Count the frequency of numbers in bins
bins_count = count_numbers_in_bins(numbers, num_bins, range_max)

# Display the counts in each bin
for i, count in enumerate(bins_count):
    print("Bin {}: {}".format(i, count))
