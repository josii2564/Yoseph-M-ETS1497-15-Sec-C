# Concatenating elements of a list using str.join() method
def concatenate_elements(element_list, separator):
    """
    Takes a list of strings and joins them into a single string using a specified separator.
    Args:
    element_list (list): A list of strings to be joined.
    separator (str): The separator to use for joining.
    
    Returns:
    str: The concatenated string.
    """
    if not all(isinstance(item, str) for item in element_list):
        raise ValueError("All elements in the list must be strings.")
    
    return separator.join(element_list)


# Example usage
elements = ["Hello", "world", "Python", "is", "fun"]
sep = " "
result = concatenate_elements(elements, sep)
print(result)  # Output: Hello world Python is fun
