def append_to_list(existing_list, new_elements):
    """
    This function takes an existing list and appends elements to it using the append() method.
    Returns the updated list.
    """
    for element in new_elements:
        existing_list.append(element)
    return existing_list

# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    elements_to_add = ["date", "elderberry", "fig"]
    updated_list = append_to_list(my_list, elements_to_add)
    print("Original list:", ["apple", "banana", "cherry"])
    print("Elements to append:", elements_to_add)
    print("Updated list:", updated_list)
