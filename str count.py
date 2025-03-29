def count_substrings(strings_list, substring):
    """
    This function takes a list of strings and a substring, then returns a list of
    counts for how many times the substring appears in each string.
    """
    return [s.count(substring) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["banana", "bandana", "cabana", "banana bread"]
    search_substring = "ana"
    counts = count_substrings(input_strings, search_substring)
    print("Input strings:", input_strings)
    print(f"Count of substring '{search_substring}' in each string:", counts)
