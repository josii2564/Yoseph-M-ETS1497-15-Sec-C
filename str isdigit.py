# Check if a string contains only numeric characters using str.isdigit()
def is_numeric(input_string):
    """
    Checks whether the given string contains only numeric characters.

    Args:
    input_string (str): The string to check.

    Returns:
    bool: True if all characters in the string are numeric, False otherwise.
    """
    if not isinstance(input_string, str):
        raise ValueError("The input must be a string.")
    
    return input_string.isdigit()


# Example usage
string1 = "12345"
result1 = is_numeric(string1)
print(f"Is '{string1}' numeric? {result1}")  # Output: Is '12345' numeric? True

string2 = "123abc"
result2 = is_numeric(string2)
print(f"Is '{string2}' numeric? {result2}")  # Output: Is '123abc' numeric? False

