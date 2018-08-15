from classes.gameMaster import GameMaster
from classes.levelManager import LevelManager
from classes.question import Question
from classes.wordLoader import WordLoader

def main():
    # levelManager = LevelManager()
    # print(levelManager.getSelectedLevel())

    wl = WordLoader("./data/lvl1.json", "json")
    q = Question(wl.getWords())



if __name__ == '__main__':
    main()
