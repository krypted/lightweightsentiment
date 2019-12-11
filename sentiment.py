import json

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


# -----------------------------------------------------------
# Sentiment class returns Polarity Score if no file is given else returns label probability distribution that is
# 0 for neg 1 for pos depending on the file passed
# --------------------------------------------------
class Sentiment:
    def __init__(self):
        file = 'data.json'
        self.file = file
        cl = False
        if file is not None:
            with open(file, 'r') as fp:
                cl = NaiveBayesClassifier(fp, format="json")
        self.cl = cl

    # Tested, brings a better accuracy if you use something like .0001 as the threshold for the polarity
    def get_score(self, text):
        cl = self.cl

        if cl:
            prob_dist = cl.prob_classify(text)
            return round(prob_dist.prob("pos"), 4)
        else:
            analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def add_text(self, text, label):

        with open(self.file, 'r') as f:
            data = json.load(f)
        duplicate = False
        for key, line in enumerate(data):
            if line['text'] == text:
                data[key] = {'text': text, 'label': label}
                duplicate = True
        if not duplicate:
            data.append({'text': text, 'label': label})
        with open(self.file, 'w') as f:
            json.dump(data, f)
