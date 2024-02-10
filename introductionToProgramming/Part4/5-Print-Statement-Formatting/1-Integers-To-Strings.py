#  solution
def formatted(floatList: list):
    formattedList = []
    for number in floatList:
        formattedList.append(f"{number:.2f}")
    return formattedList

#  test
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list) # ['1.23', '0.33', '0.11', '3.45']