sentence = input("Please type in a string: ")

vowels = "aeo"

index = 0

while index < len(vowels):
    vowel = vowels[index]
    if vowel in sentence:
        print(vowel + " found")
    else:
        print(vowel + " not found")
    index += 1
