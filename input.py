import argparse
from sentiment import Sentiment
parser = argparse.ArgumentParser(prog='sentiment analyser')
parser.add_argument('--text', metavar='N', type=str, nargs='?', help='Text to analyse')
parser.add_argument('--train', metavar='N', type=str, nargs='?', help='Add text to train')
parser.add_argument('--label', metavar='N', type=str, nargs='?', help='label for text to train')
args = parser.parse_args()

text = args.text
sentiment = Sentiment()
train = args.train
label = args.label
if text:
    print(sentiment.get_score(text))


if train and label:
    # to append just call
    sentiment.add_text(train, label)
