# 14. Function to check whether a string is palindrome
def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

print("Palindrome:", palindrome("mom"))
