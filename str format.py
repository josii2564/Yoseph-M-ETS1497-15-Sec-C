def generate_formatted_strings(names, scores):
    """
    This function takes two lists: names and scores, and formats them into a readable string
    using the str.format() method.
    Returns a list of formatted strings.
    """
    return ["Name: {}, Score: {}".format(name, score) for name, score in zip(names, scores)]

# Example usage
if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    formatted_strings = generate_formatted_strings(names, scores)
    print("Formatted Output:")
    for string in formatted_strings:
        print(string)

