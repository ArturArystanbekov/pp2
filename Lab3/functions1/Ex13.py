def is_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")
        
word = input("Enter a phrase: ")
is_palindrome(word)