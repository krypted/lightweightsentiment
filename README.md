# lightweightsentiment
lightweightsentiment is a Lightweight Sentiment Analysis Tool built using python. 

## Requirements
It was written to conform to python 2 or 3 and requires the following modules installed (newer versions may work):

nltk==3.4.5

textblob==0.15.3

To install nltk run:

python3 -m textblob.download_corpora

## Usage

Simply call the script using python3:

python3 input.py --text "Gosh, I hate this feature"

### Expected Output

The output would then be a number between -1.0 and 1.0. For example:

-0.8

### Training the Data Model

The data.json contains the model. You can add information programmatically using a seperate tool or train the data.json file using the --train option:

python input.py --train="This is an great python script!" --label="pos"

### CSV Usage

The sentiment.py script is called by a parsing script called parse_csv.py. The data.json and input.py scripts should be in the same directory as well, with data.json acting as the model's training data. 

python3 parse_csv.py --file="Episodes_analysis_page.csv" --column="Group Description"


## Microservice

This is module across scripts so a service could be hosted as a lambda or google cloud function to process a csv or manual call per line. This facilitates calling from another application by simply sending the text in a standard json format with a response of the same floating point integer. 
