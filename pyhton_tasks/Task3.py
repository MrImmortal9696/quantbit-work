def first_unique_char(s: str) -> str:
    char_count = {}  # Dictionary to count how much time has each character appear

    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return "None"  # If all characters repeat

# Example usage:
s = "swiss"
print(first_unique_char(s))  
