def find_substrings(strings_list, substring):
    """
    This function takes a list of strings and a substring, then returns a list of
    indices where the substring first appears in each string. If the substring is not found, it returns -1.
    """
    return [s.find(substring) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello world", "python programming", "find method example"]
    search_substring = "o"
    indices = find_substrings(input_strings, search_substring)
    print("Input strings:", input_strings)
    print(f"Searching for substring '{search_substring}':", indices)

