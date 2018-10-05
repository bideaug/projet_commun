from .word import Word as w
from .wordLoader import WordLoader
from .levelManager import LevelManager
import os

class GameMaster:
    def __init__(self, numberOfQuestions = 20):
        self.levelManager = LevelManager()
        self.appDirectory = os.path.dirname(os.path.realpath("VocabularyGame"))
        self.wordsManager = WordLoader(self.appDirectory + "/data/lvl"+str(self.levelManager.getSelectedLevel())+".json", "json")
        self.wordsManager.creatingWords(self.wordsManager.FetchingJsonData())
        self.numberOfQuestions = numberOfQuestions
        self.numberOfError = 0

    def pickAWord(self):
        return self.availableWords[0]


if __name__ == '__main__':
    gm = GameMaster(["coucou", "oups"])
    print(gm.pickAWord())
