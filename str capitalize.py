def capitalize_strings(strings_list):
    """
    This function takes a list of strings and returns a new list with each string capitalized.
    """
    return [s.capitalize() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello", "world", "python", "programming"]
    capitalized_strings = capitalize_strings(input_strings)
    print("Original strings:", input_strings)
    print("Capitalized strings:", capitalized_strings)
