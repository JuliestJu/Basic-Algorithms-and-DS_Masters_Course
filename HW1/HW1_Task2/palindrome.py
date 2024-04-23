from collections import deque

def is_palindrome(s):
    # Normalize the string: lower case and remove spaces
    normalized_string = ''.join(ch.lower() for ch in s if ch.isalnum())
    char_deque = deque(normalized_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

s = ""
result = is_palindrome(s)
print(result)