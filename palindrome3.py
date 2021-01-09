word = input("enter a string:")
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print("the middle of the word: ",middle(word))
print("the word is palindrome or not: ",is_palindrome(word))
