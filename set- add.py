def add_to_set(existing_set, element):
    """
    Adds a single element to the given set using the add() method.
    
    Parameters:
        existing_set (set): The set to which the element will be added.
        element: The element to add to the set.
    
    Returns:
        set: The updated set with the new element added.
    """
    existing_set.add(element)
    return existing_set

if __name__ == "__main__":
    # Example set
    my_set = {1, 2, 3}
    print("Original set:", my_set)
    
    # Element to add
    element_to_add = 4
    updated_set = add_to_set(my_set, element_to_add)
    print(f"Adding '{element_to_add}' to the set:")
    print("Updated set:", updated_set)
    
    # Adding a duplicate element (no change since sets avoid duplicates)
    duplicate_element = 2
    updated_set = add_to_set(my_set, duplicate_element)
    print(f"Adding duplicate element '{duplicate_element}' to the set:")
    print("Updated set:", updated_set)
