def pop_element_from_list(existing_list, index=None):
    """
    This function takes a list and optionally an index, then removes and returns
    the element at the specified index using the pop() method.
    If no index is provided, the last element is removed.
    """
    if index is not None:
        if 0 <= index < len(existing_list):
            return existing_list.pop(index)
        else:
            print(f"Error: Index {index} is out of range.")
            return None
    else:
        return existing_list.pop()

# Example usage
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry", "date"]
    print("Original list:", my_list)
    
    # Removing an element by specifying an index
    removed_element = pop_element_from_list(my_list, 2)
    print(f"Removed element at index 2: {removed_element}")
    print("Updated list:", my_list)
    
    # Removing the last element
    removed_element = pop_element_from_list(my_list)
    print(f"Removed last element: {removed_element}")
    print("Updated list:", my_list)

