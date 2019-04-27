def find_missing_number(list_numbers):
    
    for num in range(1, len(list_numbers) + 1):
        if num not in list_numbers:
            return num
