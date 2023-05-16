def descending_order(n):
    # Convert the integer to a string to be able to iterate over its digits
    n_str = str(n)

    # Convert the string to a list of characters (digits), sort it in reverse order
    sorted_digits = sorted(n_str, reverse=True)

    # Join the sorted digits back into a single string, and convert this string back to an integer
    sorted_n = int(''.join(sorted_digits))

    return sorted_n

print(sort_digits_descending(42145))      # Output: 54421
print(sort_digits_descending(145263))     # Output: 654321
print(sort_digits_descending(123456789))  # Output: 987654321

#My first Kata
