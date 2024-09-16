def reverse_string_with_stack(input_string):
    stack = []
    
    for char in input_string:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

user_input = input("문자열을 입력하세요: ")


reversed_output = reverse_string_with_stack(user_input)
print("역순 문자열:", reversed_output)
