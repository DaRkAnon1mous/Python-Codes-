def hillvalley(l):
    if len(l) < 4:
        return False

    increasing = decreasing = False

    # Check for an ascending sequence
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            increasing = True
        elif l[i] < l[i - 1]:
            break

    # Check for a descending sequence
    for i in range(len(l) - 1, 0, -1):
        if l[i] > l[i - 1]:
            break
        elif l[i] < l[i - 1]:
            decreasing = True

    return increasing and decreasing


# Test cases
print(hillvalley([1, 2, 3, 5, 4]))  # Expected: True
print(hillvalley([1, 2, 3, 4, 5]))  # Expected: False
print(hillvalley([5, 4, 1, 2, 3]))  # Expected: True
print(hillvalley([5, 4, 3, 2, 1]))  # Expected: False
