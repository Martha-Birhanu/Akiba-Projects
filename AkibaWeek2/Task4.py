
def isPalindrome(word):
    word=word.lower()  # to make the word in lowercase
    for i in range(len(word)):
        if word[i] != word[len(word)-(i+1)]:
            return False  # break because got letters proves the assumption wrong.
    return True     

word=input("Enter a word you want to check: ")
print(isPalindrome((word)))




