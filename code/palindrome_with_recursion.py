def is_palindrome(string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz'
    
    if len(string) == 1:
        return True
    
    if string[0].lower() not in allowed_chars:
        return is_palindrome(string[1:])
    
    if string[len(string)-1].lower() not in allowed_chars:
        return is_palindrome(string[:-1])
    
    if string[0].lower() == string[len(string)-1].lower():
        return is_palindrome(string[1:-1])
    
    return False    
    


        
s = 'Go hang a salami; I’m a lasagna hog'
print(is_palindrome(s))

s = 'Reviled did I live, said I, as evil I did deliver'
print(is_palindrome(s))

s = 'Wassamassaw – a town in South Dakota'
print(is_palindrome(s))

s = 'Kanakanak – a town in Alaska'
print(is_palindrome(s))

s = 'Able was I ere I saw Elba'
print(is_palindrome(s))
