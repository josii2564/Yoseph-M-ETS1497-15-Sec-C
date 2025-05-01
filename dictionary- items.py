def get_dictionary_items(input_dict):
    """
    Retrieves all key-value pairs from the given dictionary using the items() method.
    
    Parameters:
        input_dict (dict): The dictionary to extract key-value pairs from.
    
    Returns:
        list: A list containing tuples of key-value pairs.
    """
    return list(input_dict.items())

if __name__ == "__main__":
    # Example dictionary
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    
    print("Dictionary:", my_dict)
    
    # Retrieving key-value pairs
    items_list = get_dictionary_items(my_dict)
    print("Key-value pairs in the dictionary:", items_list)
