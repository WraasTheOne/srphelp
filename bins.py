def count_numbers_in_bins(numbers, num_bins, range_max):
    bin_size = range_max // num_bins
    bins = [0] * num_bins
    
    for number in numbers:
        bin_index = min(number // bin_size, num_bins - 1)
        bins[bin_index] += 1

    return bins

# Example input
numbers = [115, 98, 147, 150, 112, 150, 44, 67, 5, 58, 11, 143, 91, 182, 45, 19, 44, 55, 14, 115, 71, 98, 17, 95, 198, 116, 16, 116, 36, 155, 9, 91, 77, 139, 107, 135, 92, 50, 159, 62, 60, 64, 166, 55, 32, 9, 15, 149, 2, 147, 104, 181, 138, 186, 133, 44, 107, 33, 117, 83, 2, 154, 145, 137, 184, 116, 42, 196, 125, 116, 27, 153, 39, 52, 145, 181, 22, 161, 76, 180, 13, 134, 46, 88, 104, 119, 117, 76, 151, 157, 126, 42, 158, 153, 2, 195, 111, 10, 78, 45]
num_bins = 10  # Adjust the number of bins as needed
range_max = 199

# Count the frequency of numbers in bins
bins_count = count_numbers_in_bins(numbers, num_bins, range_max)

# Display the counts in each bin
for i, count in enumerate(bins_count):
    print("Bin {}: {}".format(i, count))
