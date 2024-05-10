# solution
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
    
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouy"
        player1_vowels_count = 0
        for letter in player1_word:
            if letter in vowels:
                player1_vowels_count += 1
        
        player2_vowels_count = 0
        for letter in player2_word:
            if letter in vowels:
                player2_vowels_count += 1

        if player1_vowels_count > player2_vowels_count:
            return 1
        elif player1_vowels_count < player2_vowels_count:
            return 2
            

# test
# if __name__ == "__main__":