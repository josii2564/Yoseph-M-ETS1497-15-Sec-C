def get_value_from_dict(input_dict, key, default_value=None):
    """
    Retrieves the value for a specified key from the dictionary using the get() method.
    
    Parameters:
        input_dict (dict): The dictionary to search in.
        key: The key whose value needs to be retrieved.
        default_value: The default value to return if the key is not found (optional).
    
    Returns:
        The value associated with the key if found, otherwise the default value.
    """
    return input_dict.get(key, default_value)

if __name__ == "__main__":
    # Example dictionary
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}

    print("Dictionary:", my_dict)
    
    # Retrieving values using get()
    key_to_find = "age"
    print(f"Value for key '{key_to_find}':", get_value_from_dict(my_dict, key_to_find))

    # Retrieving a key that doesn't exist, with a default value
    missing_key = "country"
    print(f"Value for missing key '{missing_key}':", get_value_from_dict(my_dict, missing_key, "Unknown"))
