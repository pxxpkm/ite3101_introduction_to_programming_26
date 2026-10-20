def median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle = length // 2
    if length % 2 == 1:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2.0
