import argparse
from sentiment import Sentiment
parser = argparse.ArgumentParser(prog='sentiment analyser')
parser.add_argument('--text', metavar='N', type=str, nargs='?', help='Text to analyse')
parser.add_argument('--file', metavar='N', type=str, nargs='?', help='Text training')
args = parser.parse_args()

text = args.text
file = args.file
sentiment = Sentiment(file)
print(sentiment.get_score(text))
