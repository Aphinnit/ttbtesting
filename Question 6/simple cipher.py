# A simple cipher is built on the alphabet wheel which has uppercase English letters ['A'-'Z'] written on It:
# Given an encrypted string consisting of English letters ['A'-'Z'] only, decrypt the string by replacing each character with the kth character away on the wheel in the
 
# counterclockwise direction, Counter-clockwise is the opposite direction in which the hands on a clock usually move.


def simpleCipher(encrypted, k):
    decrypted = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in encrypted:
        # Find the index of the character in the alphabet
        index = alphabet.index(i)
        # Calculate the index after moving k positions counter-clockwise
        new_index = (index - k) % 26
        # Append the decrypted character to the decrypted string
        decrypted += alphabet[new_index]
    
    return decrypted

# Example usage:
encrypted = 'VTAOG'
k = 2
print(simpleCipher(encrypted, k))  # Output: 'TRYME'
