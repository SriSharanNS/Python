def largest(numbers):
    large=numbers[0]
    for item in numbers:
        if item>large:
            large=item
    return large 
def smallest(numbers):
    small=numbers[0] 
    for item in numbers:
        if item<small:
            small=item 
    return small          