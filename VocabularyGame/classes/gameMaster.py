from .word import Word as w
from .wordLoader import WordLoader

class GameMaster:
    def __init__(self, words, numberOfQuestions = 20):
        self.wordsManager = WordLoader("./data/lvl1.json", "json")
        self.wordsManager.creatingWords(self.wordsManager.FetchingJsonData())
        self.numberOfQuestions = numberOfQuestions
        self.numberOfError = 0

    def pickAWord(self):
        return self.availableWords[0]


if __name__ == '__main__':
    gm = GameMaster(["coucou", "oups"])
    print(gm.pickAWord())
