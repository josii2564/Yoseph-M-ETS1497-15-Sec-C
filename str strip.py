def strip_whitespace(strings_list):
    """
    This function takes a list of strings and removes leading and trailing whitespace
    from each string.
    """
    return [s.strip() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["  hello world  ", "  python programming ", " strip method example ", "    clean spaces    "]
    stripped_strings = strip_whitespace(input_strings)
    print("Input strings:", input_strings)
    print("Strings after stripping:", stripped_strings)
