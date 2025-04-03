def check_isupper(strings_list):
    """
    This function takes a list of strings and checks if each string is in all uppercase letters.
    Returns a list of boolean values (True or False).
    """
    return [s.isupper() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["HELLO", "World", "PYTHON", "UPPERCASE", "lowercase"]
    results = check_isupper(input_strings)
    print("Input strings:", input_strings)
    print("Are all characters uppercase:", results)
