def rstrip_whitespace(strings_list):
    """
    This function takes a list of strings and removes trailing whitespace
    from each string.
    """
    return [s.rstrip() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello world   ", "  python programming   ", "rstrip method example   ", "clean spaces    "]
    stripped_strings = rstrip_whitespace(input_strings)
    print("Input strings:", input_strings)
    print("Strings after removing trailing whitespace:", stripped_strings)
