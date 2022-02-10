def is_palindrome(word):
    if len(word)<=1:
        return True
    else:
            if word[0]==word[-1]:
                return is_palindrome(word[1:-1])
            else:

                return False
words=["tacocat","Miran","arara", "wsw","kayak","dan"]
for word in words:
    print("the word",word,is_palindrome(word))
