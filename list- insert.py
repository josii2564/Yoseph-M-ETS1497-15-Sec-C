def insert_into_list(existing_list, index, element):
    """
    This function takes a list, an index, and an element, then inserts the element
    at the specified index using the insert() method.
    Returns the updated list.
    """
    existing_list.insert(index, element)
    return existing_list

# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    index_to_insert = 1
    element_to_insert = "orange"
    updated_list = insert_into_list(my_list, index_to_insert, element_to_insert)
    print("Original list:", ["apple", "banana", "cherry"])
    print(f"Inserting '{element_to_insert}' at index {index_to_insert}:")
    print("Updated list:", updated_list)
