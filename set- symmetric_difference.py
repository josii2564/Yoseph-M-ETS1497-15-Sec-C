def symmetric_difference_of_sets(set1, set2):
    """
    Computes the symmetric difference between two sets using the symmetric_difference() method.
    
    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.
    
    Returns:
        set: A set containing elements that are in either set1 or set2, but not in both.
    """
    return set1.symmetric_difference(set2)

if __name__ == "__main__":
    # Example sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print("Set A:", set_a)
    print("Set B:", set_b)

    # Performing the symmetric difference operation
    symmetric_diff_set = symmetric_difference_of_sets(set_a, set_b)
    print("Symmetric Difference of Set A and Set B:", symmetric_diff_set)
