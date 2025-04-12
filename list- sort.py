def sort_list(my_list, reverse=False):
    """
    Sorts the given list in ascending or descending order using the sort() method.
    
    Parameters:
        my_list (list): The list to sort.
        reverse (bool): If True, sorts the list in descending order. Defaults to False (ascending).
    
    Returns:
        list: The sorted list.
    """
    my_list.sort(reverse=reverse)
    return my_list

if __name__ == "__main__":
    # Example lists
    numbers = [5, 2, 9, 1, 5, 6]
    fruits = ["banana", "apple", "cherry", "date"]

    # Sorting numbers in ascending order
    print("Original numbers:", numbers)
    sorted_numbers = sort_list(numbers.copy())  # Using a copy to avoid modifying the original list
    print("Numbers sorted in ascending order:", sorted_numbers)

    # Sorting numbers in descending order
    sorted_numbers_desc = sort_list(numbers.copy(), reverse=True)
    print("Numbers sorted in descending order:", sorted_numbers_desc)

    # Sorting fruits in ascending order
    print("\nOriginal fruits:", fruits)
    sorted_fruits = sort_list(fruits.copy())
    print("Fruits sorted in ascending order:", sorted_fruits)

    # Sorting fruits in descending order
    sorted_fruits_desc = sort_list(fruits.copy(), reverse=True)
    print("Fruits sorted in descending order:", sorted_fruits_desc)
