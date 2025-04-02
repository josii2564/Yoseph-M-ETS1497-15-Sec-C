def get_lengths(strings_list):
    """
    This function takes a list of strings and returns a list of their lengths
    using the len() method.
    """
    return [len(s) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello", "world", "Python", "length", ""]
    lengths = get_lengths(input_strings)
    print("Input strings:", input_strings)
    print("Lengths of strings:", lengths)
