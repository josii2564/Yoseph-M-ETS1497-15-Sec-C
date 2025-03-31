# Check if all characters in a string are alphabetic using str.isalpha()
def is_alphabetic(input_string):
    """
    Checks whether the given string contains only alphabetic characters.

    Args:
    input_string (str): The string to check.

    Returns:
    bool: True if all characters in the string are alphabetic, False otherwise.
    """
    if not isinstance(input_string, str):
        raise ValueError("The input must be a string.")
    
    return input_string.isalpha()


# Example usage
string = "HelloWorld"
result = is_alphabetic(string)
print(f"Is '{string}' alphabetic? {result}")  # Output: Is 'HelloWorld' alphabetic? True

string = "Hello123"
result = is_alphabetic(string)
print(f"Is '{string}' alphabetic? {result}")  # Output: Is 'Hello123' alphabetic? False
