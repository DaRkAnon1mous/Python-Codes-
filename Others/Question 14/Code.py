def intreverse(n):
    # Convert the integer to a string
    n_str = str(n)
    
    # Reverse the string
    reversed_str = n_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_int = int(reversed_str)
    
    return reversed_int
