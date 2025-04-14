def slice_list(my_list, start=None, end=None, step=None):
    """
    Extracts a slice from the given list using slicing syntax [start:end:step].
    
    Parameters:
        my_list (list): The list to slice.
        start (int): The starting index for slicing. Defaults to None (start of the list).
        end (int): The ending index for slicing (exclusive). Defaults to None (end of the list).
        step (int): The step size for slicing. Defaults to None (step of 1).
    
    Returns:
        list: A sliced portion of the original list.
    """
    return my_list[start:end:step]

if __name__ == "__main__":
    # Example list
    my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    print("Original list:", my_list)

    # Example 1: Slicing a sublist from index 1 to 4
    sliced_list_1 = slice_list(my_list, 1, 5)
    print("Sliced list (index 1 to 4):", sliced_list_1)

    # Example 2: Slicing with a step of 2
    sliced_list_2 = slice_list(my_list, 0, None, 2)
    print("Sliced list with step 2:", sliced_list_2)

    # Example 3: Slicing the last three elements
    sliced_list_3 = slice_list(my_list, -3, None)
    print("Last three elements:", sliced_list_3)
