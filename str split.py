def split_strings(strings_list, delimiter):
    """
    This function takes a list of strings and a delimiter, then splits each string
    into a list of substrings based on the given delimiter.
    """
    return [s.split(delimiter) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["apple,banana,cherry", "dog,cat,bird", "red;green;blue"]
    delimiter = ","
    split_results = split_strings(input_strings, delimiter)
    print("Input strings:", input_strings)
    print(f"Strings after splitting by '{delimiter}':", split_results)
