def count_occurrences_in_tuple(input_tuple, value):
    """
    This function counts the number of occurrences of a specified value in a tuple
    using the count() method.
    
    Parameters:
        input_tuple (tuple): The tuple to search in.
        value: The value whose occurrences need to be counted.
    
    Returns:
        int: The number of occurrences of the value in the tuple.
    """
    return input_tuple.count(value)

if __name__ == "__main__":
    # Example tuple
    my_tuple = (1, 2, 3, 1, 4, 1, 5, 6, 1)
    value_to_count = 1

    print("Tuple:", my_tuple)
    print(f"Value to count: {value_to_count}")
    occurrences = count_occurrences_in_tuple(my_tuple, value_to_count)
    print(f"Number of occurrences of {value_to_count}: {occurrences}")
