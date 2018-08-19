import protobuf.word_pb2
import json

class Converter:
    def __init__(self, pathToSourceData, pathToDestinationData):
        self.src = pathToSourceData
        self.dest = pathToDestinationData
        self.supportedExtentions = ["json", "vocalist"]
        self.srcExtention = self.getExtention(pathToSourceData[1:])
        self.destExtention = self.getExtention(pathToDestinationData[1:])
        if ("jsontovocalist" == self.srcExtention + "to" + self.destExtention):
            self.jsonToVocalist()

    def getExtention(self, path):
        _, extention = path.split(".")
        if self.isValidExtention(extention):
            return extention
        else :
            raise Exception("Unknown file format")

    def isValidExtention(self, extentionToTest):
        if extentionToTest in self.supportedExtentions:
            return True
        return False

    def fetchData(self):
        srcFile = open(self.src, "r")
        fetchedData = srcFile.read()
        srcFile.close()
        return fetchedData

    def jsonToVocalist(self):
        srcData = json.loads(self.fetchData())
        wordsInProtobuf = protobuf.word_pb2.VocabularyWords()
        self.processJsonToVocalist(srcData, wordsInProtobuf)
        self.savingData(wordsInProtobuf)

    def processJsonToVocalist(self, jsonData, wordslist ):
        print(jsonData)
        for jsonPart in jsonData :
            for word in jsonData[jsonPart]:
                print(word)
                self.addingWord(wordslist.words.add(), word)

    def addingWord(self, vocalistWord, data):
        vocalistWord.wordInFirstLang = data["ge"]
        vocalistWord.firstLang = protobuf.word_pb2.Word.GERMAN
        vocalistWord.wordInSecondLang = data["fr"]
        vocalistWord.secondLang = protobuf.word_pb2.Word.FRENCH
        if ("inflection" in data.keys()):
            vocalistWord.inflection = data["inflection"]
        if ("plural" in data.keys()):
            vocalistWord.plural = data["plural"]
        if ("comment" in data.keys()):
            vocalistWord.comment = data["comment"]
        print(vocalistWord)

    def savingData(self, wordslist):
        f = open(self.dest, "wb")
        f.write(wordslist.SerializeToString())
        f.close()
