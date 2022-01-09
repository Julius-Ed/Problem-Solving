"""
Encrypted Words
"""

# recursive approach.
def encrypted_words(S):


    R = ""

    if len(S) % 2 != 0:
        middle = len(S) // 2
    else:
        middle = (len(S) // 2) - 1
    
    R += S[middle]

    left = S[:middle]
    right = S[middle +1:]

    if middle > 0:
        R += encrypted_words(left)
    
    if middle < len(S) - 1:
        R += encrypted_words(right)

    return R




#print(encrypted_words("abc") == "bac")
#print(encrypted_words("abcd") == "bacd")
#print(encrypted_words("Facebook"))