import argparse
from sentiment import Sentiment
parser = argparse.ArgumentParser(prog='sentiment analyser')
parser.add_argument('--text', metavar='N', type=str, nargs='?', help='Text to analyse')
args = parser.parse_args()

text = args.text
sentiment = Sentiment()
print(sentiment.get_score(text))

# to add to data.json just call
sentiment.add_text('my bird hates me', 'neg')