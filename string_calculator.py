def add(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split('\n', 1)
        numbers = numbers.replace(delimiter, ',')
    numbers = numbers.replace('\n', ',')
    num_list = numbers.split(',')
    return sum(int(num) for num in num_list)