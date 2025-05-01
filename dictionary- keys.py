def get_dictionary_keys(input_dict):
    """
    Retrieves all the keys from the given dictionary using the keys() method.
    
    Parameters:
        input_dict (dict): The dictionary to extract keys from.
    
    Returns:
        list: A list containing all the keys in the dictionary.
    """
    return list(input_dict.keys())

if __name__ == "__main__":
    # Example dictionary
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    
    print("Dictionary:", my_dict)
    
    # Retrieving keys
    keys_list = get_dictionary_keys(my_dict)
    print("Keys in the dictionary:", keys_list)
