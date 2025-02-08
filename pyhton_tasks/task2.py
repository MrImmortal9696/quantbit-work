def is_valid(s: str) -> bool:
    stack = []                              # To store opening brackets
    pairs = {')': '(', '}': '{', ']': '['}  # Matching pairs

    for char in s:
        if char in pairs.values():          # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in pairs:                 # If it's a closing bracket
            if not stack or stack.pop() != pairs[char]:  # Check if it matches the last opening
                return False

    return not stack                         # If stack is empty, it's balanced

# Example usage:
print(is_valid("{[()]}"))  # True
print(is_valid("{[(])}"))  # False
