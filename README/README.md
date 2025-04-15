
                               for str.lower method

# Convert String to Lowercase Using Python

This Python script demonstrates the use of the `str.lower()` method to convert a string to lowercase. The `lower()` method is a built-in string method in Python that creates a new string with all characters in lowercase.

## Features

- Converts uppercase letters in a string to lowercase.
- Includes a reusable function: `convert_to_lowercase(input_string)`.

## Usage Instructions

1. Copy the Python code into a file (e.g., `string_to_lowercase.py`).
2. Run the file using a Python interpreter.
3. The output will display both the original string and its lowercase counterpart.

## Example Execution

Input: `"HELLO, WORLD!"`  
Output: "hello, world"





                          for str.upper method              

   # Convert String to Uppercase Using Python

This Python script demonstrates the use of the `str.upper()` method to convert a string to uppercase. The `upper()` method is a built-in string method in Python that creates a new string with all characters converted to uppercase.

## Features

- Converts lowercase letters in a string to uppercase.
- Includes a reusable function: `convert_to_uppercase(input_string)`.

## Usage Instructions

1. Copy the Python code into a file (e.g., `string_to_uppercase.py`).
2. Run the file using a Python interpreter.
3. The output will display both the original string and its uppercase counterpart.

## Example Execution

Input: `"hello, world!"`  
Output: "HELLO, WORLD"




                      
                        for str.title method
                    
# Convert String to Title Case Using Python

This Python script demonstrates the use of the `str.title()` method to convert a string to title case. The `title()` method is a built-in Python string method that capitalizes the first letter of each word in a string while converting the rest to lowercase.

## Features

- Converts a given string to title case.
- Includes a reusable function: `convert_to_title_case(input_string)`.

## Usage Instructions

1. Copy the Python code into a file (e.g., `string_to_title_case.py`).
2. Run the file using a Python interpreter.
3. The output will display both the original string and its title-cased counterpart.

## Example Execution

Input: `"hello, python world!"`  
Output: "Hello, Python World"


           
                       
                        for str.capitalize method

## Overview
This Python script provides a simple function to capitalize the first character of each string in a list. It uses the built-in `str.capitalize()` method to achieve this, ensuring the remaining characters in the string are in lowercase.

## Features
- Takes a list of strings as input.
- Returns a new list with each string capitalized.

## Usage
1. Provide a list of strings to the `capitalize_strings` function.
2. Run the script to see the original and capitalized strings printed to the console.

### Example Input
```python
["hello", "world", "python", "programming"]  




                         for str.swapcase method 

## Overview
This Python script provides a simple function to swap the case of each character in a list of strings. It uses the built-in `str.swapcase()` method to achieve this.

## Features
- Takes a list of strings as input.
- Returns a new list with each character's case swapped.

## Usage
1. Provide a list of strings to the `swapcase_strings` function.
2. Run the script to see the original and swapped case strings printed to the console.

### Example Input
```python
["Hello World", "Python Programming", "SwapCASE Method"]
                    


                      
                        for str.find method

## Overview
This Python script demonstrates the use of the `str.find()` method to locate the index of the first occurrence of a specified substring within a list of strings. If the substring is not found, the method returns `-1`.

## Features
- Accepts a list of strings and a substring to search for.
- Returns a list of indices corresponding to the position of the substring's first occurrence in each string.

## Usage
1. Provide a list of strings and the substring to search for to the `find_substrings` function.
2. Run the script to see the indices of the substring's first occurrence in each string.

### Example Input
```python
["hello world", "python programming", "find method example"]
Substring to search: "o"



                          
                           for str.index method

## Overview
This Python script demonstrates the use of the `str.index()` method to locate the index of the first occurrence of a specified substring within a list of strings. If the substring is not found, the script raises a `ValueError` and provides a message indicating where it couldn't be found.

## Features
- Accepts a list of strings and a substring to search for.
- Returns a list of indices corresponding to the position of the substring's first occurrence in each string.
- Handles cases where the substring is not found and provides meaningful messages.

## Usage
1. Provide a list of strings and the substring to search for to the `index_substrings` function.
2. Run the script to see the indices of the substring's first occurrence or meaningful messages for strings where the substring is absent.

### Example Input
```python
["hello world", "python programming", "index method example"]
Substring to search: "o"
                       



                       for str.startswith method

## Overview
This Python script demonstrates the use of the `str.startswith()` method to check if each string in a list starts with a given prefix. The script returns a list of boolean values (True or False) indicating the result for each string.

## Features
- Takes a list of strings and a prefix as input.
- Returns a list of boolean values to indicate whether each string starts with the specified prefix.

## Usage
1. Provide a list of strings and the prefix to check for to the `check_start` function.
2. Run the script to see which strings start with the given prefix.

### Example Input
```python
["apple pie", "banana split", "apricot tart", "peach cobbler"]
Prefix to check: "ap" 



                        
                        for str.endswith method

## Overview
This Python script demonstrates the use of the `str.endswith()` method to check if each string in a list ends with a given suffix. The script returns a list of boolean values (True or False) indicating the result for each string.

## Features
- Accepts a list of strings and a suffix to check.
- Returns a list of boolean values to indicate whether each string ends with the specified suffix.

## Usage
1. Provide a list of strings and the suffix to check for to the `check_suffix` function.
2. Run the script to see which strings end with the given suffix.

### Example Input
```python
["hello world", "python programming", "suffix method example", "ends well"]
Suffix to check: "ing"




                       for str.count method

## Overview
This Python script demonstrates the use of the `str.count()` method to count the occurrences of a specific substring within a list of strings. It provides a simple and efficient way to analyze text for repeated patterns.

## Features
- Accepts a list of strings and a substring to search for.
- Returns a list of integers representing the count of the substring in each string.

## Usage
1. Provide a list of strings and the substring to search for to the `count_substrings` function.
2. Run the script to see the count of the substring in each string.

### Example Input
```python
["banana", "bandana", "cabana", "banana bread"]
Substring to search: "ana"
                     

                         
                        
                         for str.replace method

## Overview
This Python script demonstrates the use of the `str.replace()` method to replace occurrences of a substring within a list of strings. It enables you to modify text systematically by substituting one substring with another.

## Features
- Accepts a list of strings, an old substring, and a new substring to replace it with.
- Returns a list of strings where all occurrences of the old substring are replaced with the new substring.

## Usage
1. Provide a list of strings, an old substring, and a new substring to the `replace_substrings` function.
2. Run the script to see the modified list of strings.

### Example Input
```python
["hello world", "python programming", "world of code"]
Old substring: "world"
New substring: "universe"
                    



                            for str.strip method

## Overview
This Python script demonstrates the use of the `str.strip()` method to remove leading and trailing whitespace from strings in a list. It's a convenient utility for cleaning up text data.

## Features
- Accepts a list of strings with potential leading or trailing whitespace.
- Returns a list of cleaned strings where the whitespace has been removed.

## Usage
1. Provide a list of strings to the `strip_whitespace` function.
2. Run the script to see the cleaned strings without leading or trailing whitespace.

### Example Input
```python
["  hello world  ", "  python programming ", " strip method example ", "    clean spaces    "]                          

     
               
                        for str.lstrip method

## Overview
This Python script demonstrates the use of the `str.lstrip()` method to remove leading whitespace from strings in a list. It is a convenient tool for cleaning up text data efficiently.

## Features
- Accepts a list of strings with potential leading whitespace.
- Returns a list of cleaned strings where the leading whitespace has been removed.

## Usage
1. Provide a list of strings to the `lstrip_whitespace` function.
2. Run the script to see the cleaned strings without leading whitespace.

### Example Input
```python
["  hello world", "   python programming", "  lstrip method example", "   clean spaces"]
     Input strings: ["  hello world", "   python programming", "  lstrip method example", "   clean spaces"]
Strings after removing leading whitespace: ["hello world", "python programming", "lstrip method example", "clean spaces"]
        


                       
                          for str.rstrip method

## Overview
This Python script demonstrates the use of the `str.rstrip()` method to remove trailing whitespace from strings in a list. It's a helpful utility for cleaning up text data efficiently.

## Features
- Accepts a list of strings with potential trailing whitespace.
- Returns a list of cleaned strings where the trailing whitespace has been removed.

## Usage
1. Provide a list of strings to the `rstrip_whitespace` function.
2. Run the script to see the cleaned strings without trailing whitespace.

### Example Input
```python
["hello world   ", "  python programming   ", "rstrip method example   ", "clean spaces    "]
Input strings: ["hello world   ", "  python programming   ", "rstrip method example   ", "clean spaces    "]
Strings after removing trailing whitespace: ["hello world", "  python programming", "rstrip method example", "clean spaces"]


                             
                             for str.split method

## Overview
This Python script demonstrates the use of the `str.split()` method to break strings into substrings based on a specified delimiter. It's a simple and effective tool for processing text data.

## Features
- Accepts a list of strings and a delimiter.
- Splits each string into substrings based on the given delimiter.
- Returns a list of lists containing the substrings.

## Usage
1. Provide a list of strings and a delimiter to the `split_strings` function.
2. Run the script to see the results of the splitting operation.

### Example Input
```python
["apple,banana,cherry", "dog,cat,bird", "red;green;blue"]
Delimiter: ","
Input strings: ["apple,banana,cherry", "dog,cat,bird", "red;green;blue"]
Strings after splitting by ',': [["apple", "banana", "cherry"], ["dog", "cat", "bird"], ["red;green;blue"]]


                       
                           for str.join method

This project provides a simple Python function to demonstrate the usage of the `str.join()` method for concatenating elements of a list into a single string.

## Overview

The `str.join()` method is a built-in function in Python that allows you to join the elements of a list into a single string, separated by a specified delimiter. This is particularly useful when working with text processing tasks.

## Features

- Concatenate elements of a list using a specified separator.
- Ensures all elements in the list are strings before joining.
- Includes error handling for type validation.

## Usage

### Example Code
```python
elements = ["Hello", "world", "Python", "is", "fun"]
separator = " "
result = concatenate_elements(elements, separator)
print(result)  # Output: Hello world Python is fun


                     
                            for str.isalpha method

This project provides a Python function to demonstrate the usage of the `str.isalpha()` method for checking whether all characters in a string are alphabetic.

## Overview

The `str.isalpha()` method is a built-in Python function that returns `True` if all characters in a string are alphabetic and the string is not empty. It is commonly used for text validation and string processing tasks.

## Features

- Verifies if a string contains only alphabetic characters.
- Includes error handling for non-string inputs.

## Usage

### Example Code
```python
string = "HelloWorld"
result = is_alphabetic(string)
print(f"Is '{string}' alphabetic? {result}")  # Output: Is 'HelloWorld' alphabetic? True

string = "Hello123"
result = is_alphabetic(string)
print(f"Is '{string}' alphabetic? {result}")  # Output: Is 'Hello123' alphabetic? False
                      

         
                           for str.isdigit method

This project provides a Python function to demonstrate the usage of the `str.isdigit()` method for checking if a string contains only numeric characters.

## Overview

The `str.isdigit()` method is a built-in Python function that returns `True` if all characters in a string are numeric and the string is not empty. This method is especially useful for input validation or preprocessing data in numeric operations.

## Features

- Validates if a string contains only numeric characters.
- Includes error handling for non-string inputs.

## Usage

### Example Code
```python
string1 = "12345"
result1 = is_numeric(string1)
print(f"Is '{string1}' numeric? {result1}")  # Output: Is '12345' numeric? True

string2 = "123abc"
result2 = is_numeric(string2)
print(f"Is '{string2}' numeric? {result2}")  # Output: Is '123abc' numeric? False
 


                          for str.isalnum method

## Overview
This Python script demonstrates the use of the `str.isalnum()` method to verify if a string consists of alphanumeric characters. The script processes a list of strings and outputs a corresponding list of boolean values indicating the result.

## Features
- Accepts a list of strings.
- Uses the `str.isalnum()` method to check if each string contains only alphanumeric characters (letters and digits).
- Returns a list of boolean values.

## Usage
1. Provide a list of strings to the `check_isalnum` function.
2. Run the script to see the results indicating whether each string is alphanumeric.

### Example Input
```python
["hello123", "python!", "2023", "hello world", "ValidString"]
Input strings: ["hello123", "python!", "2023", "hello world", "ValidString"]
Is alphanumeric: [True, False, True, False, True]


                         
                           for str.isspace method

## Overview
This Python script demonstrates the use of the `str.isspace()` method to check if a string consists entirely of whitespace characters. The script processes a list of strings and outputs a list of boolean values indicating the results.

## Features
- Accepts a list of strings as input.
- Uses the `str.isspace()` method to check if each string contains only whitespace characters.
- Returns a list of boolean values.

## Usage
1. Provide a list of strings to the `check_isspace` function.
2. Run the script to determine which strings contain only whitespace.

### Example Input
```python
["   ", "hello world", "\t\n", "   text   ", ""]
Input strings: ["   ", "hello world", "\t\n", "   text   ", ""]
Is only whitespace: [True, False, True, False, False]


                  
                      for str.format method

## Overview
This Python script demonstrates the use of the `str.format()` method to create readable and structured strings by inserting dynamic values. It formats names and scores into a readable format, making it an essential tool for formatting output in Python programs.

## Features
- Takes two lists as input: one containing names and another containing scores.
- Uses the `str.format()` method to dynamically insert values into a string.
- Outputs a list of formatted strings.

## Usage
1. Provide two lists: one for names and one for scores.
2. Run the script to generate formatted strings displaying the name and score of each individual.

### Example Input
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
Formatted Output:
Name: Alice, Score: 85
Name: Bob, Score: 92
Name: Charlie, Score: 78



                            for f-strings method

## Overview
This Python script demonstrates the use of Python's f-strings to format strings dynamically. F-strings were introduced in Python 3.6 and provide a clean, efficient way to insert variables into strings, making your code more readable and concise.

## Features
- Accepts two lists as input: one containing names and another containing scores.
- Uses f-strings to format the output dynamically.
- Outputs a list of formatted strings showing the name and score of each individual.

## Usage
1. Provide two lists: one for names and one for scores.
2. Run the script to generate formatted strings using f-strings.

### Example Input
```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 76]



                             for len method

## Overview
This Python script demonstrates the use of the built-in `len()` method to calculate the length of strings. The script processes a list of strings and outputs their lengths.

## Features
- Accepts a list of strings as input.
- Uses the `len()` method to compute the length of each string.
- Handles strings of any length, including empty strings.
- Outputs a list of lengths corresponding to each input string.

## Usage
1. Provide a list of strings to the `get_lengths` function.
2. Run the script to calculate and view the lengths of the strings.

### Example Input
```python
["hello", "world", "Python", "length", ""]
Input strings: ["hello", "world", "Python", "length", ""]
Lengths of strings: [5, 5, 6, 6, 0]



     
                           for str.encode method

## Overview
This Python script demonstrates the use of the `str.encode()` method to convert strings into byte strings using a specified encoding format. By default, it uses UTF-8 encoding.

## Features
- Accepts a list of strings as input.
- Encodes each string into a byte string using the `str.encode()` method.
- Supports specifying different encoding formats (e.g., UTF-8, ASCII).

## Usage
1. Provide a list of strings to the `encode_strings` function.
2. Optionally specify the encoding format (default is UTF-8).
3. Run the script to encode the strings into byte strings.

### Example Input
```python
["hello", "world", "Python", "encode", "😊"]
Input strings: ["hello", "world", "Python", "encode", "😊"]
Encoded byte strings: [b'hello', b'world', b'Python', b'encode', b'\xf0\x9f\x98\x8a']



                         for str.islower method

## Overview
This Python script demonstrates the use of the `str.islower()` method to check whether a string contains only lowercase letters. It processes a list of strings and outputs a corresponding list of boolean values.

## Features
- Accepts a list of strings as input.
- Uses the `str.islower()` method to check if each string is entirely lowercase.
- Returns a list of boolean values (True or False).

## Usage
1. Provide a list of strings to the `check_islower` function.
2. Run the script to see which strings are in all lowercase.

### Example Input
```python
["hello", "WORLD", "python3", "lowercase", "MixedCase"]
Input strings: ["hello", "WORLD", "python3", "lowercase", "MixedCase"]
Are all characters lowercase: [True, False, False, True, False]

      

                        for str.isupper method`

## Overview
This Python script demonstrates the use of the `str.isupper()` method to check whether a string contains only uppercase letters. It processes a list of strings and outputs a corresponding list of boolean values.

## Features
- Accepts a list of strings as input.
- Uses the `str.isupper()` method to check if each string is entirely uppercase.
- Returns a list of boolean values (True or False).

## Usage
1. Provide a list of strings to the `check_isupper` function.
2. Run the script to see which strings are in all uppercase.

### Example Input
```python
["HELLO", "World", "PYTHON", "UPPERCASE", "lowercase"]
Input strings: ["HELLO", "World", "PYTHON", "UPPERCASE", "lowercase"]
Are all characters uppercase: [True, False, True, True, False]



                
                          for list-append() method

## Overview
This Python script demonstrates how to use the `append()` method to add elements to the end of a list. The `append()` method is a simple and effective way to dynamically expand a list.

## Features
- Accepts an existing list and a list of new elements to append.
- Uses the `append()` method to add each new element to the existing list.
- Returns the updated list after appending all elements.

## Usage
1. Provide an existing list and a list of elements to append.
2. Run the script to append the new elements to the existing list.

### Example Input
```python
Original list: ["apple", "banana", "cherry"]
Elements to append: ["date", "elderberry", "fig"]
Original list: ["apple", "banana", "cherry"]
Elements to append: ["date", "elderberry", "fig"]
Updated list: ["apple", "banana", "cherry", "date", "elderberry", "fig"]



                           for list-insert() method

## Overview
This Python script demonstrates how to use the `insert()` method to add elements at specific positions in a list. The `insert()` method provides an easy way to dynamically modify the structure of lists.

## Features
- Accepts an existing list, an index, and an element.
- Uses the `insert()` method to add the element at the specified index.
- Returns the updated list after insertion.

## Usage
1. Provide an existing list, the index where the element should be inserted, and the element itself.
2. Run the script to insert the element into the list.

### Example Input
```python
Original list: ["apple", "banana", "cherry"]
Index to insert: 1
Element to insert: "orange"
Original list: ["apple", "banana", "cherry"]
Inserting 'orange' at index 1:
Updated list: ["apple", "orange", "banana", "cherry"]



                           for list-remove() method

## Overview
This Python script demonstrates how to use the `remove()` method to eliminate the first occurrence of a specified element from a list. The `remove()` method is an efficient way to modify lists dynamically.

## Features
- Accepts an existing list and an element to remove.
- Uses the `remove()` method to eliminate the element.
- Handles cases where the element is not found in the list.

## Usage
1. Provide an existing list and the element you want to remove.
2. Run the script to remove the specified element from the list.

### Example Input
```python
Original list: ["apple", "banana", "cherry", "apple"]
Element to remove: "apple"
Original list: ["apple", "banana", "cherry", "apple"]
Removing 'apple' from the list:
Updated list: ["banana", "cherry", "apple"]



                              for list-pop() method

## Overview
This Python script showcases the functionality of the `pop()` method, which allows you to remove an element from a list by specifying its index or defaulting to the last element. The method also returns the removed element, providing a way to retrieve and process it.

## Features
- Removes an element at a specified index from the list using the `pop()` method.
- Removes the last element if no index is provided.
- Returns the removed element.
- Handles cases where the index is out of range.

## Usage
1. Provide an existing list and optionally an index for the element to remove.
2. Run the script to remove and retrieve the specified or last element from the list.

### Example Input
```python
Original list: ["apple", "banana", "cherry", "date"]
Index to remove: 2
Original list: ["apple", "banana", "cherry", "date"]
Removed element at index 2: cherry
Updated list: ["apple", "banana", "date"]
Removed last element: date
Updated list: ["apple", "banana"]

                         

                         for list-len() method

## Overview
This Python script demonstrates how to use the built-in `len()` method to calculate the number of elements in a list. The `len()` method is a fundamental tool for working with lists and other data structures in Python.

## Features
- Accepts a list as input.
- Uses the `len()` method to calculate the number of elements in the list.
- Outputs the length of the list.

## Usage
1. Provide a list as input to the `get_list_length` function.
2. Run the script to calculate and display the length of the list.

### Example Input
```python
["apple", "banana", "cherry", "date"]
List: ["apple", "banana", "cherry", "date"]
Length of the list: 4


                            
                            for list-sort() method

## Overview
This Python script demonstrates the use of the built-in `sort()` method to sort lists. It allows sorting in both ascending (default) and descending order by setting the `reverse` parameter.

## Features
- Sorts a list of numbers or strings in ascending order.
- Can also sort in descending order by setting the `reverse` parameter to `True`.
- Keeps the original list intact by working on a copy.

## Usage
1. Provide a list to be sorted.
2. Call the `sort_list()` function, optionally setting `reverse=True` for descending order.
3. View the sorted results.

### Example Input
```python
numbers = [5, 2, 9, 1, 5, 6]
fruits = ["banana", "apple", "cherry", "date"]
Original numbers: [5, 2, 9, 1, 5, 6]
Numbers sorted in ascending order: [1, 2, 5, 5, 6, 9]
Numbers sorted in descending order: [9, 6, 5, 5, 2, 1]

Original fruits: ["banana", "apple", "cherry", "date"]
Fruits sorted in ascending order: ["apple", "banana", "cherry", "date"]
Fruits sorted in descending order: ["date", "cherry", "banana", "apple"]
                


                             for list-slicing method 

## Overview
This Python script demonstrates how to use slicing operations to extract portions of a list. Slicing provides a powerful way to work with sublists by specifying start, end, and step indices.

## Features
- Extracts sublists using slicing syntax `[start:end:step]`.
- Allows flexible operations such as:
  - Slicing specific ranges.
  - Skipping elements using a step size.
  - Using negative indices for slicing from the end of the list.

## Slicing Syntax
- `my_list[start:end:step]`
  - `start` (optional): The index to start slicing. Defaults to the beginning of the list if not specified.
  - `end` (optional): The index to stop slicing (exclusive). Defaults to the end of the list if not specified.
  - `step` (optional): The step size (interval) for slicing. Defaults to 1 if not specified.

## Usage
1. Define a list to slice.
2. Call the `slice_list()` function with the desired `start`, `end`, and `step` values.
3. Run the script to view the sliced portions of the list.

### Example Input
```python
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
Original list: ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
Sliced list (index 1 to 4): ["banana", "cherry", "date", "elderberry"]
Sliced list with step 2: ["apple", "cherry", "elderberry", "grape"]
Last three elements: ["elderberry", "fig", "grape"]



                         for tuple-count() method

## Overview
This Python script demonstrates how to use the built-in `count()` method to find the number of occurrences of a specified value in a tuple. Tuples are immutable, ordered collections, and this method is useful for analyzing their contents.

## Features
- Accepts a tuple and a value as input.
- Uses the `count()` method to calculate the number of occurrences of the value in the tuple.
- Returns and displays the result.

## Usage
1. Define a tuple and the value you want to count.
2. Call the `count_occurrences_in_tuple()` function with the tuple and value as arguments.
3. Run the script to view the result.

### Example Input
```python
Tuple: (1, 2, 3, 1, 4, 1, 5, 6, 1)
Value to count: 1
Tuple: (1, 2, 3, 1, 4, 1, 5, 6, 1)
Value to count: 1
Number of occurrences of 1: 4
     


                              for tuple-index() method

## Overview
This Python script demonstrates how to use the built-in `index()` method to find the index of the first occurrence of a specified value in a tuple. Tuples are immutable and ordered, making the `index()` method a useful tool for locating elements efficiently.

## Features
- Accepts a tuple and a value to search for.
- Uses the `index()` method to find the index of the first occurrence of the value in the tuple.
- Handles cases where the value is not found by displaying a user-friendly message.

## Usage
1. Provide a tuple and a value to search for.
2. Call the `find_index_in_tuple()` function to find the index of the value.
3. Run the script to view the index or handle cases where the value does not exist in the tuple.

### Example Input
```python
Tuple: (1, 2, 3, 1, 4, 1, 5, 6, 1)
Value to find: 4
Tuple: (1, 2, 3, 1, 4, 1, 5, 6, 1)
Value to find: 4
Index of the first occurrence of 4: 4



                          for set-add() method

## Overview
This Python script demonstrates how to use the `add()` method to add elements to a set. Sets are unordered collections of unique elements, and the `add()` method efficiently adds elements while preserving the uniqueness property.

## Features
- Adds a single element to the set using the `add()` method.
- Handles duplicate elements gracefully (duplicates are ignored in sets).
- Returns and displays the updated set.

## Usage
1. Define a set and an element to add.
2. Call the `add_to_set()` function with the set and element as arguments.
3. Run the script to view the updated set.

### Example Input
```python
Original set: {1, 2, 3}
Element to add: 4
Original set: {1, 2, 3}
Adding '4' to the set:
Updated set: {1, 2, 3, 4}

Adding duplicate element '2' to the set:
Updated set: {1, 2, 3, 4}



                              for set-remove() method

## Overview
This Python script demonstrates how to use the `remove()` method to delete specific elements from a set. Sets are unordered collections of unique elements, and the `remove()` method enables efficient removal of items.

## Features
- Removes a specified element from the set.
- Handles cases where the element does not exist, displaying an error message.
- Modifies the original set directly.

## Usage
1. Define a set and specify the element to remove.
2. Call the `remove_from_set()` function with the set and element as arguments.
3. Run the script to view the updated set and handle missing elements gracefully.

### Example Input
```python
Original set: {1, 2, 3, 4, 5}
Element to remove: 3
Original set: {1, 2, 3, 4, 5}
Element '3' removed successfully.
Updated set after removal: {1, 2, 4, 5}

Error: Element '6' not found in the set.
Updated set after trying to remove a non-existent element: {1, 2, 4, 5}



                      for set-union() method

# Python Script: Union of Sets Using the `union()` Method

## Overview
This Python script showcases the use of the `union()` method to combine two sets into a single set containing all unique elements. The union operation is a fundamental feature of Python sets.

## Features
- Combines two sets and returns all unique elements.
- Handles sets with overlapping elements by ensuring no duplicates appear in the result.
- Demonstrates set operations in a clear and concise manner.

## Usage
1. Define two sets to perform the union operation.
2. Call the `union_of_sets()` function with the two sets as arguments.
3. Run the script to view the union of the sets.

### Example Input
```python
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}
Union of Set A and Set B: {1, 2, 3, 4, 5, 6}
