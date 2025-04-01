def check_isspace(strings_list):
    """
    This function takes a list of strings and checks if each string consists only of whitespace characters.
    Returns a list of boolean values (True or False).
    """
    return [s.isspace() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["   ", "hello world", "\t\n", "   text   ", ""]
    results = check_isspace(input_strings)
    print("Input strings:", input_strings)
    print("Is only whitespace:", results)
