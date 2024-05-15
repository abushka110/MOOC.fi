# Write your solution here:
class Person:
    def __init__(self, name) -> None:
        self.__person_name = name
        self.__person_numbers = []
        self.__person_address = None

    def name(self):
        return self.__person_name
    
    def numbers(self):
        return self.__person_numbers
    
    def address(self):
        return self.__person_address
    
    def add_number(self, number_to_add):
        self.__person_numbers.append(number_to_add)

    def add_address(self, address_to_add):
        self.__person_address = address_to_add


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    # def add_number(self, name: str, number: str):
    #     for person in self.__persons:
    #         if person.

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        if numbers == None:
            print("number unknown") 
            return 
        for number in numbers:
            print(number)       

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
