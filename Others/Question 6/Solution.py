def threesquares(m):
  if m <= 0:
      return False

  # Loop through all possible combinations of p, q, r
  for p in range(int(m**0.5) + 1):
      for q in range(int(m**0.5) + 1):
          for r in range(int(m**0.5) + 1):
              if p**2 + q**2 + r**2 == m:
                  return True
  return False

# Test cases for threesquares
print(threesquares(6))   # Output: True
print(threesquares(188)) # Output: False
print(threesquares(1000))# Output: True
