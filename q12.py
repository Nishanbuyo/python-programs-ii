def is_palindrome(str1):
    return str1== str1[::-1]

input_str = input("Enter the string: ")
is_palindrome = is_palindrome(input_str)

if is_palindrome:
    print("palindrome")
else:
    print("Not palindrome")