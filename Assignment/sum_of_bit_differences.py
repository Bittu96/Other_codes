sample_array_1 = [1, 2]
sample_array_2 = [1,3,5]

def compute_bit_difference(array):
	sum_of_bit_differences = 0

	# going through each and every pair

	for i in array:
	    for j in array:

	        # finding bit differences which is bacically XOR
	        # (as XOR returns 1 if not same)
	        # here it returns string of 0s or 1s as comparisions
	        # and formatting as a binary
	        bit_difference = f"{i^j:b}"

	        # counting for ones which is
	        # basically the differences in bits
	        count_of_ones = bit_difference.count("1")

	        # adding the differences
	        sum_of_bit_differences += count_of_ones

	print(sum_of_bit_differences)

compute_bit_difference(sample_array_1)
compute_bit_difference(sample_array_2)

'''
solution

4
8

'''