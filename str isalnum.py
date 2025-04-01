def check_isalnum(strings_list):
    """
    This function takes a list of strings and checks if each string is alphanumeric.
    Returns a list of boolean values (True or False).
    """
    return [s.isalnum() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello123", "python!", "2023", "hello world", "ValidString"]
    results = check_isalnum(input_strings)
    print("Input strings:", input_strings)
    print("Is alphanumeric:", results)
