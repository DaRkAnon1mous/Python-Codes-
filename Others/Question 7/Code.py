def repfree(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# Test cases for repfree
print(repfree("zb%78"))      # Output: True
print(repfree("(7)(a"))      # Output: False
print(repfree("a)*(?"))      # Output: True
print(repfree("abracadabra"))# Output: False
