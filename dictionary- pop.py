def pop_key_from_dict(input_dict, key, default_value=None):
    """
    Removes a specified key from the dictionary using the pop() method and returns its value.
    
    Parameters:
        input_dict (dict): The dictionary from which the key will be removed.
        key: The key to remove from the dictionary.
        default_value: The default value to return if the key is not found (optional).
    
    Returns:
        The value associated with the key if found, otherwise the default value.
    """
    return input_dict.pop(key, default_value)

if __name__ == "__main__":
    # Example dictionary
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}

    print("Dictionary before removal:", my_dict)
    
    # Removing a key
    key_to_remove = "age"
    removed_value = pop_key_from_dict(my_dict, key_to_remove)
    print(f"Removed key '{key_to_remove}', value:", removed_value)
    print("Updated dictionary:", my_dict)

    # Attempting to remove a key that doesn't exist, with a default value
    missing_key = "country"
    removed_value = pop_key_from_dict(my_dict, missing_key, "Unknown")
    print(f"Attempting to remove '{missing_key}', returned value:", removed_value)
    print("Final dictionary state:", my_dict)
