import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    # Check for custom delimiters
    if numbers.startswith("//"):
        delimiter_index = numbers.index("\n")
        delimiter_line = numbers[2:delimiter_index]
        numbers_part = numbers[delimiter_index + 1:]
        
        delimiters = parse_delimiters(delimiter_line)
        return sum_numbers(numbers_part, delimiters)
    
    # Default delimiters (comma and newline)
    return sum_numbers(numbers, [",", "\n"])

def parse_delimiters(delimiter_line: str):
    delimiters = []
    
    # Check for multiple delimiters enclosed in []
    if delimiter_line.startswith("[") and delimiter_line.endswith("]"):
        delimiter_matches = re.findall(r"\[(.*?)\]", delimiter_line)
        delimiters.extend(delimiter_matches)
    else:
        delimiters.append(delimiter_line)
    
    return delimiters

def sum_numbers(numbers: str, delimiters: list) -> int:
    # Create a regex pattern for splitting the numbers using the delimiters
    pattern = "|".join(map(re.escape, delimiters))
    number_list = re.split(pattern, numbers)
    
    # Remove empty values
    number_list = [num for num in number_list if num.strip()]
    
    # Check for negative numbers
    negative_numbers = [num for num in number_list if int(num) < 0]
    if negative_numbers:
        raise ValueError(f"negative numbers not allowed {', '.join(negative_numbers)}")
    
    # Filter out numbers greater than 1000
    number_list = [num for num in number_list if int(num) <= 1000]
    
    # Return the sum of valid numbers
    return sum(int(num) for num in number_list)