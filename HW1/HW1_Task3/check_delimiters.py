
def check_delimiters(expression):
    # Stack to keep track of opening delimiters
    stack = []
    # Mapping of opening to closing delimiters
    matching_delimiter = {'(': ')', '[': ']', '{': '}'}
    
    # Iterate through each character in the string
    for char in expression:
        if char in matching_delimiter:
            # It's an opening delimiter
            stack.append(char)
        elif char in matching_delimiter.values():
            # It's a closing delimiter
            if not stack or matching_delimiter[stack.pop()] != char:
                return "Несиметрично"
    
    # If stack is empty, all delimiters were matched
    return "Симетрично" if not stack else "Несиметрично"

# Test the function with examples
print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Should return 'Симетрично'
print(check_delimiters("( 23 ( 2 - 3);"))  # Should return 'Несиметрично'
print(check_delimiters("( 11 }"))  # Should return 'Несиметрично'