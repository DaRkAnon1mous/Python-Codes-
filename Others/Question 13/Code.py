def longest_palindrome_subword(word):
    n = len(word)
    max_length = 0
    max_subword = ""

    for i in range(n):
        # For odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and word[l] == word[r]:
            if r - l + 1 > max_length:
                max_length = r - l + 1
                max_subword = word[l:r+1]
            l -= 1
            r += 1

        # For even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and word[l] == word[r]:
            if r - l + 1 > max_length:
                max_length = r - l + 1
                max_subword = word[l:r+1]
            l -= 1
            r += 1

    return max_length, max_subword

# Read input
N = int(input())
word = input().strip()

# Get the longest palindrome subword
length, subword = longest_palindrome_subword(word)

# Print output
print(length)
print(subword)
