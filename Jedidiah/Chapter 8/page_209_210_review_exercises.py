word = input("Enter a word: ")
if len(word) > 5:
    print("The length of the word is greater than 5 letters.")
elif len(word) == 5:
    print("The length of the word is 5 letters.")
else:
    print("The length of the word is fewer than 5 letters.")