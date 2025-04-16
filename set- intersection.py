def intersection_of_sets(set1, set2):
    """
    Finds the common elements of two sets using the intersection() method.
    
    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.
    
    Returns:
        set: A set containing the elements that are common to both sets.
    """
    return set1.intersection(set2)

if __name__ == "__main__":
    # Example sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print("Set A:", set_a)
    print("Set B:", set_b)

    # Performing intersection operation
    intersection_set = intersection_of_sets(set_a, set_b)
    print("Intersection of Set A and Set B:", intersection_set)
