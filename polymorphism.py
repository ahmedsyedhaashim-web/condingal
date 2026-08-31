class cricket:
    def__init_(self, player, score):
        self.player = player
        self.score = score
    def info(self):
        print(f'cricket - player: {self.__player}, Score: {self.__score}"end)
    def play(self):
        print(f"{self.__player} hits a six!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to {self.__score}")
            else:
            print("score cannot be negative")

class football:
def __init__(self, player, score):