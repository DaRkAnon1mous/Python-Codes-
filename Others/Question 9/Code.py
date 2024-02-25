def hillvalley(l):
    """
    Returns True if the list l is a hill or a valley, and False otherwise.
    """
    if len(l) < 4:
        return False

    # Check for ascending sequence followed by descending sequence
    for i in range(1, len(l) - 2):
        if l[i] < l[i + 1] and l[i + 1] > l[i + 2]:
            return True

    # Check for descending sequence followed by ascending sequence
    for i in range(1, len(l) - 2):
        if l[i] > l[i + 1] and l[i + 1] < l[i + 2]:
            return True

    return False

# Test cases
print(hillvalley([1, 2, 3, 5, 4]))  # Expected: True
print(hillvalley([1, 2, 3, 4, 5]))  # Expected: False
print(hillvalley([5, 4, 1, 2, 3]))  # Expected: True
print(hillvalley([5, 4, 3, 2, 1]))  # Expected: False
