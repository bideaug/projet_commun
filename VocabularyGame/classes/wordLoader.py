import json
from .word import Word

class WordLoader:
    def __init__(self, pathToData, dataFormat):
        self.pathToData = pathToData
        self.dataFormat = dataFormat
        self.words = []
        self.availableOptions = ["inflection","comment","plural"]
        self.creatingWords(self.FetchingJsonData())

    def getWords(self):
        if (len(self.words) == 0 ) :
            self.creatingWords(FetchingJsonData())
        if (len(self.words) == 0):
            raise Error("The data must be corrupted!")
        return self.words

    def FetchingJsonData(self):
        with open(self.pathToData, 'r') as jsonDataFile :
            jsonData = jsonDataFile.read().replace('\n', '')
        return json.loads(jsonData)

    def creatingWords(self, jsonData):
        for data in jsonData["words"] :
            currentWord = Word(data["ge"], data["fr"])
            for opt in self.availableOptions :
                try:
                    currentWord.setAnOption(opt, data[opt])
                except KeyError:
                    pass
            self.words.append(currentWord)

if __name__ == '__main__':
    wordLoader = WordLoader("../data/lvl1.json", "json")
    #wordLoader.creatingWords(wordLoader.FetchingJsonData())

    for word in wordLoader.getWords():
        print(word)
