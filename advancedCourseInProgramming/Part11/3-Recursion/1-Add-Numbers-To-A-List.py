# solution
def add_numbers_to_list(numbers: list):
    while len(numbers) % 5 != 0:
        numbers.append(numbers[len(numbers) - 1] + 1)
        add_numbers_to_list(numbers)
        
# test
if __name__ == "__main__":
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)
