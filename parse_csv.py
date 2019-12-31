import argparse
import csv
from sentiment import Sentiment

sent = Sentiment()
parser = argparse.ArgumentParser(prog='Tagger')
parser.add_argument('--file', metavar='N', type=str, nargs='?', help='File')
parser.add_argument('--column', metavar='N', type=str, nargs='?', help='Column name')
args = parser.parse_args()
file_ = args.file
column = args.column
if not file_ or not column:
    raise Exception("--file and --column options must be set")

rows_header = []
rows = []
with open(file_, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            row["Score"] = ""
            rows_header = row.keys()
            line_count += 1
        text = row[column]
        score = sent.get_score(text)

        row['Score'] = score
        # row.append({score: score})

        rows.append(row)
parts = str(file_).split('.')
filename = parts[0]+"_sentiment."+parts[1]

with open(filename, mode='w') as sentiment_file:
    sentiment_writer = csv.writer(sentiment_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sentiment_writer.writerow(rows_header)
    for row in rows:
        sentiment_writer.writerow(row.values())