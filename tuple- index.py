def find_index_in_tuple(input_tuple, value):
    """
    This function finds the index of the first occurrence of a specified value in a tuple
    using the index() method.
    
    Parameters:
        input_tuple (tuple): The tuple to search in.
        value: The value whose index needs to be found.
    
    Returns:
        int: The index of the first occurrence of the value in the tuple.
             Returns None if the value does not exist in the tuple.
    """
    try:
        return input_tuple.index(value)
    except ValueError:
        print(f"Value '{value}' not found in the tuple.")
        return None

if __name__ == "__main__":
    # Example tuple
    my_tuple = (1, 2, 3, 1, 4, 1, 5, 6, 1)
    value_to_find = 4

    print("Tuple:", my_tuple)
    print(f"Value to find: {value_to_find}")
    index = find_index_in_tuple(my_tuple, value_to_find)
    if index is not None:
        print(f"Index of the first occurrence of {value_to_find}: {index}")
    else:
        print(f"{value_to_find} is not in the tuple.")
