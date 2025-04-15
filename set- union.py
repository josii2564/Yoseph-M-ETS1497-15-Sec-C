def union_of_sets(set1, set2):
    """
    Performs the union operation on two sets using the union() method.
    
    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.
    
    Returns:
        set: A set containing all unique elements from both sets.
    """
    return set1.union(set2)

if __name__ == "__main__":
    # Example sets
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    print("Set A:", set_a)
    print("Set B:", set_b)

    # Performing union operation
    union_set = union_of_sets(set_a, set_b)
    print("Union of Set A and Set B:", union_set)
