def lstrip_whitespace(strings_list):
    """
    This function takes a list of strings and removes leading whitespace
    from each string.
    """
    return [s.lstrip() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["  hello world", "   python programming", "  lstrip method example", "   clean spaces"]
    stripped_strings = lstrip_whitespace(input_strings)
    print("Input strings:", input_strings)
    print("Strings after removing leading whitespace:", stripped_strings)
