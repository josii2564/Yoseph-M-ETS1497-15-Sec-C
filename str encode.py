def encode_strings(strings_list, encoding="utf-8"):
    """
    This function takes a list of strings and encodes them into byte strings
    using the specified encoding format (default is UTF-8).
    Returns a list of encoded byte strings.
    """
    return [s.encode(encoding) for s in strings_list]

# Example usage
if __name__ == "__main__":
    input_strings = ["hello", "world", "Python", "encode", "😊"]
    encoded_strings = encode_strings(input_strings, "utf-8")
    print("Input strings:", input_strings)
    print("Encoded byte strings:", encoded_strings)
