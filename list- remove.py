def remove_element_from_list(existing_list, element):
    """
    This function takes a list and an element, then removes the first occurrence
    of the element from the list using the remove() method.
    Returns the updated list.
    """
    if element in existing_list:
        existing_list.remove(element)
    else:
        print(f"Element '{element}' not found in the list.")
    return existing_list

# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry", "apple"]
    element_to_remove = "apple"
    updated_list = remove_element_from_list(my_list, element_to_remove)
    print("Original list:", ["apple", "banana", "cherry", "apple"])
    print(f"Removing '{element_to_remove}' from the list:")
    print("Updated list:", updated_list)
