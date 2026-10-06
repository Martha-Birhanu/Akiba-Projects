word=input("Enter a word you want to check: ")

word=word.lower()      # to make the word in lowercase 

is_palindrome= True        # assumption 
for i in range(0, len(word)):
    if word[i] != word[len(word)-(i+1)]:
       is_palindrome = False
       break  # break because got letters proves the assumption wrong.
if is_palindrome:
    print(f"the word {word} is palindrome!")
else:
    print(f"the word {word} is not palindrome!")