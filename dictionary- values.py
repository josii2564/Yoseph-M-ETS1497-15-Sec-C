def get_dictionary_values(input_dict):
    """
    Retrieves all the values from the given dictionary using the values() method.
    
    Parameters:
        input_dict (dict): The dictionary to extract values from.
    
    Returns:
        list: A list containing all the values in the dictionary.
    """
    return list(input_dict.values())

if __name__ == "__main__":
    # Example dictionary
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    
    print("Dictionary:", my_dict)
    
    # Retrieving values
    values_list = get_dictionary_values(my_dict)
    print("Values in the dictionary:", values_list)
