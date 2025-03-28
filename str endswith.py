def check_suffix(strings_list, suffix):
    """
    This function takes a list of strings and a suffix, then checks if each string
    ends with the given suffix. Returns a list of boolean values (True or False).
    """
    return [s.endswith(suffix) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello world", "python programming", "suffix method example", "ends well"]
    suffix_to_check = "ing"
    ends_with_suffix = check_suffix(input_strings, suffix_to_check)
    print("Input strings:", input_strings)
    print(f"Checking if strings end with '{suffix_to_check}':", ends_with_suffix)
