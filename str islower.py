def check_islower(strings_list):
    """
    This function takes a list of strings and checks if each string is in all lowercase letters.
    Returns a list of boolean values (True or False).
    """
    return [s.islower() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello", "WORLD", "python3", "lowercase", "MixedCase"]
    results = check_islower(input_strings)
    print("Input strings:", input_strings)
    print("Are all characters lowercase:", results)