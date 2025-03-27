def swapcase_strings(strings_list):
    """
    This function takes a list of strings and returns a new list where the case of each character is swapped.
    Uppercase becomes lowercase and vice versa.
    """
    return [s.swapcase() for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["Hello World", "Python Programming", "SwapCASE Method"]
    swapped_strings = swapcase_strings(input_strings)
    print("Original strings:", input_strings)
    print("Swapped case strings:", swapped_strings)
