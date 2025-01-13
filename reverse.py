word = input("word pls ")

print(word)



def plaidrome(word):
    if word == word[::-1]:
        print("is")

plaidrome(word)