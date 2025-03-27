def convert_to_uppercase(input_string):
    uppercase_string = input_string.upper()
    return uppercase_string

# Example usage
if __name__ == "__main__":
    original_string = "hello, world!"
    print("Original String:", original_string)

    uppercase_result = convert_to_uppercase(original_string)
    print("Uppercase String:", uppercase_result)