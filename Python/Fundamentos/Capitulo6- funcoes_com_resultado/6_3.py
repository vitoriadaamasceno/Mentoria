word = "araraa"
def first(word):
    if word!='':
        return word[0]
    else:
        return None
def last(word):
    if word!='':
        return word[-1]
    else:
        return None
def middle(word):
    if word!='':
        return word[1:-1]
    else:
        return None


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

        
print(is_palindrome(word))