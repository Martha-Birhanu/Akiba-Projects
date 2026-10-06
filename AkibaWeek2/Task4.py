word=input("Enter a word you want to check: ")

is_palindrome= True
for i in range(0, len(word)):
    if word[i] != word[len(word)-(i+1)]:
       is_palindrome = False
       break
if is_palindrome:
    print(f"the word {word} is palindrome!")
else:
    print(f"the word {word} is not palindrome!")