def replace_substrings(strings_list, old_substring, new_substring):
    """
    This function takes a list of strings, an old substring, and a new substring.
    It replaces all occurrences of the old substring with the new substring in each string.
    """
    return [s.replace(old_substring, new_substring) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello world", "python programming", "world of code"]
    old_substring = "world"
    new_substring = "universe"
    replaced_strings = replace_substrings(input_strings, old_substring, new_substring)
    print("Input strings:", input_strings)
    print(f"Replacing '{old_substring}' with '{new_substring}':", replaced_strings)
