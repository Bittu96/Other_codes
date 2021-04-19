arr = [1, 2]
sum_of_bit_differences = 0

# going through each and every pair

for i in arr:
    for j in arr:

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
