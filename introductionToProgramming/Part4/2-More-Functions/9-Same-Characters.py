# Write your solution here
def same_chars(word, index, index1):
    if len(word) - 1 < index or len(word) - 1 < index1:
        return False
    else:
        if word[index] == word[index1]:
            return True
        else:
            return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False