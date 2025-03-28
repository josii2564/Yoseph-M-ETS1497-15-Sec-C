def index_substrings(strings_list, substring):
    """
    This function takes a list of strings and a substring, then returns a list of
    indices where the substring first appears in each string. Raises a ValueError if the substring is not found.
    """
    indices = []
    for s in strings_list:
        try:
            indices.append(s.index(substring))
        except ValueError:
            indices.append("Substring not found in: " + s)
    return indices

# Example usage
if __name__ == "__main__":
    input_strings = ["hello world", "python programming", "index method example"]
    search_substring = "o"
    indices = index_substrings(input_strings, search_substring)
    print("Input strings:", input_strings)
    print(f"Searching for substring '{search_substring}':", indices)
