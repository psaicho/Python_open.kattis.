def check_palindrome(text):
    return True if text.upper().replace(" ", "") == text[::-1].replace(" ", "").upper() else False

print(check_palindrome("Kobyła ma mały bok"))

