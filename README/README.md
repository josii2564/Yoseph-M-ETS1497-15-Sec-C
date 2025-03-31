
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
