def difference_of_sets(set1, set2):
    """
    Computes the difference between two sets using the difference() method.
    
    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.
    
    Returns:
        set: A set containing elements in set1 but not in set2.
    """
    return set1.difference(set2)

if __name__ == "__main__":
    # Example sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print("Set A:", set_a)
    print("Set B:", set_b)

    # Performing the difference operation
    difference_set = difference_of_sets(set_a, set_b)
    print("Difference of Set A and Set B (A - B):", difference_set)
