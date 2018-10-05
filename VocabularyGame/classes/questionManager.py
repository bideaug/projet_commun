class QuestionManager:
    def __init__(self, words, goodAnwser):
        self.goodAnwser = goodAnwser
        self.choices = words

    def ensureGoodAnwserIsAvailable(self):
        return self.goodAnwser in self.choices



    
