def remove_from_set(existing_set, element):
    """
    Removes a specific element from the given set using the remove() method.
    
    Parameters:
        existing_set (set): The set from which the element will be removed.
        element: The element to remove from the set.
    
    Returns:
        set: The updated set with the element removed. If the element is not found, an error message is displayed.
    """
    try:
        existing_set.remove(element)
        print(f"Element '{element}' removed successfully.")
    except KeyError:
        print(f"Error: Element '{element}' not found in the set.")
    return existing_set

if __name__ == "__main__":
    # Example set
    my_set = {1, 2, 3, 4, 5}
    print("Original set:", my_set)

    # Removing an element
    element_to_remove = 3
    updated_set = remove_from_set(my_set, element_to_remove)
    print("Updated set after removal:", updated_set)

    # Attempting to remove an element not in the set
    non_existent_element = 6
    updated_set = remove_from_set(my_set, non_existent_element)
    print("Updated set after trying to remove a non-existent element:", updated_set)
