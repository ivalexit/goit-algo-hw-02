from collections import deque
import time

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    str_deque = deque(cleaned_string)

    while len(str_deque) > 1:
        if str_deque.popleft() != str_deque.pop():
            return False 
        
    return True


check_palindrome = input("Input a phrase/word to check if it's a palindrome: ")

start_time = time.time()

if is_palindrome(check_palindrome):
    print(f'"{check_palindrome}" is a palindrome.')
else:
    print(f'"{check_palindrome}" is not a palindrome.')

end_time = time.time()
execution_time = end_time - start_time 

print(f"Execution time: {execution_time:.6f} sec")



# Реалізація через список, завдання виконується довше приблизно на 40%

# import time

# def is_palindrome(input_string):
#     cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
#     str_list = list(cleaned_string)


#     while len(str_list) > 1:
#         if str_list.pop(0) != str_list.pop():
#             return False
        
#     return True

# check_palindrome = input("Input a phrase/word to check if it's a palindrome: ")

# start_time = time.time()

# if is_palindrome(check_palindrome):
#     print(f'"{check_palindrome}" is a palindrome.')
# else:
#     print(f'"{check_palindrome}" is not a palindrome.')

# end_time = time.time()
# execution_time = end_time - start_time  # Обчислення часу виконання

# print(f"Execution time: {execution_time:.6f} sec")