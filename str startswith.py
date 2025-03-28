def check_start(strings_list, prefix):
    """
    This function takes a list of strings and a prefix, then checks if each string
    starts with the given prefix. Returns a list of boolean values (True or False).
    """
    return [s.startswith(prefix) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["apple pie", "banana split", "apricot tart", "peach cobbler"]
    prefix_to_check = "ap"
    starts_with_prefix = check_start(input_strings, prefix_to_check)
    print("Input strings:", input_strings)
    print(f"Checking if strings start with '{prefix_to_check}':", starts_with_prefix)
