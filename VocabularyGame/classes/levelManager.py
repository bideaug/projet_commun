import os

class LevelManager:
    def __init__(self, selectedLevel = None):
        self.availableLevelList = self.getAvailableLevelList()
        self.selectedLevel = selectedLevel
        if (self.selectedLevel == None):
            self.selectALevel()

    def selectALevel(self):
        print("Here are the available level : ")
        self.displayListOfAvailableLevel()
        self.selectedLevel = int(self.askForTheWantedLevel())
        print("in selectALevel : " + str(self.selectedLevel))

    def displayListOfAvailableLevel(self):
        for lvl in self.availableLevelList :
            print("Level : " + lvl + " ")

    def askForTheWantedLevel(self):
        selectedLevel = input('>>> ')
        print("selectedLevel : " + selectedLevel)
        try :
            selectedLevel = int(selectedLevel)
        except ValueError :
            return self.selectALevel()
        if (self.isValidLevel(selectedLevel)) :
            return selectedLevel
        else :
            return self.selectALevel()

    def isValidLevel(self, levelToVerify):
        return str(levelToVerify) in self.availableLevelList


    def parsingLevelIdFromFileName(self, fileName):
        return fileName.split(".")[0].split("lvl")[1]

    def getAvailableLevelList(self) :
        appDirectory = os.path.dirname(os.path.realpath("VocabularyGame"))
        filesInData = os.listdir(appDirectory + "/data/")
        lvlIds = []
        for file in filesInData :
            lvlIds.append(self.parsingLevelIdFromFileName(file))
        return lvlIds


    def getSelectedLevel(self):
        if (self.selectedLevel == 0) :
            self.selectALevel()
        print(self.selectedLevel)
        return self.selectedLevel
